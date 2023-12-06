# list_question = [
#     "상품의 품질에 대해 어떻게 생각하시나요?",
#     "상품의 가격에 대해 어떻게 생각하시나요?",
#     "상품의 디자인에 대해 어떻게 생각하시나요?",
#     "상품에 대한 전반적인 만족도는 어떠신가요?"
# ]

# list_answer =  ["좋음", "중간", "좋아지길"]

# ---------------------------------------------------------
# 1. 상품의 품질에 대해 어떻게 생각하시나요? index : 0
# 1. 좋음     2. 중간     3. 좋아지길      index : 1
# ----------
# 2. 상품의 가격에 대해 어떻게 생각하시나요?    index : 2
# 1. 좋음     2. 중간     3. 좋아지길        index : 3
# ----------
# 3. 상품의 디자인에 대해 어떻게 생각하시나요?    index : 4
# 1. 좋음     2. 중간     3. 좋아지길           index : 5
# ----------
# 4. 상품에 대한 전반적인 만족도는 어떠신가요?    index : 6
# 1. 좋음     2. 중간     3. 좋아지길           index : 7 


list_question = ["상품의 품질에 대해 어떻게 생각하시나요?",
                "상품의 가격에 대해 어떻게 생각하시나요?",
                "상품의 디자인에 대해 어떻게 생각하시나요?",
                "상품에 대한 전반적인 만족도는 어떠신가요?"
    ]

list_answer =  ["좋음", "중간", "좋아지길"]


for num_question in range(len(list_question)) :
    print("{}. {}".format(num_question + 1, list_question[num_question]))
    for num_answer in range(len(list_answer)) :
        print("{}. {}".format(num_answer + 1, list_answer[num_answer]), end="  ")
    if num_question != 3 :
        print("")
        print("----------------")
    elif num_question == 3 :
        break


