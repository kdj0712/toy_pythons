1. 문제 출력과 정답 입력
2. 항목별 점수를 난이도를 반영하여 학점으로 산출 / 산출한 결과를 화면으로 출력
3. 폴더/파일 이름: solving_problem(폴더 및 통합파일명) 
4. 문제별 배점 리스트 : question_grade
5. 입력받은 정답 리스트 : answer_list
6. 실제 문제 정답  : correct_list
7. A : 김경하 (solving_problem_A)
8. B : 김덕재 (solving_problem_B)

A : 문제 풀기 => 처음부터 input이 아닌 상수로 받고 index 값으로 뽑아내기
                input_temp=[]라는 테스트 input을 먼저 사용하기 



B : 통계 내기 => 1. 실제 정답 리스트(제공) 2. 입력 리스트(사용자에 대한 list_test=[]를 먼저 만들고 확인한 후 점수화) 3. 점수 리스트  -> 이걸 토대로 합계

통합해서는 사용자 입력(input)

A가 결국에는 입력 리스트를 뽑아내서 B에게 넘겨주고 B가 그걸 토대로 합계 

funtion으로 두개 만든 후에 마지막에 return 두 줄로 통합 