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


    # if num_question != 3 :
    #     print("")
    #     print("----------------")
    # elif num_question == 3 :
    #     break
print("--------통계--------")
print("설문자 답항별 갯수 표시 : {}".format(list_statistics))
print("답변별 가중치: (좋음 : 3, 중간 : 2, 좋아지길 : 1)")
num_average = (list_statistics[0]*3 + list_statistics[1]*2 + list_statistics[2]*1) / (list_statistics[0] +list_statistics[1] +list_statistics[2] )
print("답항 가중 평균 : ({}*3 + {}*2 + {}*1) / ({} + {} + {}) = {}".format(list_statistics[0], list_statistics[1], list_statistics[2],list_statistics[0],list_statistics[1], list_statistics[2], num_average))
    


