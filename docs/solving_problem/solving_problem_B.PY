def match_point(correct_list, answer_list):
    result = []
    for i in range(len(correct_answers)):
        if correct_list[i] == answer_list[i]:
            result.append(sum)
        else:
            pass
      return result

def check_answers():
    correct_list = ["A", "B", "C", "D"]  # 정답 리스트를 정의합니다.
    answer_list = []  # 사용자의 입력 리스트를 초기화합니다.
    
    for i in range(1, 5):
        answer = answer_list[]
        answer_list.append(right)

    result = match_point(correct_list, answer_list)


def sum():
    num_sum = 0
    for sum, right in in question_grade():
        if right:
            num_sum += sum 
        return num_sum 
    

def grade():
    while True:
        call_sum = sum()
        my_grade = ''
        if sum >= 30:
            my_grade = 'A'
        elif sum > 20:
            my_grade = 'B'
        else:
            my_gread = 'F'
        return my_grade
str_grade = grade()
print("당신의 학점은 {}입니다.".format(str_grade))