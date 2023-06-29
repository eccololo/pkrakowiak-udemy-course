score_stack = []
last_element = len(score_stack) - 1
score_stack.append("0-0")
print(score_stack[last_element])
score_stack.append('1-0')
print(score_stack[last_element])
score_stack.append('1-1')
print(score_stack[last_element])
score_stack.append('1-2')
print(score_stack[last_element])
canceled = score_stack.pop(last_element)
print(score_stack[last_element])
