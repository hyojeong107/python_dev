import threading
import time

# thread로 작동될 함수 선언 
def say(msg):
    while True:
        time.sleep(1)
        print(msg)
        
# 3개의 thread 생성하는 반복 
for msg in ['you','need','python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True # 메인스레드가 종료되면 자식스레드들도 종료 된다 
    t.start()
    
for i in range(100):
    time.sleep(0.1)
    print(i)