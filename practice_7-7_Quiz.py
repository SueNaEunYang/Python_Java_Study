#Sue's Answer

gender = str(input("성별은? 남자/여자 중 선택하여 입력"))
height = int(input("키는? 000cm에서 숫자만 입력"))

def std_weight(gender, height):
    if gender == "남자":
        return height/100 * height/100 * 22
    elif gender == "여자":
        return height/100 * height/100 * 21

stdweight = std_weight(gender, height) #여기서 round( ,2)를 해야한다!!
print("키 {0}cm {1}의 표준 체중은 {2} kg 입니다.".format(height, gender, stdweight))

#Teacher's Answer
def std_weight2(height2, gender2):
    if gender2 == "남자":
        return height2 * height2 * 22
    else :
        return height2 * height2 * 21

height2 = 175
gender2 = "남자"
weight2 = round(std_weight2(height2 /100 , gender2), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height2, gender2, weight2))