string = "HOLA !,I AM PRANJAL I AM A SOFTWARE ENGINEER"
print(string[0])

print(len(string))
print("SOFTWARE" in string)

string_2 = "10,20,30,40,50"
result="60" in string_2

print(result)
notinresult = "angular" not in string
print(notinresult)


# string slicing

print(string[0:5])

#string slicing from start
print(string[:10])

#string slicing to the End
print(string[3:])
  
  #negative string slicing
print(string[-15:-10])