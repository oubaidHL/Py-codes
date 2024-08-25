'''
Created on 26 janv. 2022

@author: hlaimi_oubaid
'''
from test.datetimetester import SEC
from test._test_multiprocessing import identity

def printing(length,width):
    print("hello word")
    print(5+7)
    print("5"+"7")
    area=length*width
    print("the area of the triangl is :"+ str(area))

def greeting (name):
    print("welcom "+(name)+" your are the best ever !!")


def area_triangle(widht,hight):
    return widht*hight/2

#triangle_a=area_triangle(34, 34)
#triangle_b=area_triangle(2, 3)
#sum=triangle_a+triangle_b
#print("the sum of the areas to the tow triangles is : "+ str(sum))

def convert_second_V1(sec):
    hours=sec//3600
    minutes=(sec- hours*3600)//60
    seconds=(sec-hours*3600-minutes*60)
    return hours,minutes,seconds


def convert_second_V2(sec):
    hours=sec //3600
    sec%=3600
    minutes=sec//60
    sec%=60
    return hours,minutes,sec


#hours,minutes,seconds=convert_second_V1(11000)
#print("hours: "+str(hours)+" ,minutes: "+str(minutes)+" ,seconds: "+str(seconds))

#hours,minutes,seconds=convert_second_V2(11000)
#print("hours: "+str(hours)+" ,minutes: "+str(minutes)+" ,seconds: "+str(seconds))


def identity ():
    name=input("ur name !")
    nationality=input("ur nationality bro !")
    age =int(input("ur age !"))
    if age<=18:
        print("u are fucking kid")
    else:
        print("ur are man now u should be take ur postion in this life ma nigga !")
    

#identity()

def is_even(number):
    if number%2 ==0 :
        return True
    else :
        return False
    
#print(is_even(33))

#---------------------------------First_day---------------------------------------------------



