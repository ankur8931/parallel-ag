#!/use/bin/python

import threading
import time
import os
import sys
os.environ['MULVALROOT'] = "/root/Downloads/mulval/"
os.environ['XSB'] = "/root/Downloads/XSB/"
os.environ['PATH'] +=os.pathsep+'/root/Downloads/XSB/utils'
os.environ['PATH'] +=os.pathsep+'/root/Downloads/XSB/bin'
os.environ['PATH'] +=os.pathsep+'/root/Downloads/mulval/utils'
os.environ['PATH'] +=os.pathsep+'/root/Downloads/mulval/bin'




count = 1
path ="../data/testcases/after/"
files=["20after.P","40after.P","60after.P","80after.P","100after.P","120after.P","140after.P","160after.P","180after.P","200after.P","250after.P","300after.P","350after.P","400after.P","450after.P","500after.P"]


def createSubAG(count, filename):
   print("Thread-"+str(count))
   os.system("/root/Downloads/mulval/utils/graph_gen.sh "+ path+filename +" -v -p")
      

##main function####

if __name__ == "__main__": 
    # creating thread 
   tname = list()

   for filename in files:
       tname.append(threading.Thread(target=createSubAG, args=(count, filename,))) 
       count=count+1

   start_time = time.time() 
   for i in range(len(tname)):
       # starting thread 1 
       tname[i].start() 
      # wait until thread 2 is completely executed 
       tname[i].join() 
   
   print"Runtime:",(time.time()-start_time) 

