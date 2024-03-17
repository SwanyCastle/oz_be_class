from  multiprocessing import Process, Pipe
import os

def send(conn):
    print(f'{os.getpid()} 가 {os.getppid()} 에게 데이터를 보낸다!')
    conn.send("hello parent!")
    conn.close()

if __name__ == "__main__":
    # 파이프 클래스를 호출하게되면 튜플 형태로 2개의 객체가 반환된다.
    parent, child = Pipe()
    ps = Process(target=send, args=(child,))
    ps.start()
    print("기존 프로세스 아이디 : ", os.getpid())
    print(parent.recv())
    ps.join()