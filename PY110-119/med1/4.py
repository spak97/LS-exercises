"""

"""
def minilang(cmd):
    stack = []
    reg = 0
    cmd_list = cmd.split()
    for command in cmd_list:
        if command.isnumeric() or command.startswith("-"):
            reg = int(command)
        elif command == "PUSH":
            stack.append(reg)
        elif command == "ADD":
            reg += int(stack.pop())        
        elif command == "SUB":
            reg -= int(stack.pop())
        elif command == 'MULT':
            reg *= int(stack.pop())
        elif command == 'DIV':
            reg //= int(stack.pop())
        elif command == 'REMAINDER':
            reg %= int(stack.pop())
        elif command == 'POP':
            reg = int(stack.pop())
        elif command == 'PRINT':
            print(reg)


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)