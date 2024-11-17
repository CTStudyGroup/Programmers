def solution(N, number):
    if N == number:
        return 1

    # set 배열 초기화
    s = [set() for x in range(8)]

    # set마다 숫자 설정
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # set[i]: N을 i개 사용해 만든 숫자들의 집합

    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer
