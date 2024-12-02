# Python-Cypto-tools
一款基于python的在命令台运行的密码学工具箱V1.0版
需要python3环境
所需要的支持库
1.Naked	0.1.32	0.1.32
2.Padding	0.5	0.5
3.PyYAML	3.11	6.0.2
4.arithmetic	0.6.2	0.6.2
5.base58	2.1.1	2.1.1
6.base91	1.0.1	1.0.1
7.certifi	2024.7.4	2024.8.30
8.cffi	1.17.1	1.17.1
9.charset-normalizer	3.3.2	3.4.0
10.click	6.2	8.1.7
11.continuedfractions	0.17.6	0.18.2
12.cryptography	43.0.3	44.0.0
13.distlib	0.3.9	0.3.9
14.enum-compat	0.0.3	0.0.3
15.filelock	3.16.1	3.16.1
16.future	1.0.0	1.0.0
17.gmpy2	2.2.0	2.2.1
18.gmssl	3.2.2	3.2.2
19.hashes	1.1.0	1.1.0
20.idna	3.7	3.10
21.libnum	1.7.1	1.7.1
22.mpmath	1.3.0	1.3.0
23.numpy	2.1.3	2.1.3
24.passlib	1.7.4	1.7.4
25.pip	24.1.2	24.3.1
26.platformdirs	4.3.6	4.3.6
27.pluggy	0.3.1	1.5.0
28.py	1.11.0	1.11.0
29.py-bcrypt	0.4	0.4
30.pyasn1	0.6.1	0.6.1
31.pycparser	2.22	2.22
32.pycryptodome	3.21.0	3.21.0
33.pycryptodomex	3.21.0	3.21.0
34.rabbit	1.2.0	1.2.0
35.requests	2.32.3	2.32.3
36.rsa	4.9	4.9
37.serialization	1.2.3	1.2.3
38.setuptools	75.3.0	75.6.0
39.shellescape	3.8.1	3.8.1
40.six	1.16.0	1.16.0
41.sympy	1.13.0	1.13.3
42.tox	2.2.1	4.23.2
43.urllib3	2.2.2	2.2.3
44.virtualenv	20.27.1	20.28.0
45.virtualenv	20.27.1	20.28.0
本工具提供了bat文件，便于打开命令台直接使用，可以自己将后缀改为TXT打开检查是否为为病毒
运行main函数可以直接查看帮助文档
例：python main.py
python密码学脚本帮助文档
使用方法：输入python base16off.py即可运行base16解密
以下是对照表
编码
base加解密
1.base16off.py     base16解密
2.base16up.py     base16加密
3.base32off.py     base32解密
4.base32up.py     base32加密
5.base36off.py     base36解密
6.base36up.py     base36加密
7.base58off.py     base58解密
8.base58up.py     base58加密
9.base62off.py     base62解密
10.base62up.py     base62加密
11.base64off.py     base64解密
12.base64up.py     base64加密
13.base85off.py     base85解密
14.base85up.py     base85加密
15.base91off.py     base91解密
16.base91up.py     base91加密
17.base92off.py     base92解密
18.base92up.py     base92加密
其他编码
1.hex off   hex解码
2.hex up   hex编码
3.ROT5 off   ROT5解密
4.ROT5 up   ROT5解码
5.ROT13 off   ROT13解密
6.ROT13 up   ROT13解码
7.ROT18 off   ROT18解密
8.ROT18 up   ROT18解码
9.ROT47 off   ROT47解密
10.ROT47 up   ROT47解码
11.Tap Code off  敲击码解密
12.Tap Code up  敲击码加密
13.Unicode off    Unicode解码
14.Unicode up    Unicode编码
15.UrlBase64 off  UrlBase64解码
16.UrlBase64 up UrlBase64编码
17.UrlEncode off  UrlEncode解码
18.UrlEncode up   UrlEncode编码
19.UTF8 off      UTF8解码
20.UTF8 up      UTF8编码
21.UTF16 off    UTF16解码
22.UTF16 up    UTF16编码
23.Binary up     将字符转二进制
24.Binary off     将二进制转字符
25.ASCLL-STRING   将ASCLL码转字符串
26.STRING-ASCLL   将字符串转ASCLL码
古典密码加解密
1.Affine Cipher off    仿射密码解密
2.Affine Cipher up    仿射密码加密
3.Atbash Cipher        埃特巴什码（加解密同一个）
4.Bacon's Cipher off 培根密码解密
5.Bacon's Cipher up 培根密码加密
6.Caesar Cipher off   凯撒密码解密
7.Caesar Cipher up   凯撒密码加密
8.Morse Code off     摩斯密码加密
9.Morse Code up     摩斯密码解密
10.Playfair Cipher off  曲路密码解密
11.Playfair Cipher up  曲路密码加密
12.Playfair off    Playfair加密
13.Playfair up    Playfair解密
14.Polybius off  方块密码解密
15.Polybius up  方块密码加密
16.Rail Fence Cipher off  栅栏密码解密
17.Rail Fence Cipher up  栅栏密码加密
18.Vigenère Cipher off    维吉尼亚密码解密
19.Vigenère Cipher up    维吉尼亚密码加密
20.ZUC Cipher off      祖冲之密码解密
21.ZUC Cipher up      祖冲之密码加密
哈希加密
1.MD5 up  MD5加密
2.SHA1 up  SHA1加密
3.SHA224 up  SHA224加密
4.SHA256 up  SHA256加密
5.SHA384 up  SHA384加密
6.SHA512 up  SHA512加密
7.HmacSHA1 up  HmacSHA1加密
8.HmacSHA224 up  HmacSHA224加密
9.HmacSHA256 up  HmacSHA256加密
10.HmacSHA384 up  HmacSHA384加密
11.HmacSHA512 up  HmacSHA512加密
12.Shacal up   Shacal加密
13Shacal off   注：验证完整性和真实性
对称加解密
1.SMS4 up  SMS4加密
2.SMS4 off  SMS4解密
3.DES up     DES加密
4.DES off     DES解密
5.3DES up   3DES加密
6.3DES off   3DES解密
7.AES up      AES加密
8.AES off    AES加密
9.RC2 up    RC2加密
10.RC2 off    RC2解密
11.RC4 up    RC4加密
12.RC4 off    RC4加密
13.XOR up    异或加密
14.XOR off    异或解密
15.Zuc128 up  Zuc128加密
16.Zuc128 off  Zuc128解密
17.Salsa20 up   Salsa20加密
18.Salsa20 off   Salsa20解密
19.OCB up   OCB模式加密
20.OCB off   OCB模式解密
21.OFB up    OFB模式加密
22.OFB off    OFB模式解密
23.HC128.HC256 up   HC128.HC256加密
24.HC128.HC256 off   HC128.HC256解密
25.Grainv1 up    Grainv1 加密
26.Grainv1 off    Grainv1解密
27.Grain-128 up   Grain-128加密
28.Grain-128 off   Grain-128解密
29.GCM up   GCM加密
30.GCM off   GCM解密
31.ECB up     ECB加密
32.ECB off     ECB解密
33.EAX up     EAX加密
34.EAX off     EAX解密
35.CTS up     CTS加密
36.CTS off     CYS解密
37.ChaCha up   ChaCha加密
38.ChaCha off   ChaCha解密
39.CFB up    CFB加密
40.CFB off    CFB解密
41.CCM up   CCM加密
42.CCM off   CCM解密
43.CBC up     CBC加密
44.CBC off     CBC解密
45.BLOWFISH up   BLOWFISH加密
46.BLOWFISH off   BLOWFISH解密
非对称加密
1.RSA  RSA加密
2.SM2  SM2加密
3.ECC   ECC加密
其他
1.Radix Conversion   进制转换
2.reverse order         字符串倒序
您可以随时使用python main.py来查看帮助文档，祝您使用愉快！
