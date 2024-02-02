#coding=utf-8
import random
import string
import codecs

StringBase='\u7684\u4e00\u662f\u4e86\u6211\u4e0d\u4eba\u5728\u4ed6\u6709\u8fd9\u4e2a\u4e0a\u4eec\u6765\u5230\u65f6\u5927\u5730\u4e3a\u5b50\u4e2d\u4f60\u8bf4\u751f\u56fd\u5e74'
#StringBase=''.join(StringBase.split('\\u'))

def getEmail():#邮箱地址
    suffix=['.com','.org','.net','.cn'] #后缀
    characters=string.ascii_letters+string.digits+'_'
    username=''.join(random.choice(characters) for i in range(random.randint(6,12))) #随机生成用户名
    domain=''.join(random.choice(characters) for i in range(random.randint(3,6)))#随机生成域名
    return username+'@'+domain+random.choice(suffix)

def getTelNo():#电话号码
    return ''.join((str(random.randint(0,9))) for i in range(11))

def getNameOrAddress(flag): #flag=1返回随机姓名,flag=0返回随机地址
    result=''
    if flag==1:
        rangestart,rangeend=2,5 #姓名
    elif flag==0:
        rangestart,rangeend=10,31 #地址
    else:
        print('flag must be 1 or 0')
        return ''
    for i in range(random.randrange(rangestart,rangeend)):
        result += random.choice(StringBase)
    return result

def getSex():#性别
    return random.choice(('男','女'))

def getAge():#年龄
    return str(random.randint(18,100))

def main(filename):
    with open(filename,'w',encoding='utf-8') as fp:
        for i in range(200):
            name=getNameOrAddress(1)
            sex=getSex()
            age=getAge()
