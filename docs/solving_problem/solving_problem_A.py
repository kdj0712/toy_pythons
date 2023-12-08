# 아래는 4개의 Python 관련 문제와 각 문항의 난이도에 따른 점수화

# 1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)
#    1) var name, 2) name = value, 3) set name, 4) name == value
#    - 정답: 2

# 2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)
#    1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다
#    - 정답: 1

# 3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)
#    1) if-else, 2) for-in, 3) while, 4) def
#    - 정답: 1

# 4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)
#    1) class, 2) def, 3) import, 4) return
#    - 정답: 2

# 4. 문제별 배점 리스트 : question_grade
# 5. 입력받은 정답 리스트 : answer_list
# 6. 실제 문제 정답  : list_correct

# 출제 문제
list_question = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)", 
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)", 
                 "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)", 
                 "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"]

list_option = ["1) var name, 2) name = value, 3) set name, 4) name == value", 
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다", 
               "1) if-else, 2) for-in, 3) while, 4) def", "1) class, 2) def, 3) import, 4) return"]

answer_list = [0,0,0,0]

for i in range(len(list_question)) :
    print("{}".format(list_question[i]))
    print("{}".format(list_option[i]))
    get_num = int(input("정답 : "))
    answer_list[i] = get_num
    pass
    



