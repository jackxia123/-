import re
def solution(i):
  for arr in i.split("-"):
    if(re.match('[0-9A-F]',i)):
      return True
    else:
      return False

print(solution("01-23-45-67-89-AB"))
