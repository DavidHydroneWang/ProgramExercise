#!/usr/bin/env python
# coding=utf-8
import  threading, time, random


class Container1():
    def __init__(self):
        self.contents = 0
        self.avaliable = False
        self.cv = threading.Condition()

    def put(self, value):
        with self.cv:
            if self.avaliable:
                self.cv.wait()
            self.contents = value
            t = threading.current_thread()
            print('{0}生产{1}'.format(t.name, self.contents))
            self.avaliable = True
            self.cv.notify()

    def get(self):
        with self.cv:
            if not self.avaliable:
                self.cv.wait()
            t = threading.current_thread()
            print('{0}消费{1}'.format(t.name, self.contents))
            self.avaliable = False
            self.cv.notify()


class Container2():
    def __init__(self):
        self.contents = 0
        self.avaliable = False

    def put(self, value):
        if self.avaliable:
            pass
        else:
            self.contents = value
            t = threading.current_thread()
            print('{0}生产{1}'.format(t.name, self.contents))
            self.avaliable = True

    def get(self):
        if not self.avaliable:
            pass
        else:
            t = threading.current_thread()
            print('{0}消费{1}'.format(t.name, self.contents))
            self.avaliable = False


class Producer(threading.Thread):
    def __init__(self, container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        for i in range(1, 6):
            time.sleep(random.choice(range(5)))
            self.container.put(i)


class Consumer(threading.Thread):
    def __init__(self, container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        for i in range(1, 6):
            time.sleep(random.choice(range(5)))
            self.container.get()


def test1():
    print('基本同步通信的生产着消费者模型：')
    container = Container1()
    Producer(container).start()
    Consumer(container).start()


def test2():
    print('无同步通信的生产着消费者模型：')
    container = Container2()
    Producer(container).start()
    Consumer(container).start()


if __name__ == '__main__':
#    test1()
    test2()
