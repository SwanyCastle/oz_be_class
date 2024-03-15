from multiprocessing import Process
import os, time

def coke():
    while True:
        try:
            print('콜라 프로세스 아이디 : ', os.getpid())
            print('부모 프로세스 아이디 : ', os.getppid())
        except KeyboardInterrupt:
            break

def cider():
    while True:
        try:
            print('콜라 프로세스 아이디 : ', os.getpid())
            print('부모 프로세스 아이디 : ', os.getppid())
        except KeyboardInterrupt:
            break

def juice():
    while True:
        try:
            print('콜라 프로세스 아이디 : ', os.getpid())
            print('부모 프로세스 아이디 : ', os.getppid())
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print('07.py 프로세스 아이디 : ', os.getpid())
    child1 = Process(target=coke).start()
    time.sleep(0.1)
    child2 = Process(target=cider).start()
    time.sleep(0.1)
    child3 = Process(target=juice).start()
    time.sleep(0.1)