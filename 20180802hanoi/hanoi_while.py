while(1):
  num = int(input("input the number(press 0 to leave):"))
  if(num==0):
    break
  
  # 0:A, 1:B, 2:C
  move = []
  for i in range(0,3):
    move.append(True)

  A = []
  B = []
  C = []
  A.append(10000)
  B.append(10000)
  C.append(10000)
  i=num
  while(i>1):
    A.append(i)
    i -= 1
  
  current_num = num
  if(num%2 == 1):
    if(current_num==1):
          current_num -= 1
    C.append(1)
    print(1,"A->C")
    smallest_cur = 'C'
    smallest_dir = False
    move[2] = False
  else:
    B.append(1)
    print(1,"A->B")
    smallest_cur = 'B'
    smallest_dir = True
    move[1] = False

  # smallest plate move when steps is odd
  # when num is odd(False)/even(True), smallest plate move left/right(rotate)
  steps = 2
  while(current_num>0):
    itemA = A[len(A)-1]
    itemB = B[len(B)-1]
    itemC = C[len(C)-1]
    
    if(steps%2 == 1): # smallest
      if(smallest_cur=='A'):
        if(smallest_dir):
          print(1,"A->B")
          B.append(1)
          smallest_cur = 'B'
          move[1] = False
          move[2] = True
        else:
          print(1,"A->C")
          C.append(1)
          smallest_cur = 'C'
          move[1] = True
          move[2] = False
          if(current_num==1):
            current_num -= 1	
        A.pop()
        move[0] = True
      elif(smallest_cur=='B'):
        if(smallest_dir):
          print(1,"B->C")
          C.append(1)
          smallest_cur = 'C'
          move[0] = True
          move[2] = False
          if(current_num==1):
            current_num -= 1
        else:
          print(1,"B->A")
          A.append(1)
          smallest_cur = 'A'
          move[0] = False
          move[2] = True	
        B.pop()
        move[1] = True
      elif(smallest_cur=='C'):
        if(smallest_dir):
          print(1,"C->A")
          A.append(1)
          smallest_cur = 'A'
          move[0] = False
          move[1] = True
        else:
          print(1,"C->B")
          B.append(1)
          smallest_cur = 'B'
          move[0] = True
          move[1] = False	
        C.pop()
        move[2] = True
    elif(move[0]&((itemA<itemB)|(itemA<itemC))):
      if(itemA<itemB):
        print(itemA,"A->B")
        B.append(itemA)
        A.pop()       
        move[1] = False
        move[2] = True
      elif(itemA<itemC):
        if(itemA==current_num):
          current_num -= 1
        print(itemA,"A->C")
        C.append(itemA)
        A.pop()
        move[1] = True 
        move[2] = False
    elif(move[1]&((itemB<itemA)|(itemB<itemC))):
      if(itemB<itemA):
        print(itemB,"B->A")
        A.append(itemB)
        B.pop()        
        move[0] = False
        move[2] = True
      elif(itemB<itemC):
        if(itemB==current_num):
          current_num -= 1
        print(itemB,"B->C")
        C.append(itemB)
        B.pop()       
        move[0] = True 
        move[2] = False
    elif(move[2]&((itemC<itemA)|(itemC<itemB))):
      if(itemC<itemA):
        print(itemC,"C->A")
        A.append(itemC)
        C.pop()
        move[0] = False 
        move[1] = True
      elif(itemC<itemB):
        print(itemC,"C->B")
        B.append(itemC)
        C.pop()
        move[0] = True 
        move[1] = False

    steps += 1


