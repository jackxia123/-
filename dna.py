paris ={'A':'T','T':'A','C':'G','G':'C'}
def solution(dna):
  return ''.join([paris[x] for x in dna])
