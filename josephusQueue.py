import Queue as queue

count = raw_input("How many soldiers? ")
input_string = raw_input("Enter " + count + " soldier names separated by a comma: ")
soldier_list  = input_string.split(",")
position = raw_input("Enter the position: ")

q = queue.Queue(count)
temp = queue.Queue(count)
for soldier in soldier_list:
    q.put(soldier)

while q.qsize() != 1:
    for i in range(int(position)):
        soldier = q.get()
        temp.put(soldier)

    for i in range(int(position) - 1):
        soldier = temp.get()
        q.put(soldier)
print(q.get())
