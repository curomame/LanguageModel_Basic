def removeEnter(lines):
  newLines = []
  for word in lines:
    newLines.append(word.replace('\n',''))
  return newLines


def splitMerge(lines):
  splitLines = []
  for word in lines:
    splitLines.append(list(word))
  return splitLines
  

def bep(filepath):
  file = open(filepath,"r")
  lines = file.readlines()
  newLines = removeEnter(lines)

  return lines
  
  
bep('example1.txt')


# merges.txt 만들기

# 1. 모든 글자를 하나씩 쪼개기