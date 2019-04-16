"""
Name: Nicholas Visalli 
Assignment number: 2
Purpose: Implement Joesphus algorithm using queues
"""

import Queue as queue


"""General user input
"""
count = raw_input("How many soldiers? ")
input_string = raw_input("Enter " + count + " soldier names separated by a comma: ")
soldier_list  = input_string.split(",")
position = raw_input("Enter the position: ")


"""Dequeue first `position` soldiers from queue
"""
q = queue.Queue(count)
temp = queue.Queue(count)
for soldier in soldier_list:
    q.put(soldier)

"""Dequeue first `position - 1` soldiers from queue
This removes the soldier at `position`

Place remaing soldiers back into original queue
"""
while q.qsize() != 1:
    for i in range(int(position)):
        soldier = q.get()
        temp.put(soldier)

    for i in range(int(position) - 1):
        soldier = temp.get()
        q.put(soldier)
print(q.get())
