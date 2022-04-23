def solution(inputString):
  #定义26个字母的字典
  res=''
  tinyDict={'a':'z','b':'y','c':'x','d':'w','e':'v','d':'u','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':'a'}
  for search_text in inputString:
    if (search_text in tinyDict.keys()):
      res+=tinyDict[search_text]
  return res
  
print(solution("avyz"))
