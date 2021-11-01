x= 0 
y = 0 
G = []
E =  len(B)
P = len(B[0])-1

while P>0 and E>0 :
  down(B,G)
  right(B,G)
  Up(B,G)
  left(B,G)

print(G)