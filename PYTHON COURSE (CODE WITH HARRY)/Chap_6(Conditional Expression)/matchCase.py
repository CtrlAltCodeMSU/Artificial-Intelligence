while True:
  x = int(input("enter the value of x: "))
  match x:
    case 0:
      print("x ix zero")
    case 4:
      print("case is 4")
    case _:
      print(x)