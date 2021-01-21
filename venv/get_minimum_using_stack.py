# get minimum using stack with O(1) complexity - constant complexity

top_main = -1
top_supporting = -1
main_stack = []
supporting_stack = []


def get_minimum():
    global supporting_stack, top_supporting
    if top_supporting == -1:
        print("NO ELEMENT IN STACK")
    else:
        return supporting_stack[top_supporting]


def push_array(elem):
    global top_supporting, top_main, main_stack, supporting_stack
    if main_stack.__contains__(elem):
        print("Repetition of numbers not allowed")
        pass
    else:
        top_main = top_main + 1
        main_stack.append(elem)
        if len(supporting_stack) == 0:
            top_supporting = top_supporting + 1
            supporting_stack.append(elem)
        elif supporting_stack[top_supporting] > elem :
            top_supporting = top_supporting + 1
            supporting_stack.append(elem)

def pop_array():
    global top_supporting, top_main, supporting_stack, main_stack
    popped_elem = main_stack.pop()
    top_main = top_main - 1
    if supporting_stack[top_supporting] == popped_elem:
        supporting_stack.pop()
        top_supporting = top_supporting - 1


push_array(1)
push_array(2)
push_array(0)

print(main_stack)
print(supporting_stack)

min = get_minimum()
print(min)

pop_array()
push_array(-2)


print(main_stack)
print(supporting_stack)

min = get_minimum()
print(min)

pop_array()

print(main_stack)
print(supporting_stack)

min = get_minimum()
print(min)

push_array(0)
push_array(0)
push_array(0)
pop_array()


print(main_stack)
print(supporting_stack)

min = get_minimum()
print(min)