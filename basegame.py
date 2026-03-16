import random

def No():
    return random.randint(1, 100)

No1 = No()
No2 = No()

def QType():
    return random.choice(["Add", "Minus", "Times", "Divide"])
CpuChoice = QType()

def Add():
    Ans = No1 + No2
    return Ans

def Minus():
    Ans = No1 - No2
    return Ans

def Times():
    Ans = No1 * No2
    return Ans

if CpuChoice == 'Add':
    Ques = int(input(f"What is {No1} + {No2} = "))
    Ans = Add()
    if Ques == Ans:
        print('Correct')
    elif Ques != Ans:
        print("Wrong")
    else:
        print("error")
elif CpuChoice == 'Minus':
    Ques = int(input(f"What is {No1} - {No2} = "))
    Ans = Minus()
    if Ques == Ans:
        print('Correct')
    elif Ques != Ans:
        print("Wrong")
    else:
        print("error")
elif CpuChoice == 'Times':
    Ques = int(input(f"What is {No1} x {No2} = "))
    Ans = Times()
    if Ques == Ans:
        print('Correct')
    elif Ques != Ans:
        print("Wrong")
    else:
        print("error")
elif CpuChoice == 'Divide':
    Ques = int(input(f"What is {No1} + {No2} = "))
    Ans = Add()
    if Ques == Ans:
        print('Correct')
    elif Ques != Ans:
        print("Wrong")
    else:
        print("error")

CpuChoice = QType()


