msg_ = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]

good = {"+", "-", "*", "/"}
memory = 0
result = 0

def start():
    print(msg_[0])
    calc = input()
    calc = calc.split()
    global memory

    if len(calc) == 3:
        first = calc[0]
        operator = calc[1]
        second = calc[2]
        if first == "M":
            first = memory
        if second == "M":
            second = memory
        checkme(first, second, operator)
    else:
          print(msg_[1])
          start()


def checkme(first, second, operator):
    try:
        float(first)
        first = float(first)
        try:
            float(second)
            second = float(second)
            if operator in good:
                lazy_check(first, second, operator)
            else:
                print(msg_[2])
                start()
        except ValueError:
            print(msg_[1])
            start()
    except ValueError:
        print(msg_[1])
        start()

def calculate(first, second, operator):
    global result
    if operator == "+":
        result = (first + second)
    elif operator == "-":
        result = (first - second)
    elif operator == "*":
        result = (first * second)
    elif operator == "/":
        if second == 0:
            print(msg_[3])
            start()
        else:
            result = (first / second)
    if result or result == 0:
        print(result)
        message_4(result)

def message_4(result):
    print(msg_[4])
    answer = input()
    if answer == "y" or answer == "n":
        if answer == "y":
            save_memory(result)
        message_5(result)
    else:
        message_4(result)

def save_memory(result):
    global memory
    if is_one_digit(result):
        msg_index = 10
        answer_me(msg_index, result)
    else:
        memory = result
        message_5(result)

def answer_me(msg_index, result):
    global memory
    printme = msg_[msg_index]
    print(printme)
    answer = input()
    if answer == "y" and msg_index < 12:
        msg_index = msg_index + 1
        answer_me(msg_index, result)
    elif msg_index >= 12 or answer != "n":
        memory = result
    message_5(result)

def message_5(result):
    print(msg_[5])
    answer1 = input()
    if answer1 == "y":
        start()
    elif answer1 == "n":
        pass
    else:
        message_5(result)

def lazy_check(first, second, operator):
    msg = ""
    if is_one_digit(first) and is_one_digit(second):
        msg = msg + msg_[6]
    if (first == 1 or second == 1) and operator == "*":
        msg = msg + msg_[7]
    if(first == 0 or second == 0) and (operator == "*" or operator == "+" or operator == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)
    calculate(first, second, operator)

def is_one_digit(digit):
    if (digit > -10 and digit < 10) and (digit == int(digit)):
            return True
    return False

start()
