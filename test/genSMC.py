import hmac
import hashlib
import random
import string

# 随机生成一个32位的密钥
secret_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
print(secret_key)
# 要加密的数据
data = 'hello world'

# 使用HMAC算法进行加密，并指定使用SHA-1算法进行哈希
hmac_obj = hmac.new(secret_key.encode(), data.encode(), hashlib.sha1)

# 生成长度为20的字符令牌字符串
token = hmac_obj.digest().hex()[:20]

print(token)
