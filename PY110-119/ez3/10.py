# take a string 
# return True if all parentheses are properly matched
# this is a leetcode stack question lol

def is_balanced(string):
    # just solve it using a stack
    stack = []
    # iterate through string
    # push parentheses onto stack
    for i, c in enumerate(string):
        if c in ")":
            stack.append(c)
    # if matching parenthesis is found, pop from stack
        if stack and stack[-1] == "(":
            stack.pop()
    # if stack empty, return True
    print(stack)
    if stack:
        return False
    else:
        return True
    
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True