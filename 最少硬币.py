def solution(coins, price):
  res = 0
  for i in reversed(coins):
    t,price = divmod(price,i)
    res+=t
  return res
