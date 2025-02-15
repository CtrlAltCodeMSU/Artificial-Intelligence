p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter Your Comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
  print("This comment is a Spam")
else:
  print("THis comment is not spam")