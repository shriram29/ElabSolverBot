import pyautogui
import time as t
import random as r
import csv
from os import system, name
import win32clipboard
from PIL import ImageGrab, ImageOps
import numpy as np
import mysql.connector
from mysql.connector.errors import Error

complete=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
question=(91,505)
urlc=(474,44)
sour=(1200,625)


dbcon = mysql.connector.connect(
  host="localhost",
  user="", #use your credentials
  passwd="",#use your credentials
  database="elab"
)
elabdb= dbcon.cursor()



def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


def url(x):
    add="http://care.srmuniv.ac.in/rmpcseos/login/student/code/operating-systems/operating-systems.code.php?id=1&value="+str(x)
    pyautogui.click(urlc[0],urlc[1])
    pyautogui.typewrite(add)
    pyautogui.press('enter')
    t.sleep(1)
    while 1:
        t.sleep(.5)
        box=(22,6,33,21)
        img=ImageGrab.grab(box)
        img=ImageOps.grayscale(img)
        a=np.asarray(img.getcolors())
        if a.sum()==757:
            break

def reader():
    pyautogui.doubleClick(question[0],question[1])
    pyautogui.hotkey('ctrl','c')
    win32clipboard.OpenClipboard()
    qno = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.click(sour[0],sour[1])
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    win32clipboard.OpenClipboard()
    code = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    sql = "INSERT INTO questions (id, code) VALUES (%s, %s)"
    val=(qno,code)
    try:
        elabdb.execute(sql,val)
        dbcon.commit()
        return None
    except  mysql.connector.Error as e:
        return None


def completed():
    for i in range(0,100):
        complete.append(1)
    x=0
    system("cls")
    print("=== Which Questions are incomplete ? ===")
    print("Section:")
    print("   11 - Done !")
    print("Question:")
    print("   11 - All questions in this Section")
    print("   12 - Wrong Section :( Continue ==> ")

    while x!=11:
        x=int(input("Enter Section :"))
        if x==11:
            break
        while 1:
            y=int(input("In Section "+ str(x) +" enter question :"))
            if y==11:
                for i in range(0,10):
                    complete[(x-1)*10+i]=0
                break
            elif y==12 :
                break
            elif 0<=y & y<=9:
                complete[(x-1)*10+y]=0
    system("cls")


for i in range(0,100):
    if complete[i]!=0:
        print("Accesing Que "+str(i) )
        url(i)
        reader()
