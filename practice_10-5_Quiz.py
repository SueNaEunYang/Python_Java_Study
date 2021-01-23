# chicken = 10
# waiting = 1
# while(Ture):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#     if order > chicken:
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#         waiting += 1
#         chicken -= order

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리, 출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정. 치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료, 출력메세지: "재고가 소진되어 더 이상 주문을 받지 않습니다."



# Sue's answer
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try: 
    chicken = 10
    waiting = 1
    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError("") #...?
except ValueError:
   print("잘못된 값을 입력하였습니다.")
except SoldOutError as err:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    #break를 빼먹었음



# Teacher's answer
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break