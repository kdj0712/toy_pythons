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
# 입력받은 데이터의 횟수를 카운팅하기 위한 임의의 리스트를 작성하고 해당 값을 각 0회라고 선언하며 이는 0번째 0회, 1번쨰 0회, 2번째 0회이다.
for num_question in range(len(list_question)) :           
    print("{} .{}".format(num_question + 1, list_question[num_question])) 
    for num_answer in range(len(list_answer)) :  
        print("{}. {}".format(num_answer + 1, list_answer[num_answer]), end=" ")
    print("")
    num_qa = int(input("당신의 생각은 몇 번 인가요? : ")) # 입력받은 데이터를 숫자형 타입으로 변경하는 것을 num_qa로 선언한다.
    index_num_qa = num_qa - 1
    # num_qa로 입력받은 값의 숫자는 list_qa에 선언된 값의 순서와 맞지 않으므로, 이를 매칭하기 위해 -1을 해 준뒤 index_num_qa라는 변수로 선언한다.
    list_qa[index_num_qa] = list_qa[index_num_qa] + 1
    # 입력받은 데이터값인 index_num_qa를 list_qa에 삽입한다. 이 때 list_qa의 데이터 위치상의 순서와 맞는 해당 데이터의 값을 1을 증가시키는 역할을 한다.
  
    if num_question != 3 :     #위와 동일
        print()             
        print("----------------")
    elif num_question == 3 :
        pass

# 입력받은 값에 대한 횟수를 파악한 후 각 항목별 가중치를 부가하여 평균을 계산한 후 이를 출력한다.
for num_qa in list_qa:           # 입력받은 값을 항목별 데이터의 입력받은 횟수로 반복적으로 계산하도록 명령
    molecule = (list_qa[0]*3)+(list_qa[1]*2)+(list_qa[2]*1) # 입력받는 값을 이용하여 평균값을 계산할 때 분자를 계산하는 방식, 이를 molecule이라는 변수로 선언
    denominator = (list_qa[0]+list_qa[1]+list_qa[2])        # 입력받는 값을 이용하여 평균값을 계산할 때 분자를 계산하는 방식, 이를 denominator라는 변수로 선언
    result = molecule/denominator  # 각각 산출된 분자와 분모를 연산하여, 그 결과값을 result라는 변수로 선언한다.
    pass
print("1.좋음 {}회, 2.중간 {}회, 3.좋아지길 {}회".format(list_qa[0],list_qa[1],list_qa[2])) # 입력한 값의 횟수를 출력하도록 지정한 list_qa의 데이터값의 위치를 지정한다.
print("답항 가중 평균 = {}".format(result)) # result로 계산한 값을 출력한다.