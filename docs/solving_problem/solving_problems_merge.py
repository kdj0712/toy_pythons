def match_point(correct_list, answer_list, question_grade):
    result = []
    for i in range(len(correct_list)):
        if correct_list[i] == answer_list[i]:
            result.append((question_grade[i],True))
    return result


def check_answers():
    # question_grade = [10,15,10,5]
    # correct_list = [2,1,1,2]  
    # answer_list = [2,1,1,4]     #확인용 임시 변수 삭제
    result = match_point(correct_list, answer_list, question_grade)
    sum, right = calculate_score(result)
    str_grade = grade(sum)
    print("당신의 점수는 {}점 입니다.".format(sum))
    print("당신의 학점은 {}입니다.".format(str_grade))


def calculate_score(data):
    sum = 0
    right = 0
    for points, is_correct in data:
        if is_correct:
            sum += points
            right += 1
    return sum, right
    

def grade(sum):
    my_grade = ''
    if sum >= 30:
        my_grade = 'A'
    elif sum > 20:
        my_grade = 'B'
    else:
        my_grade = 'F'
    return my_grade

check_answers()