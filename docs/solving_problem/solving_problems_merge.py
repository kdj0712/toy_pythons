list_question = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)", 
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)", 
                 "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)", 
                 "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"]

list_option = ["1) var name, 2) name = value, 3) set name, 4) name == value", 
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다", 
               "1) if-else, 2) for-in, 3) while, 4) def", "1) class, 2) def, 3) import, 4) return"]

answer_list = [0,0,0,0]  #입력받은 정답 리스트 

for i in range(len(list_question)) :
    print("{}".format(list_question[i]))
    print("{}".format(list_option[i]))
    get_num = int(input("정답 : "))
    answer_list[i] = get_num
    pass
print("{}".format(answer_list)) 
def match_point(correct_list, answer_list, question_grade):
    result = []
    for i in range(len(correct_list)):
        if correct_list[i] == answer_list[i]:
            result.append((question_grade[i],True))
    return result


def check_answers():
    question_grade = [10,15,10,5]
    correct_list = [2,1,1,2]  
    answer_list = [2,1,1,4]  
    result = match_point(correct_list, answer_list, question_grade)
    sum, right = calculate_score(result)
    str_grade = grade(sum)
    print("당신의 점수는 {}점 입니다.".format(sum))
    print("당신의 학점은 {}입니다.".format(str_grade))


def calculate_score(data):
    sum = 0
    right = 0
    for points, is_correct in data:
        if is_correct:
            sum += points
            right += 1
    return sum, right
    

def grade(sum):
    my_grade = ''
    if sum >= 30:
        my_grade = 'A'
    elif sum > 20:
        my_grade = 'B'
    else:
        my_grade = 'F'
    return my_grade

check_answers()
