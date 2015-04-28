# _*_ coding:utf-8 _*_
'''
Created on 2013-03-25
@author: jimmy.dong@gmail.com
'''
import os
import urllib.request

class MyJobs(object):

    def __init__(self, param ):
        #do something
        self.param = param

    def __del__(self):
        ''' destruct '''
        self.exit()

    def exit(self):
        ''' 退出'''
        self.quit = True

    def run(self):
        ''' 开始处理 '''
        #使用shell模式
        #cmd = '/usr/bin/curl "http://at.yoka.com/try/amqp_consume.php?key=' + str(self.param) + '"'
        cmd = 'D:/CYDPHP/soft/php5.4.27/php.exe -c D:/CYDPHP/soft/php5.4.27/php.ini D:/CYDPHP/www/test_rabbitmq/consumer.php ' + str(self.param)
        re = os.system(cmd)

        #使用web模式
        #req = urllib.request.urlopen('http://at.yoka.com/try/amqp_consume.php?key=' + str(self.param))
        #re = req.read()
        #print re