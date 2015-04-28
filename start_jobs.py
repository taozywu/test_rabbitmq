# _*_ coding:utf-8 _*_
'''
yoka at 实现多线程处理任务的守护进程
Created on 2012-4-7
@author: xwarrior
@update: jimmy.dong@gmail.com
'''
#在此引入项目需要的数据包
from MyJobs import MyJobs
from MyThread import MyThread
import logging
import time

def main():
    logger = logging.getLogger('main()')
    logger.info('server start!')
    worker_threads = 4 #定义需要启动的线程数量
    timeline = 2 #线程检查时间间隔，秒
    thread_pool = {}

    for i in range(0, worker_threads ):
        param = 'some param'
        job = MyJobs( param )
        thread = MyThread( job, i )
        thread.setDaemon = True
        thread.start()
        logger.info('start thread %s' %( thread.getName() ))
        thread_pool[i] = thread

    #干完就结束模式
    #for eachKey in thread_pool.keys():
    # thread_pool[eachKey].join()

    #保持线程数量模式
    while 1:
        time.sleep(timeline)
        # 检查每一个线程
        for eachKey in thread_pool.keys():
            if thread_pool[eachKey].isAlive():
                print ('thread alive:' + str(i))
            else:
                print ('thread down:' + str(i))
                thread_pool[eachKey].run()

    logger.info('main exist!')
    return

if __name__ == '__main__':
    #init config format
    FORMAT = '%(asctime)-15s %(name)s %(levelname)s file %(filename)s:lineno %(lineno)s - %(message)s'
    logging.basicConfig(format=FORMAT,level=logging.INFO)

    main()
    pass