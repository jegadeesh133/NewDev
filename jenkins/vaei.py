# i=0
# def add(a,b):
#     return print(a+b)
# def sub(a,b):
#     return print(a-b)
# while (i<4):
#     print("1.Add\n2.Sub\n3.Multi\n4.Divide")
#     choice = input("enter your choice : ")
#     a  = int(input("enter a"))
#     b = int(input("enter b"))

#     if(choice == "1" or choice == "add"):
#         add(a,b)
#     elif(choice == "2"):
#         sub(a,b)
#     elif(choice == "3"):
#         print("addition of a+b is", a*b)
#     elif(choice == "4"):
#         if(b != 0):
#             print("addition of a+b is", a/b)
#         else:
#             print("veliya poda ")
#     else:
#         print("invalid input")
#     i = i+1
# else:
#     print("free trail over")

def add(a,b):
 
    return print(a+b)
    
try:
    add(1)
except TypeError:
    print("miising paramerer")


