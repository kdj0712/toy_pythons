# source from ../polls_first/polls_first[deokjaekim].py

# list_question = [
#     "상품의 품질에 대해 어떻게 생각하시나요?",
#     "상품의 가격에 대해 어떻게 생각하시나요?",
#     "상품의 디자인에 대해 어떻게 생각하시나요?",
#     "상품에 대한 전반적인 만족도는 어떠신가요?"
# ]

# list_answer =  ["좋음", "중간", "좋아지길"]

#("------------------------------------------------------------")

# 1. 상품의 품질에 대해 어떻게 생각하시나요?
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 3
# ----------
# 2. 상품의 가격에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 2
# ----------
# 3. 상품의 디자인에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 3
# ----------
# 4. 상품에 대한 전반적인 만족도는 어떠신가요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 1

# —--- 통 계 ----
# 설문자 답항별 갯수 표시 : [1, 1, 2]
# 답항 가중 평균 : 답변별 가중치 순서 (좋음:3, 중간:2, 좋아지길:1)
# (1*3 + 1*2 +2*1) / (3+2+1) = 0.86


list_question = ["상품의 품질에 대해 어떻게 생각하시나요?",
                "상품의 가격에 대해 어떻게 생각하시나요?",
                "상품의 디자인에 대해 어떻게 생각하시나요?",
                "상품에 대한 전반적인 만족도는 어떠신가요?"
    ]

list_answer =  ["좋음", "중간", "좋아지길"]

## 덕재님 코드
question_index = 0 #question_index라는 변수에 index의 값을 지정
for question in list_question: #question 변수에 list_question에 있는 모든 값을 할당
    question_index += 1 #question_index 변수에 1을 선언하고 반복될 때마다 1씩 증가하도록 선언
    print("{}. {}".format(question_index, question)) 
#question_index로 선언된 변수의 값이 최초 출력되고, . 을 1회 출력한 후 이어서 question 변수에 있는 값을 출력하도록 선언
    answer_index = 0 #answer_index 변수에 index의 값을 지정
    for answer in list_answer: #answer 변수에 list_answer에 입력되어 있는 모든 값을 할당
        answer_index += 1 #answer_index 변수에 1을 선언하고 반복될 때마다 1씩 증가되도록 선언
        print("{}. {}".format(answer_index, answer), end='     ')
# answer_index로 선언된 변수의 값이 최초 출력되고, . 을 1회 출력한 후 이어서 answer 변수에 있는 값을 출력하도록 선언,
# 다만 같은 줄에서 줄바꿈이 없이 이어서 출력될 수 있도록 end=r과 그 그값에 공백을 주는 구문을 이용하여 선언
# 공백을 주는 넓이를 통해 간격을 조정할 수 있다.
    print()    # 완료된 구문 이후 줄을 바꿀 수 있도록 함수를 선언
    if question_index < 4: # if 함수의 조건을 question_index로 선언한 변수의 값이 4 미만일 경우로 지정
        print("------------------")
# for 구문이 반복되는 상황 속에서 if 함수를 선언할 때 제시한 조건인 question_index의 값이 4 미만인 경우 출력을 하는 값을 선언.
    else: #if함수의 조건인 question_index의 값이 4 미만이 아닌 경우 코드 블록을 건너뛰다는 것을 의미
        pass #if 함수의 조건이 충족하지 못한 경우 동작하지 않도록 pass를 선언





## 경하 코드
list_statistics = [0,0,0]
for num_question in range(len(list_question)) :           
    print("{} .{}".format(num_question + 1, list_question[num_question])) 
    for num_answer in range(len(list_answer)) :  
        print("{}. {}".format(num_answer + 1, list_answer[num_answer]), end="  ")

    print("")
    str_question_result = input("당신 생각은 몇번 : ")
    num_question_result = int(str_question_result)
    index = num_question_result - 1
    list_statistics[index] = list_statistics[index] + 1 


    if num_question != 3 :
        print("")
        print("----------------")
    elif num_question == 3 :
        break
print("--------통계--------")
print("설문자 답항별 갯수 표시 : {}".format(list_statistics))
print("답변별 가중치: (좋음 : 3, 중간 : 2, 좋아지길 : 1)")
num_average = (list_statistics[0]*3 + list_statistics[1]*2 + list_statistics[2]*1) / (list_statistics[0] +list_statistics[1] +list_statistics[2] )
print("답항 가중 평균 : ({}*3 + {}*2 + {}*1) / ({} + {} + {}) = {}".format(list_statistics[0], list_statistics[1], list_statistics[2],list_statistics[0],list_statistics[1], list_statistics[2], num_average))
    


