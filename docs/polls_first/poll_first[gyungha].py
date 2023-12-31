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
    print("{} .{}".format(num_question + 1, list_question[num_question])) 
    for num_answer in range(len(list_answer)) :  
        print("{}. {}".format(num_answer + 1, list_answer[num_answer]), end="  ")
    if num_question != 3 :
        print("")
        print("----------------")
    elif num_question == 3 :
        break


# 이 부분은 'list_question'이라는 리스트의 길이만큼 반복을 할 것이라는 뜻 /# 'len' 함수는 리스트의 길이를 반환하고, 'range' 함수는 0부터 인자로 받은 숫자 - 1 까지의 일련의 정수를 반환 /  #따라서 이 코드는 'list_question'의 모든 요소에 대하여 반복을 수행

#  이 코드는 'list_question'의 각 요소를 순서대로 화면에 출력하며, 각 요소 앞에는 1부터 시작하는 숫자가 붙습니다
# list_question[num_question] => list_question의 첫번째 ,두번 째 ...

# 반복문으로, 'list_answer'라는 리스트의 길이만큼 반복을 할 것이라는 뜻. 이 코드는 'list_answer'의 모든 요소에 대하여 반복을 수행

#  이 코드는 'list_answer'의 각 요소를 순서대로 화면에 출력하며, 각 요소 앞에는 1부터 시작하는 숫자가 붙습니다. 'end="  "'은 print 함수가 끝나고 나서 줄바꿈이 아닌 두 번의 공백("  ")을 출력하라는 의미

# 따라서, 이 코드는 'list_question'의 각 요소에 대해 'list_answer'의 모든 요소를 순서대로 번호와 함께 출력/ 이는 일종의 중첩된 반복 구조를 형성하며, 이러한 구조는 특정 작업을 여러 번 반복해야 할 때 유용
