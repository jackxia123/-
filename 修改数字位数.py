def solution(number, width):
  res=''
  if(len(str(number))<width):
    res = str(number).zfill(width)
  else:
    res = str(number)[-width:]
    
  
  
  return res
    
print(solution(1234,5))
print(solution(1234,4))
    
