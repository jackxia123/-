def solution(min1, min2_10, min11, s):
  numMinutes=0
  if s >= min1:
    s -=min1
    numMinutes += 1
  while s >=min2_10 and numMinutes <10:
    s -= min2_10
    numMinutes += 1
  while s >=min11 and numMinutes >=10:
    s-=min11
    numMinutes+=1
  return numMinutes
  
  
