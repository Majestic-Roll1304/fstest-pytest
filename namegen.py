import random
import string

def namegen():
    name='pjdfstest_'
    name+=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=10))
    return  name
