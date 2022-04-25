import re
def solution(maxLength, text):
  count=0
  for ier in re.split("[] ;',:?!]",text):
    if(len(ier) <=maxLength and ier):
      count+=1
  return count
  
  

print(solution(4,"The Fox asked the stork, 'How is the soup?'"))
