def findXYZ(n) :
  const  = []

  for x in range(n) :
    for y in range(n):
      for z in range(n):
        if( 3*x + 9*y + 8*z == 79 ) :
            #print(f" x = {x} , y = {y} , z = {z} ")
            const.extend([x,y,z])
  return const


print(findXYZ(10)); # => [{x: 0, y: 7, z: 2}, ...]

