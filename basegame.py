import random

def No():
    return random.randint(1, 100)

No1 = No()
No2 = No()

def QType():
    return random.choice(["Add", "Minus", "Times", "Divide"])

CpuChoice = QType()
print(CpuChoice)