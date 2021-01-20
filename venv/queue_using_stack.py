# QUEUE USING STACK
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)
        print(x, "INSERTED TO QUEUE")

    def dequeue(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
            x = self.s2.pop()
            print(x, "DELETED FROM QUEUE")
        else:
            x = self.s2.pop()
            print(x, "DELETED FROM QUEUE")

if __name__ == '__main__':
    q = Queue()
    while True:
        print("1.INSERT 2.REMOVE 3.DISPLAY")
        choice = input("ENTER THE CHOICE : ")
        if choice == '1':
            elem = input("ENTER THE ELEMENT TO INSERT : ")
            q.enqueue(elem)
        elif choice == '2':
            if len(q.s1) == 0 and len(q.s2) == 0:
                print("NO ELEMENTS IN QUEUE TO DEQUEUE")
            else:
                q.dequeue()
