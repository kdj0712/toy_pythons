list_question = ["1. 문제: Python에서 변수를 선언하는 방법은?", 
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요?", 
                 "3. 문제: Python에서 조건문을 작성하는 방법은?", 
                 "4. 문제: Python에서 함수를 정의하는 방법은?"]  # 문항 별 배점 항목을 별도의 list를 생성한 뒤 따로 호출

list_option = ["1) var name, 2) name = value, 3) set name, 4) name == value", 
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다", 
               "1) if-else, 2) for-in, 3) while, 4) def", "1) class, 2) def, 3) import, 4) return"]

correct_list = [2,1,1,2]  # 원래 각 문항 별 정답의 리스트를 추가
question_grade = [10,15,10,5] # 각 문항별 배점의 현황을 별도의 list를 생성하여 기재
answer_list = [0,0,0,0]  #입력받은 정답 리스트 


for i in range(len(list_question)) :
    print("{} 점수 : {} 점".format(list_question[i],question_grade[i])) #문제 출력 시 배점이 몇 점 인지를 .format함수를 이용해 question_grade리스트에서 호출
    print("{}".format(list_option[i]))
    get_num = int(input("정답 : "))
    answer_list[i] = get_num
    pass
print("{}".format(answer_list)) 


def match_point(correct_list, answer_list, question_grade):  #맞은 문제에 대한 정답 확인
    result = []
    for i in range(len(correct_list)):
        if correct_list[i] == answer_list[i]:
            result.append((question_grade[i],True))
    return result


def check_answers():
    # question_grade = [10,15,10,5]
    # correct_list = [2,1,1,2]  
    # answer_list = [2,1,1,4]     #확인용 임시 변수(list) 삭제
    result = match_point(correct_list, answer_list, question_grade)
    sum, right = calculate_score(result)
    str_grade = grade(sum)
    print("당신의 점수는 {}점 입니다.".format(sum))
    print("당신의 학점은 {}입니다.".format(str_grade))


def calculate_score(data): #점수 계산
    sum = 0 
    right = 0
    for points, is_correct in data: 
        if is_correct:
            sum += points
            right += 1
    return sum, right
    

def grade(sum):  #학점 계산
    my_grade = '' #학점 = ?
    if sum >= 30:             # 점수의 합계가 30점 이상인지 확인
        my_grade = 'A'
    elif sum > 20:            # 점수의 합계가 20점을 초과하는 지 확인
        my_grade = 'B'
    else:                     # 둘 다 해당되는 점수가 아니라면
        my_grade = 'F'        
    return my_grade

check_answers()