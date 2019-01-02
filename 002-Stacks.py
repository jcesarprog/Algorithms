"""The Expected behavior of a structure using a stack is what happens on any real life stacks
When you need to wash dishes you end up making a stack of dirty plates
And it's called a LIFO structure, where the acronymous stands for Last-In-First-Out
"""
import time
stack=[]

print("Lets open our fictional Stack!")
print("Put the first object arriving into the stack:")
stack.append(input())
print("\nLets see our stack now")
print(stack)

print("Now keep putting objects in the stack to see the shape its being formed")
while True:    
    print("\nPut the next object arriving into the stack: (if you want to stop just press '-')")
    var = input()
    if var != '-':
        stack.append(var)
        print("\nLets see our stack")
        print(stack)
    else:
        print("\nThat's it, you have finished our stack")
        break

print("\nLets see our stack now")        

print("Now lets see who will leave the stack in order!\n")
while stack:
    print("==> {} left the stack to be served".format(stack.pop()))
    print(stack,"\n")
    if stack == []:
        print("Now our stack is empty and the program will end!")
    time.sleep(2)

print("\nAs you've seen the first element to arrive into our stack was the first element to leave the stack(LIFO)")
    

