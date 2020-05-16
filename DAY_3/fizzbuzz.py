#Fizz Buzz
#version 1
for x in range(1,51):
  if (x%3==0 and x%5==0):
        print("FizzBuzz")
  elif(x%3==0 or x%5==0):
      print("Fizz")
  else:
      print(x)
#version 2      
list1=["fizzBuzz" if (x%3==0 and x%5==0) else "Fizz" if(x%3==0 or x%5==0) else x for x in range(1,51)]
print(list1)