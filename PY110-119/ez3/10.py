# take a string 
# return True if all parentheses are properly matched
# this is a leetcode stack question lol

def is_balanced(string):
    stack = []
    # iterate through string
    # push parentheses onto stack
    for c in string:
        # ) first means False
        # only append (
        # true if stack is empty
        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif c == "(":
            stack.append(c)
        
    print(stack)
# failing the condition where stack is empty because only 1 closing bracket remains
        
    return True if not stack else False
        


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True