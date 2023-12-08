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

answer_list = [0,0,0,0]  #입력받은 정답 리스트 

for i in range(len(list_question)) :
    print("{}".format(list_question[i]))
    print("{}".format(list_option[i]))
    get_num = int(input("정답 : "))
    answer_list[i] = get_num
    pass
print("{}".format(answer_list)) 
    


# for 루프를 사용하여 list_question의 각 요소를 출력
# for i in range(len(list_question)) : => list_question의 길이만큼 반복(range는 정수만 인자로 받기 때문에 length를 사용하여 list의 내용이 아닌 list의 길이(개수)만큼 i로 할당하여 반복을 걸어줌)
# i는 반복 회차를 나타내는 인덱스
# print("{}".format(list_question[i])) => list_question를 순차적으로 출력이 되야하므로 list_question에 i라는 인덱스를 걸어준다
# 다음으로 list_option이 순차적으로 출력이 되야하므로 list_option에 i라는 인덱스를 걸어준다
# 다음으로 사용자가 정답을 입력할 수 있게 input을 넣어주되 정수로 받아야 하므로 int(input())이라고 해준다
# 사용자가 입력한 정답을 가지고 통계를 내야하므로 그 정답을 모아둔 리스트를 만들어야 한다 
# answer_list = [0,0,0,0] => []안에 아무것도 넣지 않으면 get_num의 element와 같다라는 코드를 넣을 수 없으므로 숫자'0'이라는 element를 임의로 지정해준다
# [0,0,0,0] = [1번의 답, 2번의 답, 3번의 답, 4번의 답] 
# answer_list[i] = get_num => answer_list에 정답이 순차적으로 들어가야 하므로 i라는 인덱스를 지정해주고 answer_list[i]가 get_num과 같다라고 해준다.







