def solution(a, b):
  for row in range(len(a)):
    for index in range(len(a)):
      a[row][index] +=b[row][index]
  return a
  
print(solution([[1,2],[1,2]],[[2,3],[2,3]]))
