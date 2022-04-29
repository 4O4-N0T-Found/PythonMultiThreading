import os, sys, time, subprocess
from threading import Thread, Lock

# 读取文件夹中所有待处理文件的名称
print('Loading File List···')
fileList = set(os.listdir(sys.argv[1]))
print('Loading finished! Total:', len(fileList))
time.sleep(1)

# 创建输出文件addr2hash.txt
wf = open("addr2hash.txt", "w")
counter = 0

lock_fileList = Lock()
lock_wf = Lock()    # 写文件 锁

def mutexGetFileName():
    lock_fileList.acquire()
    if len(fileList) == 0:
        fileName =  None
    else:
        fileName = fileList.pop()
    lock_fileList.release()
    return fileName

# 调用oyente.py来处理文件
def processFile(fileName):
    # 用这个os命令来调用oyente.py
    osCmd = "python3 oyente.py " + sys.argv[1] + "/" + fileName
    _, result = subprocess.getstatusoutput(osCmd)
    return result

def mutexWriteFile(content):
    global counter
    lock_wf.acquire()
    wf.write(content + "\n")
    counter += 1
    lock_wf.release()

def myThread():
    while True:
        fileName = mutexGetFileName()
        if fileName == None:
            break
        else:
            result = processFile(fileName)
            mutexWriteFile(result)
            print('%s [INFO] %d File: %s' % (time.strftime("%y-%m-%d %H:%M:%S", time.localtime()), counter, fileName))
            

if __name__ == "__main__":
    startTime = time.asctime(time.localtime(time.time()))
    threads = []
    # 线程数
    for _ in range(4):
        thread = Thread(target=myThread)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    
    wf.close()  # 这个写法的目的是只打开输出文件一次，减少文件IO的开销。
    endTime = time.asctime(time.localtime(time.time()))
    print('start:', startTime, '\n  end:', endTime)