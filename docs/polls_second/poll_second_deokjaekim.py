# source from ../polls_first/polls_first[gyungha].py

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


# for num_question in range(len(list_question)) :           
#     print("{} .{}".format(num_question + 1, list_question[num_question])) 
#     for num_answer in range(len(list_answer)) :  
#         print("{}. {}".format(num_answer + 1, list_answer[num_answer]), end="  ")
#     if num_question != 3 :
#         print("")
#         print("----------------")
#     elif num_question == 3 :
#         break


# 이 부분은 'list_question'이라는 리스트의 길이만큼 반복을 할 것이라는 뜻 /# 'len' 함수는 리스트의 길이를 반환하고, 'range' 함수는 0부터 인자로 받은 숫자 - 1 까지의 일련의 정수를 반환 /  #따라서 이 코드는 'list_question'의 모든 요소에 대하여 반복을 수행

 # 반복문으로, 'list_answer'라는 리스트의 길이만큼 반복을 할 것이라는 뜻. 이 코드는 'list_answer'의 모든 요소에 대하여 반복을 수행

#  이 코드는 'list_answer'의 각 요소를 순서대로 화면에 출력하며, 각 요소 앞에는 1부터 시작하는 숫자가 붙습니다. 'end="  "'은 print 함수가 끝나고 나서 줄바꿈이 아닌 두 번의 공백("  ")을 출력하라는 의미입니다.

# 따라서, 이 코드는 'list_question'의 각 요소에 대해 'list_answer'의 모든 요소를 순서대로 번호와 함께 출력하게 됩니다. 이는 일종의 중첩된 반복 구조를 형성하며, 이러한 구조는 특정 작업을 여러 번 반복해야 할 때 유용합니다.

# 위 조건을 활용하여 아래와 같은 결과가 출력되도록 구문을 작성한다.

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

# 답변별 가중치 (좋음:3, 중간:2, 좋아지길:1)
# 답항 가중 평균 : 
# (1*3 + 1*2 +2*1) / (3+2+1) = 0.86
list_qa = [0,0,0]
for num_question in range(len(list_question)) :           
    print("{} .{}".format(num_question + 1, list_question[num_question])) 
    for num_answer in range(len(list_answer)) :  
        print("{}. {}".format(num_answer + 1, list_answer[num_answer]), end=" ")
    print("")
    num_qa = int(input("당신의 생각은 몇 번 인가요? : "))
    index_num_qa = num_qa - 1
    list_qa[index_num_qa] = list_qa[index_num_qa] + 1
  
    if num_question != 3 :
        print()
        print("----------------")
    elif num_question == 3 :
        pass
# 입력받은 값에 대한 횟수를 파악한 후 각 항목별 가중치를 부가하여 평균을 계산한 후 이를 출력한다.
for num_qa in list_qa:
    molecule = (list_qa[0]*3)+(list_qa[1]*2)+(list_qa[2]*1)
    denominator = (list_qa[0]+list_qa[1]+list_qa[2])
    result = molecule/denominator
    # print("1.좋음 {}회, 2.중간 {}회, 3.좋아지길 {}회".format(list_qa[0],list_qa[1],list_qa[2]))
    # result = (list_qa[0]*3)+(list_qa[1]*2)+(list_qa[2]*1)/(list_qa[0]+list_qa[1]+list_qa[2])
    # print("답항 가중 평균 = {}".format(result))
    pass
print("1.좋음 {}회, 2.중간 {}회, 3.좋아지길 {}회".format(list_qa[0],list_qa[1],list_qa[2]))
print("답항 가중 평균 = {}".format(result))
    
