#!/usr/bin/python
# -*- coding:utf-8 -*-

import codecs
import subprocess
import sys

import RPi.GPIO as GPIO
from time import sleep

s1 = u'現在起動しています/リターンコード：'
s2 = u'起動を開始しました/リターンコード:'
s3 = u'起動しました　ようそこ録画機へ/リターンコード:'
s4 = u'現在起動処理しています/リターンコード:'
s5 = u'問題発生/リターンコード'


res = subprocess.call(["ping", "192.168.1.4", "-c1", "-W2", "-q"], stdout=open('devnull', 'w'))

if res is not 1:
  sys.stdout.write(s1)
  sys.stdout.write(str(res))
  print("")
else:
  setIo = 26
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(setIo, GPIO.OUT)
  for i in range(1):
      GPIO.output(setIo, GPIO.HIGH)
      sleep(0.05)
      GPIO.output(setIo, GPIO.LOW)
      GPIO.cleanup()
  print(s2)
  sleep(5)
  for f in range(30):
    res = subprocess.call(["ping", "192.168.1.4", "-c1", "-W2", "-q"], stdout=open('devnull', 'w'))
    sleep(1)
    if res is not 1:
      sys.stdout.write(s3)
      sys.stdout.write(str(res))
      sleep(5)
      print ('')
      sys.exit()
    else:
      sys.stdout.write(s4)
      sys.stdout.write(str(res))
      print ('')
if res is 1:
  print ('問題があります、長押しますか？')
  inputWord = raw_input('yで長押し  ')
  if inputWord is 'y':
    print ('長押しコマンド発行中')
    GPIO.output(setIo, GPIO.HIGH)
    sleep(4)
    GPIO.output(setIo, GPIO.LOW)
    GPIO.cleanup()
  else:
    print('起動しませんでした')
