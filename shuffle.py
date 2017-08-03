"""
Things to add that were included in my original java program from college:
1. Generate the Cauchy cycle notation for the simple shuffle on 2n objects

Ways to generalize the problem:
1. Allow for shuffling of more than 2 stacks
2. Allow for shuffling of more than 2 colors
3. Allow for shuffling of arbitrary number of colors in arbitrary starting positions
4. Allow for shuffling of uneven stacks (if this even makes sense-- perhaps the def'n of shuffling should exclude this
5. Moving element in position i to position k in as few shuffles as possible (well studied, do online research)

The granddaddy question:
Is it possible to generate all permutations through a series of in and out shuffles?  
If no, what is the subset of all permutations that is spanned by in/out shuffling?
"""
import csv

class SimpleShuffle(object):
  def __init__(self, stacksize):
    self.origStack1 = [0 for x in range(int(stacksize))]
    self.origStack2 = [1 for x in range(int(stacksize))]

  def shuffleOnce(self, list1, list2, isInShuffle = True): 
    #single shuffle on the current stacks
    if isInShuffle:
      #print("In shuffle")
      temp = []
      for i in range(len(list1)):
        temp.append(list1[i])
        temp.append(list2[i])
      return temp[:len(list1)], temp[len(list2):]
    else:
      #print("Out shuffle")
      temp = []
      for i in range(len(list1)):
        temp.append(list2[i])
        temp.append(list1[i])
      return temp[:len(list1)], temp[len(self.list2):]
      
  def printStacks(self,list1,list2):
    for x,y in zip(list1, list2):
      print(x,y)
  
  def shuffleCycle(self):
    if len(self.origStack1) % 100 == 0: 
      print(len(self.origStack1))
    tempList1 = self.origStack1
    tempList2 = self.origStack2
    #self.printStacks(tempList1, tempList2)
    tempList1, tempList2 = self.shuffleOnce(tempList1,tempList2)
    #self.printStacks(tempList1, tempList2)
    counter = 1
    while (self.origStack1 != tempList1):
      counter = counter+1
      tempList1, tempList2 = self.shuffleOnce(tempList1, tempList2)
      #self.printStacks(tempList1, tempList2)
    return counter
    
if __name__ == '__main__':
  shuffleList = [SimpleShuffle(i) for i in range(2000)]
  output = []
  for item in shuffleList:
    output.append(item.shuffleCycle())
  with open('output.csv', 'w',encoding='utf8',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in output:
      writer.writerow([item])
    csvfile.close()