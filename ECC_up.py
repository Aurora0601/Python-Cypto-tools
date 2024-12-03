from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def generate_keys():
    # 生成ECC密钥对
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_key(key):
    # 序列化密钥以便存储或传输
    if isinstance(key, ec.EllipticCurvePrivateKey):
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        return key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

def encrypt(public_key, plaintext):
    # 生成一个随机的对称密钥（用于加密明文）
    ephemeral_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    ephemeral_public_key = ephemeral_private_key.public_key()
    shared_key = ephemeral_private_key.exchange(ec.ECDH(), public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ECC Encryption Handshake',
        backend=default_backend()
    ).derive(shared_key)

    # 使用对称密钥加密明文
    iv = os.urandom(12)  # 初始化向量
    cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # 返回密文、认证数据和ephemeral公钥
    return ciphertext, iv + encryptor.tag, serialize_key(ephemeral_public_key), serialize_key(ephemeral_private_key)

# 输入明文
plaintext = input("请输入要加密的明文（以字节串形式，如'This is a secret message.'的编码）：")
if isinstance(plaintext, str):
    plaintext = plaintext.encode('utf-8')  # 确保明文是字节串

# 生成密钥对
private_key, public_key = generate_keys()

# 加密明文
ciphertext, auth_data, ephemeral_pub_key, ephemeral_priv_key = encrypt(public_key, plaintext)

print("密文：", ciphertext)
print("认证数据：", auth_data)
print("Ephemeral 公钥：", ephemeral_pub_key.decode('utf-8'))
print("Ephemeral 私钥：", ephemeral_priv_key.decode('utf-8'))
