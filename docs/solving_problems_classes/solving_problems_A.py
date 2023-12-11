list_question = ["1. 문제: Python에서 변수를 선언하는 방법은?", 
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요?", 
                 "3. 문제: Python에서 조건문을 작성하는 방법은?", 
                 "4. 문제: Python에서 함수를 정의하는 방법은?"]
           
list_option = ["1) var name, 2) name = value, 3) set name, 4) name == value", 
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다", 
               "1) if-else, 2) for-in, 3) while, 4) def", "1) class, 2) def, 3) import, 4) return"]

        

class Quiz:
    def __init__(self, list_question, list_option): # 변수 선언하는 곳
        self.list_question = list_question
        self.list_option = list_option
        self.correct_list = [2,1,1,2] 
        self.question_grade = [10,15,10,5]
        self.answer_list = []

    def print_question(self):
        for i in range(len(list_question)) :
            print("{}".format(list_question[i]))
            print("{}".format(list_option[i]))
            get_num = int(input("정답 : "))
            self.answer_list.append(get_num)
            
           
        print("입력하신 문항 별 정답 번호 : {}".format(self.answer_list))
        return self.answer_list 

quiz = Quiz(list_question, list_option)
quiz.print_question()


