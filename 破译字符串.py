def solution(note):
  res = []
  tinydict = {'a': '0', 'b': '1', 'c': '2','d':'3','e': '4', 'f': '5', 'g': '6','h':'7','i': '8', 'j': '9'}
  for search_char in note:
        if (search_char in tinydict.keys()):
          res.append(tinydict[search_char])
        elif(search_char in tinydict.values()):
          res.append(getKey(tinydict,search_char))
        else:
          res.append(search_char)
        
  return ''.join(res)

#根据value找到对应的key
def getKey(dic,value):
  result = ''
  for key in dic:
    if dic[key] == value:
      result+=key
  if(len(result)!=0):
    return  result
  else:
    return None
