# _*_ coding:utf-8 _*_
'''
Created on 2013-03-25
@author: jimmy.dong@gmail.com
'''
from threading import Thread

class MyThread(Thread):
    '''
    创建线程
    '''

    def __init__(self,job,thread_id):
        '''
        Constructor
        '''
        self.job = job
        Thread.__init__(self, name = 'my_thread_%s' %(thread_id))

    def run(self):
        self.job.run()

    def stop(self):
        self.job.exit()