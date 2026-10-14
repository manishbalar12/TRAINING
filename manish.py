a=float(input("Enter a number:"))
b=float(input("Enter b number:"))
symbol=input()
match symbol:
    case '+':
        print("sum:",a+b)
    case '-':
        print("diff:",a-b)
    case '*':
        print("multi:",a*b)
    case '/':
        print("div:",a/b)
    case '//':
        print("floor div:",a//b)
    case '%':
        print("mod:",a%b)
    case '**':
        print("sqr:",a**b)
    case _:
        print("INVALID ")
