def factorial( n ):
    if n <= 1:
        return 1
    return n * factorial( n-1 )

print( factorial( 5 ) )



def factorial(r):
    if (r>0):
        result =  r * factorial(r-1)
        return result 
    else:
        r <= 1
        return 1 

print(factorial(5))



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)







