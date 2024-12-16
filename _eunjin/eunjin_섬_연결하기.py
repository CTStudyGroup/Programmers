def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    edge = set([costs[0][0]])

    while len(edge) != n:
        for v in costs:
            if v[0] in edge and v[1] in edge:
                continue
            if v[0] in edge or v[1] in edge:
                edge.update([v[0], v[1]])
                answer += v[2]
                break

    return answer
