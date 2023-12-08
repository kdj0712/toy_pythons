list_question = ["1. 문제: Python에서 변수를 선언하는 방법은?", 
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요?", 
                 "3. 문제: Python에서 조건문을 작성하는 방법은?", 
                 "4. 문제: Python에서 함수를 정의하는 방법은?"]
                # 문항 별 배점 항목을 별도의 list를 생성한 뒤 따로 호출하도록 지정후, 각 문항만 list에 저장될 수 있도록 일부 수정

list_option = ["1) var name, 2) name = value, 3) set name, 4) name == value", 
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다", 
               "1) if-else, 2) for-in, 3) while, 4) def", "1) class, 2) def, 3) import, 4) return"] # 각 문항에 부여된 보기를 별도 list를 생성한 뒤 따로 호출

correct_list = [2,1,1,2]        # 원래 각 문항 별 정답의 리스트를 추가(다만 이것은 list_option을 1대1로 매칭한 것이 아닌 실제 정답의 값만 부여한다.)
question_grade = [10,15,10,5]   # 각 문항별 배점의 현황을 별도의 list를 생성하여 기재
answer_list = [0,0,0,0]         # 입력받은 정답의 값을 부여받을 수 있는 리스트 


for i in range(len(list_question)) :    # 각 문항이 입력된 list_question의 입력받은 값의 갯수를 파악하도록 length로 지정을 해 준 뒤
                                        # 문항의 위치값인 index로서의 기능을 i에 부여한다. 이는 for 구문 안에서 list_question에 부여된 데이터값의 길이(즉, 갯수) 만큼 반복적으로 동작한다.
    print("{} 점수 : {} 점".format(list_question[i],question_grade[i])) #문제 출력 시 배점이 몇 점 인지를 .format함수를 이용해 question_grade리스트에서 호출
    print("{}".format(list_option[i]))    # 문항에 부여된 보기를 for 구문의 부여된 질문의 위치값과 동일한 위치를 매칭시키는 역할을 하기 위한 'i' 라는 변수를 부여하여 호출
    # i 는 for 구문에 의하여 질문의 개수만큼 반복적으로 호출이 된다. 그리고 이 구문의 i는 scope(유효 범위)안에서 동작한다.
    # 그러므로 이번의 for 구문에 있는 'i'와 후반부에 존재하는 'i'는 별도로 기능하는 것이 가능한 독립적 변수이다.
    get_num = int(input("정답 : "))       # get_num이라는 변수에 입력받은 정답을 숫자형 데이터로 변환하여 저장한다.
    answer_list[i] = get_num            # 입력받은 정답은 answer_list에 list_question과 동일한 위치값에 그 값이 부여된다.
    pass                                # 다만 'answer_list.append(get_num)'이라는 안전한 데이터 부여 방식이 존재한다고 한다.
print("입력하신 문항 별 정답 번호 : {}".format(answer_list))         # 반복되는 동작인 질문과 보기 출력 및 정답의 입력이 완료되면, 사용자가 입력한 정답이 출력된다. *안내를 위한 문구 추가 삽입*

print("정답 공개 : {}".format(correct_list)) # 문항 별 정답을 공개하도록 추가



def match_point(correct_list, answer_list, question_grade):
#맞은 문제에 대한 정답을 확인(정답의 값과 입력받은 정답의 값, 문항 별 점수의 값을 호출)하는 함수를 만든다.
    result = [] # 배점들의 값을 입력받을수 있는 result라는 리스트의 변수를 지정
    for i in range(len(correct_list)):
    # 문항 별 정답의 데이터의 길이(갯수)의 위치값을 호출하도록 지정후 index로서의 기능을 할 수 있도록 'i'라는 변수 지정(유효범위가 서로 다르기 때문에 별개로 작동)
        if correct_list[i] == answer_list[i]: # 정답의 위치와 입력받은 정답의 위치를 서로 매칭한다. 즉, 정답이 있을 경우를 true로 상정하고, 같은 결과가 없는 경우를 false라고 상정한다.
            result.append((question_grade[i],True)) 
    # 위에 부여된 문항 별 점수의 값을 result라는 변수에 입력한다. 그것은 원래 정답의 값(숫자의)이 문항의 보기와(문자의) 맞게 매칭되었다고 가정한 상황에서
    # 정답의 값의 위치값과 입력받은 정답의 값이 동일하다는 것을 확인하면, 동일한 위치값에 존재하는 문항(순서)의 배점과 매칭을 시킨 후 이것을 result에 적립하여 입력한다.
    return result # 적립된 배점들의 값을 반환한다.


def check_answers(): #(입력한 답이 정답이 맞는지 확인한다.)
    # question_grade = [10,15,10,5]
    # correct_list = [2,1,1,2]  
    # answer_list = [2,1,1,4]     #확인용 임시 변수(list) 삭제
    result = match_point(correct_list, answer_list, question_grade)
    # 위의 '맞은 문제에 대한 정답을 확인한 함수'를 호출한 뒤 사용자가 입력한 값이 정답인지 아닌지를 판단하고 결과값을 result라는 변수에 부여
    # 다만 이 result 튜플로 이루어져 있으며 서로가 매칭이 되어 정답이라면(true라면) 해당하는 배점을, 아닌 경우는 0점을 반환하여 적립하고 그것이 적립된 변수이다
    # 이렇게 적립된 result는 바로 아래 calculate_score로 보내져서 점수의 계산을 하는 곳에
    sum = calculate_score(result) #, right(기능을 하지 않으므로 하단에 있는 점수 계산의 반환값에 부여된 것을 변경하여 삭제)
    # 바로 위의 '맞은 문제의 배점을 합산한 값'을 호출하여 아래 문단의 맞은 점수에 대한 합산(연산) 함수와 그 함수의 반환값을 호출
    str_grade = grade(sum) # 최하단의 점수에 해당하는 학점을 산출한 함수와 그 반환값을 호출하여 변수로 지정
    print("당신의 점수는 {}점 입니다.".format(sum)) # 반환된 점수를 대입시켜 점수와 관련된 문구 출력
    print("당신의 학점은 {}입니다.".format(str_grade)) # 반환된 학점 값을 대입시켜 학점과 관련된 문구 출력


def calculate_score(data): #점수 계산을 하는 함수에서(함수가 호출될 때 전달받을 data라는 매개변수 지정)
    # data는 윗 문단의 구문인 result=match_point의 기능을 받아들여 그 기능을 할 변수로 작동을 한다.
    sum = 0 # 합계를 구할 변수의 초기 값을 0으로 지정
    # right = 0
#(처음에는 맞은 개수에 맞춰 적립이 되도록 기능해야 하는 것인가 생각하였으나, 위에서도 작동하지 않고 계산에 지장이 없는 듯 하여 삭제)
    for points, is_correct in data: #상술한 result의 값을 각각 할당하여 반복
        if is_correct: # 정답인지 아닌지 판단하며 참일 경우 아래 구문을 수행하도록 한다.
            sum += points #정답이 맞는 경우 해당 배점을 기존의 정답의 배점값에 적립하여 더함
            # right += 1 상술하다시피 기능하지 않으므로 제외
    return sum # 계산한 결과값 반환       (, right    상 동)
    

def grade(sum):  # 계산된 총 합산 점수를 기반으로 학점을 계산
    my_grade = '' #학점 = ? (' '은 빈 '문자열'로 초기화 = if구문에서 연산을 한 뒤 해당되는 반환값을 받기 위한 준비)
    # 데이터값의 빈 공간은 재사용성을 높여준다.
    if sum >= 30:             # 점수의 합계가 30점 이상인지 확인
        my_grade = 'A'
    elif sum > 20:            # 점수의 합계가 20점을 초과하는 지 확인
        my_grade = 'B'
    else:                     # 윗 구문에 해당되는 영역의 점수가 아닌지 확인
        my_grade = 'F'        
    return my_grade # check_answer()함수에 인용할 

check_answers()