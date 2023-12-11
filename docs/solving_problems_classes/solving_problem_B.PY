
class solving_problem_b: # 하위 function들을 내재한 solving_problem_b라는 클래스를 선언한다.
        
    def match_point(self, correct_list, answer_list, question_grade): #호출할 수 있도록 match_point라는 function을 정의한 뒤 클래스에 속해있다는 의미로 self라는 키워드를 부여한다.
    #맞은 문제에 대한 정답을 확인(정답의 값과 입력받은 정답의 값, 문항 별 점수의 값을 호출)하는 함수를 만든다.
        result = [] # 배점들의 값을 입력받을수 있는 result라는 리스트의 변수를 지정
        for i in range(len(correct_list)):
        # 문항 별 정답의 데이터의 길이(갯수)의 위치값을 호출하도록 지정후 index로서의 기능을 할 수 있도록 'i'라는 변수 지정(유효범위가 서로 다르기 때문에 별개로 작동)
            if correct_list[i] == answer_list[i]: # 정답의 위치와 입력받은 정답의 위치를 서로 매칭한다. 즉, 정답이 있을 경우를 true로 상정하고, 같은 결과가 없는 경우를 false라고 상정한다.
                result.append((question_grade[i],True)) 
        # 위에 부여된 문항 별 점수의 값을 result라는 변수에 입력한다. 그것은 원래 정답의 값(숫자의)이 문항의 보기와(문자의) 맞게 매칭되었다고 가정한 상황에서
        # 정답의 값의 위치값과 입력받은 정답의 값이 동일하다는 것을 확인하면, 동일한 위치값에 존재하는 문항(순서)의 배점과 매칭을 시킨 후 이것을 result에 적립하여 입력한다.
        return result # 적립된 배점들의 값을 반환한다.

    def check_answers(self): #호출할 수 있도록 check_answers라는 function을 정의한 뒤 클래스에 속해있다는 의미로 self라는 키워드를 부여한다.
        #입력한 답이 정답이 맞는지 확인한다.
        question_grade = [10,15,10,5]
        correct_list = [2,1,1,2]  
        answer_list = [2,1,1,4]     #확인용 임시 변수(list) 주석 처리
        result = self.match_point(correct_list, answer_list, question_grade)
        # 다른 function들의 호출을 위해 같은 클래스 안에 있을 function들에 부여된 self라는 값을 준 뒤 호출하도록한다.
        # 위의 '맞은 문제에 대한 정답을 확인한 함수'를 호출한 뒤 사용자가 입력한 값이 정답인지 아닌지를 판단하고 결과값을 result라는 변수에 부여
        # 다만 이 result 튜플로 이루어져 있으며 서로가 매칭이 되어 정답이라면(true라면) 해당하는 배점을, 아닌 경우는 0점을 반환하여 적립하고 그것이 적립된 변수이다
        # 이렇게 적립된 result는 바로 아래 calculate_score로 보내져서 점수의 계산을 하는 곳에서 인용된다.
        sum = self.calculate_score(result) 
        # 위와 같이 호출할 수 있도록 check_answers라는 function을 정의한 뒤 클래스에 속해있다는 의미로 self라는 키워드를 부여한다.4
        # 바로 위의 '맞은 문제의 배점을 합산한 값'을 호출하여 아래 문단의 맞은 점수에 대한 합산(연산) 함수와 그 함수의 반환값을 호출
        str_grade = self.grade(sum) # 최하단의 점수에 해당하는 학점을 산출한 함수와 그 반환값을 호출하여 변수로 지정
        print("당신의 점수는 {}점 입니다.".format(sum)) # 반환된 점수를 대입시켜 점수와 관련된 문구 출력
        print("당신의 학점은 {}입니다.".format(str_grade)) # 반환된 학점 값을 대입시켜 학점과 관련된 문구 출력

    def calculate_score(self, data): #점수 계산을 하는 함수에서(함수가 호출될 때 전달받을 data라는 매개변수 지정)
        # data는 윗 문단의 구문인 result=match_point의 기능을 받아들여 그 기능을 할 변수로 작동을 한다.
        sum = 0 # 합계를 구할 변수의 초기 값을 0으로 지정
        for points, is_correct in data: #상술한 result의 값을 각각 할당하여 반복
            if is_correct: # 정답인지 아닌지 판단하며 참일 경우 아래 구문을 수행하도록 한다.
                sum += points #정답이 맞는 경우 해당 배점을 기존의 정답의 배점값에 적립하여 더함
        return sum # 계산한 결과값 반환
        
    def grade(self, sum):  # 계산된 총 합산 점수를 기반으로 학점을 계산
        my_grade = '' #학점 = ? (' '은 빈 '문자열'로 초기화 = if구문에서 연산을 한 뒤 해당되는 반환값을 받기 위한 준비)
        # 데이터값의 빈 공간은 재사용성을 높여준다.
        if sum >= 30:             # 점수의 합계가 30점 이상인지 확인
            my_grade = 'A'
        elif sum > 20:            # 점수의 합계가 20점을 초과하는 지 확인
            my_grade = 'B'
        else:                     # 윗 구문에 해당되는 영역의 점수가 아닌지 확인
            my_grade = 'F'        
        return my_grade # check_answer()함수에 인용할 

solving = solving_problem_b()
solving.check_answers()
