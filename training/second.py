'''
Created on 27 janv. 2022

@author: oubaid hlaimi
'''



#-----------------while with the easy way------------------
def repeat (n):
    c=1
    while n>=c :
        print(c)
        c+=1
#repeat(int(input("donner votre : c")))



#-----------------for 3 version's---------------

def for_V1(n):
    for i in range(n):
        print("i love u " + str(i))

def for_V2(n):
    for i in range(n-5,n):
        print("i love u more than u think "+str(i))

def for_V3(n):
    for i in range (n-5,n,2):
        print("it means a world to me " +str(i))

#for_V1(20)
#for_V2(20)
#for_V3(20)
#-----------------liste-------------
def liste_V1 (liste):
    for i in liste:
        if i%2==0 :
            print("found a even number : "+str(i))
            continue
        print("found a number :" +str(i))  
          
#liste=[1,20,3,4,50,6]
#liste_V1(liste)
#----------------------------------------


