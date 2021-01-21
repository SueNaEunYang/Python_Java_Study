#활용예시
#from random import *
#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst, 1))

#Sue's Answer
import random
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chicken = random.sample(lst,1)
lst=set(lst)
lst=lst.difference(set(chicken))
coffee = (random.sample(lst,3))
lst=list(lst)
print("-- 당첨자 발표 --")
print("치킨 당첨자: " + str(chicken))
print("커피 당첨자: " + str(coffee))
print("-- 축하합니다 --")

#Teacher's Answer
users = range(1,21) #1부터 21직전까지=20까지 숫자를 생성
users = list(users)
random.shuffle(users)
winners = random.sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0:1]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")