# 1. Even and Odd Threads

import threading

def Even():
    for i in range(2, 21, 2):
        print(i)

def Odd():
    for i in range(1, 20, 2):
        print(i)

def main():

    EvenThread = threading.Thread(target=Even, name="Even")
    OddThread = threading.Thread(target=Odd, name="Odd")

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

if __name__ == "__main__":
    main()