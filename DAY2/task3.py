sample_str = input("Enter a string: ")
first_char = sample_str[0]
print("first character: ",first_char)
last_char = sample_str[-1]
print("last character: ",last_char)
length = len(sample_str)
if length%2==0:
  i = int(length/2)-1
  print("Middle character: ",sample_str[i]+sample_str[i+1]) 
else:
    print("Middle character: ",sample_str[int(length/2)])

