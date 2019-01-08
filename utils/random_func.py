import random
from faker import Factory

fake = Factory().create('zh_CN')
def random_name():
    """随机中文姓名"""
    return fake.name()

def random_name_en():
    """随机英文字母姓名"""
    full_name = "atuo_" + fake.first_romanized_name()
    return full_name

def random_phone_number():
    """随机手机号"""
    return fake.phone_number()

def random_email():
    """随机email"""
    return fake.email()

def random_str(min_chars, max_chars):
    """随机可控长度字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)

def random_address():
    """随机地址"""
    return fake.address()

def random_company():
    """随机公司名"""
    return fake.company()

if __name__ == '__main__':
    print(random_name())
    print(random_name_en())
    print(random_phone_number())
    print(random_address())
    print(random_email())
    print(random_str(5, 7))
    print(random_company())
