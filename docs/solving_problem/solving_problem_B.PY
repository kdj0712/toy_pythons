def match_point(correct_list, answer_list, question_grade):
    result = []
    for i in range(len(correct_list)):
        if correct_list[i] == answer_list[i]:
            result.append(question_grade[i],True)
        else:
            pass
      return result

def check_answers():
    question_grade = []
    correct_list = []  # 정답 리스트를 정의합니다.
    answer_list = []  # 사용자의 입력 리스트를 초기화합니다.
    result = match_point(correct_list, answer_list, question_grade)
    sum, right = calculrate_score(result)


def calculate_score(data):
    sum = 0
    right = 0
    for points, is_correct in in data:
        if is_correct:
            sum += points
            right += 1
        return sum, right
    

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