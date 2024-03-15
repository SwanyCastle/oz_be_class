# 내 파이썬 프로그램의 이름을 알아보자
# psutil 을 이용해서 지금 돌아가고 있는 프로세스에 접근 해서
# 내가 지금 돌리고 있는 지금 이 파이썬 파일과 pid 가 일치하면 그 프로세스의 이름 출력
import psutil, os

current_ps_id = os.getpid()
equal_pid_ps = []

for proc in psutil.process_iter():
    try:
        ps_id = proc.pid
        if current_ps_id == ps_id:
            equal_pid_ps.append(proc.name())
            equal_pid_ps.append(proc.pid)
    except psutil.NoSuchProcess:
        pass

print('day2_task.py 파이썬 코드 실행중 ! 실행중인 프로세스의 아이디는 : ', current_ps_id)
print('day2_task.py 프로세스 아이디와 같은 프로세스 pid : ', equal_pid_ps[1])
print('day2_task.py 프로세스 아이디와 같은 프로세스 name : ', equal_pid_ps[0])
