def solution(legs):
  return list(range(legs // 2 % 2,legs // 2 + 1,2))
  
print(solution(16))
