#coding:utf-8
#python3
import requests
import threading,queue,sys,os
class RedisUN(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue
    def run(self):
        while True:
            if self._queue.empty():
                break
            try:
                ########################## 代码放入这################################## 
                url = 'http://'+ self._queue.get(timeout=0.5)
                r = requests.get(url)
                # f = open('result.txt','a+') 
                # f.write(url+r.status_code+"\n") 

                if r.status_code == 200:#输出响应码为200的url
                    f = open('result.txt','a+') 
                    f.write(url+"\n") 
                

                #####################################################################
            except:
                continue
def banner():
    print("*"*50)
    print("*"*2+" "*13+"url activity scan V2"+" "*13+"*"*2)
    print("*"*50)

def main():
    thread_count = 10  #线程数
    threads = []
    q = queue.Queue()
    f = open("url.txt",'r') #读取txt里的ip
    sourceInLines = f.readlines()
    f.close()
    new = []
    for line in sourceInLines:
        temp1 = line.strip('\n')
        q.put(temp1)
 
    for i in range(thread_count):
        threads.append(RedisUN(q))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
 
if __name__ == '__main__':
    banner()
    f1 = open('result.txt','w')
    f1.close()
    #main()
