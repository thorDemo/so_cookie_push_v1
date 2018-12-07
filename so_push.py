from threadpool import ThreadPool, makeRequests
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini', 'utf-8')
https = int(config.get('so_push', 'https'))
thread_num = int(config.get('so_push', 'thread'))
target = config.get('so_push', 'target')
if https == 1:
    from mylib.so_push import http_push
    pool = ThreadPool(thread_num)
    arg = []
    for x in range(0, thread_num):
        arg.append(target)
    request = makeRequests(http_push, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
elif https == 0:
    from mylib.so_push import http_push
    pool = ThreadPool(thread_num)
    arg = []
    for x in range(0, thread_num):
        arg.append(target)
    request = makeRequests(http_push, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
