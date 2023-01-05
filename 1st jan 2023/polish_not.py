# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9

def evalRPN(tokens):
   
  stack = []
  for i in tokens:
      if i in "+-/*":
          op2=(stack.pop())
          op1=(stack.pop())

          if i == '+':
              stack.append(op1+op2)
          elif i == '-':
              stack.append(op1-op2)
          elif i == '*':
              stack.append(op1*op2)
          elif i == '/':
              stack.append(int(float(op1)/op2))
      else:
          stack.append(int(i))
  return (stack.pop())

tokens = ["2","1","+","3","*"]
result = evalRPN(tokens)

print(result)
