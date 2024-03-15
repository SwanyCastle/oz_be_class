import threading, os, time

def seomthing(word):
    while True:
        print(word)
        time.sleep(3)

if __name__ == "__main__":
    print('기존 프로세스 아이디 : ', os.getpid())
    thread = threading.Thread(target=seomthing, args=('happy',))
    thread.daemon = True
    thread.start()
    print('메인 스레드에서 반복문 시작')
    while True:
        try:
            print('daily.....')
            time.sleep(1)
        except KeyboardInterrupt:
            print('good bye')
            break