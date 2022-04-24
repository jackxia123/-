def solution(inputArray):
  max=0
  res=[]
  for arr in inputArray:
    if (len(arr)>max):
      max =len(arr)
  for arr in inputArray:
    if(len(arr)==max):
      res.append(arr)
      
  return res
