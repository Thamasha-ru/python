def ask():
    name = input("Enter your name : ")
    marks = float(input("Enter your marks : "))
    return name, marks

def cat(m):
    if 0 <= m < 40:
        return 'F'
    elif 40 <= m < 55:
        return 'S'
    elif 55 <= m < 65:
        return 'C'
    elif 65 <= m < 75:
        return 'B'
    else:
        return 'A'

name, marks = ask()

grade = cat(marks)

print(f'{name} has received an {grade}.')

