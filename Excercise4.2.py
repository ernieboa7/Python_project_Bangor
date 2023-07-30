def lisp_evaluation(item):
    #replace brackets with an empty string in the expression
    trimItem = item.replace("(", "") 
    trimItem = trimItem.replace(")", "")
    items = trimItem.split(" ")
    # Create stacks to hold the operands
    stack1 = []
    stack2 = []

    # Iterate through the items
    for i in reversed(items):
        if i == "+":
            # Remove the two operands from the stack, add them, and push the output back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 + operand2
            stack1.append(output)
        elif i == "-":
            # Remove the two operands from the stack, subtract the second operand from the first, and push the output back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 - operand2
            stack1.append(output)
        elif i == "*":
            # Remove the two operands from the stack, multiply them, and push the output back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 * operand2
            stack1.append(output)
        elif i == "/":
            # Remove the two operands from the stack, divide the first operand by the second, and push the output back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 / operand2
            stack1.append(output)
        else:
            # If the i is not an operator, it must be an operand. Convert it to a number and push it to the stack
            stack1.append(int(i))
    if(len(stack1) == 1):
        return stack1[0]
    #check the first operator
    operator = i[0]    
    # The last output should be the only element left on the stack
    for j in reversed(stack1):
        
        if operator == "+":
            # Remove the two operands from the stack, add them, and push the output back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 + operand2
            stack2.append(output)
        elif operator == "-":
            # Remove the two operands from the stack, subtract the second operand from the first, and push the result back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 - operand2
            stack2.append(output)
        elif operator == "*":
            # remove the last two operands from the stack, multiply them, and push the result back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 * operand2
            stack2.append(output)
        elif operator == "/":
            # Pop the last two operands from the stack, divide the first operand by the second, and push the result back to the stack
            operand1 = stack1.pop()
            operand2 = stack1.pop()
            output = operand1 / operand2
            stack2.append(output)
        else:
            # If the j is not an operator, it must be an operand. Convert it to a number and push it to the stack 
            stack2.append(int(j))

    return stack2[0]

   

# Test the interpreter
print(lisp_evaluation("(+ (* 5 6) (* 4 5) (* 2 6))")) 

