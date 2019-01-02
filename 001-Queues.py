"""The Expected behavior of a structure using queue is what happens on any real life queues
When you are in a queue at the bank you have to wait until it's your turn
So it's called a FIFO structure, where the acronymous stands for First-In-First-Out
"""
import time
queue=[]

print("Lets open our fictional queue!")
print("Put the first person arriving into the queue:")
queue.append(input())
print("\nLets see our queue now")
print(queue)

print("Now keep putting people in the queue to see the shape its being formed")
while True:    
    print("\nPut the next person arriving into the queue: (if you want to stop just press '-')")
    var = input()
    if var != '-':
        queue.append(var)
        print("\nLets see our queue:")        
        print(queue)
    else:
        print("\nThat's it, you have finished our queue")
        break

print("\nLets see our queue now")        

print("Now lets see who will leave the queue in order!\n")
while queue:
    print("==> {} left the queue to be served".format(queue.pop(0)))
    print(queue,"\n")
    if queue == []:
        print("Now our queue is empty and the program will end!")
    time.sleep(2)

print("\nAs you've seen the first element to arrive into our queue was the first element to leave the queue(FIFO)")
    

