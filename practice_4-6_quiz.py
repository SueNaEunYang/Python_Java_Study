#print(pow(4,2))
#print(max(5,10))
#print(round(3.14))

#from math import *
#print(floor(4.99))
#print(ceil(3.14))
#print(sqrt(16))

#from random import *
#print(random())
#print(random()*10)

#Quiz 3 Sue's answer
page= "http://naver.com"
index = page.index(".")
beforedot = page[7:index]
first3 = page[7:10]
count = len(beforedot)
counte = beforedot.count("e")
password = str(first3) + str(count) + str(counte) + "!"
print("생성된 비밀번호 : " + password)

#Quiz 3 Teacher's answer
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

