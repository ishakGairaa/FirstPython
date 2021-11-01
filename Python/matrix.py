<<<<<<< HEAD
# Matrix 
import replit
import random 

# print the row of matrix  
def row(x,A):
    return A[x] 

# print the column of matrix  
def column(x,A):
    F = []
    for i in range(0,len(A)):
        F.append(A[i][x])
    return F

# print the  diagonal of matrix  
def diagonal(A):
    F = []
    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            if i==j :
                F.append(A[i][j])
    return F 


n = int(input("Enter the length = "))
m = int(input("Enter the width  = ")) 
print(f" length =  {n}")
print(f" width = {m}")
B = []
for i in range(1,m+1):
    B += [[0]*n]
# Matrix fill with random numbers 
for i in range(0,len(B)):
    for j in range(0,len(B[i])):
        B[i][j] = random.randrange(100)

# print the matrix 
for i in range(0,len(B)):
  print(B[i])

print(row(int(input("Enter num of row =  ")),B))
print(column(int(input("Enter num of column = ")),B))
print(" diagonal of matrix  is  = ",diagonal(B))

def down(A,G):
    global x,y,E 
    for i in  range(0,E):
        print(A[x][y])
        G.append(A[x][y])
        x += 1
    x -= 1
    y += 1
    E = E - 1

def right(A,G):
    global x,y,P  
    for i in range(0,P):
        print(A[x][y])
        G.append(A[x][y])
        y += 1
    y -= 1
    x -= 1
    P = P -1

def Up(A,G):
    global x,y,E
    for i in range(0,E):
        print(A[x][y])
        G.append(A[x][y])
        x -= 1
    x += 1
    y -= 1
    E = E-1

def left(A,G):
    global x,y,P
    for i in range(0,P) :
        print(A[x][y])
        G.append(A[x][y])
        y -= 1
    y += 1
    x += 1
    P = P-1


x= 0 
y = 0 
G = []
E =  len(B)
P = len(B[0])-1

while P>=0 and E>0 :
  down(B,G)
  if(P==0):
      break
  right(B,G)
  if(E==0):
      break
  Up(B,G)
  if(P==0):
      break
  left(B,G)


print(f"The length of array = {len(G)}")
print(f"The result array = {G}")
# for i in range(0,len(B)):
=======
# Matrix 
import replit
import random 

# print the row of matrix  
def row(x,A):
    return A[x] 

# print the column of matrix  
def column(x,A):
    F = []
    for i in range(0,len(A)):
        F.append(A[i][x])
    return F

# print the  diagonal of matrix  
def diagonal(A):
    F = []
    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            if i==j :
                F.append(A[i][j])
    return F 


n = int(input("Enter the length = "))
m = int(input("Enter the width  = ")) 
print(f" length =  {n}")
print(f" width = {m}")
B = []
for i in range(1,m+1):
    B += [[0]*n]
# Matrix fill with random numbers 
for i in range(0,len(B)):
    for j in range(0,len(B[i])):
        B[i][j] = random.randrange(100)

# print the matrix 
for i in range(0,len(B)):
  print(B[i])

print(row(int(input("Enter num of row =  ")),B))
print(column(int(input("Enter num of column = ")),B))
print(" diagonal of matrix  is  = ",diagonal(B))

def down(A,G):
    global x,y,E 
    for i in  range(0,E):
        print(A[x][y])
        G.append(A[x][y])
        x += 1
    x -= 1
    y += 1
    E = E - 1

def right(A,G):
    global x,y,P  
    for i in range(0,P):
        print(A[x][y])
        G.append(A[x][y])
        y += 1
    y -= 1
    x -= 1
    P = P -1

def Up(A,G):
    global x,y,E
    for i in range(0,E):
        print(A[x][y])
        G.append(A[x][y])
        x -= 1
    x += 1
    y -= 1
    E = E-1

def left(A,G):
    global x,y,P
    for i in range(0,P) :
        print(A[x][y])
        G.append(A[x][y])
        y -= 1
    y += 1
    x += 1
    P = P-1


x= 0 
y = 0 
G = []
E =  len(B)
P = len(B[0])-1

while P>=0 and E>0 :
  down(B,G)
  if(P==0):
      break
  right(B,G)
  if(E==0):
      break
  Up(B,G)
  if(P==0):
      break
  left(B,G)


print(f"The length of array = {len(G)}")
print(f"The result array = {G}")
# for i in range(0,len(B)):
>>>>>>> c52f537104e665839f83ba08fdd4289588e731e7
#   print(B[i])