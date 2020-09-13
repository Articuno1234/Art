# Made by Luke P
import os, sys
import subprocess
from threading import Thread
import json

#data = {}
#data['Config'] = []
#data['Config'].append({
#    'path': '',
#    'ver': '1.1',
#    })
#with open('config.json', 'w+') as jsf:
#    json.dump(data, jsf)
#exc_type, exc_obj, exc_tb = sys.exc_info()
#fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#print(exc_type, fname, exc_tb.tb_lineno)

class Err:
    def moderr(module, num, e=''):
        print('[{}] Module: {} does not exist!'.format(num, module))
        sys.exit()
    def sayerr(num, e):
        print('[{}] {}'.format(num, e))
        
class Lang:
    def comp(line, num):
        if 'say' in line:
            if '#' in line:
                if 'say' in line.split('#')[1]:
                    pass
                else:
                    Lang.say(line.split(';')[1:2], num=num)
            else:
                Lang.say(line.split(';')[1:2], num=num)
        if 'import' in line:
            if '#' in line:
                if 'import' in line.split('#')[1]:
                    pass
                else:
                    Lang.impo(line.split(';')[1:2], num)
            else:
                Lang.impo(line.split(';')[1:2], num)
        if '' in line:
            pass
        if '#' in line:
            pass
        if 'pause' in line:
            Lang.pause(line.split(';')[1:2], num=num)
        #elif 'loop' in line:
        #    if '#' in line:
        #        if 'loop' in line.split('#')[1]:
        #            pass
        #        else:
        #            pass
        #    else:
        #        pass
        #else:
        #    print('[{}] {}'.format(num, line))
    def impo(module, num):
        for k in module:
            if os.path.isdir('data/libs'):
                if os.path.isdir('data/libs/{}'.format(k)):
                    with open('data/libs/{}/init.art'.format(k), 'r') as mod:
                        ln = 0
                        for line in mod:
                            ln += 1
                            Lang.comp(line, ln)
                else:
                    Err.moderr(k, num)
    def say(text='', end='', num=0):
        if end == '':
            try:
                for k in text:
                    print(str(k))
            except:
                print(str(text))
        else:
            try:
                print(str(text), end=end)
            except Exception as e:
                Err.sayerr(num, e)
    def pause(text='', end='', num=0):
        if end == '':
            try:
                for k in text:
                    input(str(k))
            except:
                input(str(text))
        else:
            try:
                input(str(text), end=end)
            except Exception as e:
                Err.sayerr(num, e)

try:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fle:
            ln = 0
            for line in fle:
                ln += 1
                Lang.comp(line, ln)
    else:
        input('File does not exist')
except Exception as e:
    input(e)
