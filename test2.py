def solution(survey, choices):
    #성격 유형을 저장하는 변수
    mbti = ''
    
    #각 캐릭터의 점수를 저장하는 딕셔너리
    answer = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0,}
    
    #캐릭터와 응답을 반복문으로 꺼내어 응답에 따라 캐릭터에 점수를 저장
    for s,c in zip(survey, choices) :
        #점수가 4보다 낮으면 앞 캐릭터에 점수 저장
        if c < 4 :
            answer[s][0] = answer[s][0] + (4 - c%4)
            
        elif c > 4 :
            answer[s[1]] = answer[s[1]] + (c-4)
            
    #각 캐릭터의 유형을 저장하는 리스트 생성
    first = ['R','C','J','A']
    second = ['T','F','M','N']
    
    # 캐릭터의 점수를 비교하여 성격 유형에 알맞는 캐릭터를 저장
    for f,s in zip(first, second) :
        if answer[f] < answer[s] :
            mbti += s
        elif answer[f] >= answer[s] :
            mbti += f
    return mbti
