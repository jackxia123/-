def solution(s):
  if s.isdigit():
    if(int(s)%2 == 0):
      return "even"
    else:
      return "odd"    
  else:
     return "not a digit"

  
