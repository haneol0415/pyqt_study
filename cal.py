prefix = input()

priority = {"+" : 0, "-" : 0, "*" : 1, "/" : 1}

# 63*41-71*400*110-5
# 2*3-4*5+2
# 연산자를 만나기 전까지는 숫자를 이어 붙인다.

def preToPost(prefix):
    postfix = []
    operators = []
    num = ''
    
    for i in prefix:
        if i not in priority.keys():
            num += i
        else:
            postfix.append(num)
            num = ''
            if len(operators) == 0 or priority[i] > priority[operators[-1]]:
                operators.append(i)
            else:
                while len(operators) != 0 and priority[i] <= priority[operators[-1]]:
                    postfix.append(operators.pop())
                operators.append(i)
    
    postfix.append(num)
    while len(operators) != 0:
        postfix.append(operators.pop())
    
    return postfix

def getResult(postfix):
    operands = []
    for i in postfix:
        if i not in priority.keys():
            operands.append(i)
        else:
            second = operands.pop()
            first = operands.pop()
    
            if i == '+':
                result = float(first) + float(second)
            elif i == '-':
                result = float(first) - float(second)
            elif i == '*':
                result = float(first) * float(second)
            else:
                result = float(first) / float(second)
            
            operands.append(result)

    return operands.pop()

postfix = preToPost(prefix)
result = getResult(postfix)
print(result)



# operators = []
# postfix = []
# num = ''
# for i in prefix:
#   if i not in priority.keys():
#     num += i
#   else:
#     postfix.append(num)
#     num = ''
#     if len(operators) == 0 or priority[i] > priority[operators[-1]]:
#       operators.append(i)
#     else:
#       while len(operators) != 0 and priority[i] <= priority[operators[-1]]:
#         postfix.append(operators.pop())
#       operators.append(i)
          
# postfix.append(num)
# while len(operators) != 0:
#   postfix.append(operators.pop())

# print(postfix)

# operands = []
# for i in postfix:
#   if i not in priority.keys():
#     operands.append(i)
#   else:
#     second = operands.pop()
#     first = operands.pop()
    
#     if i == '+':
#       result = int(first) + int(second)
#     elif i == '-':
#       result = int(first) - int(second)
#     elif i == '*':
#       result = int(first) * int(second)
#     else:
#       result = int(first) / int(second)
    
#     operands.append(result)

# print(operands.pop())