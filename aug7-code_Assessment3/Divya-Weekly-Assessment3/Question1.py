import multiprocessing
import logging
logging.basicConfig(filename = "MultiProcessing" ,level=logging.DEBUG)
list= [1,11,2,22,3,33,4,44,5,55,6,66,7,77,8,88,9,99]
def even(getlist):
    for i in getlist:
        if i%2==0:
            print("the even numbers are:",i)
        
def odd(getlist):
    for j in getlist:
        if j%2==1:
            print("the odd numbers are: ",j)
try:

    if (__name__)=='__main__':
        p1=multiprocessing.Process(target=even,args=(list,))
        p2=multiprocessing.Process(target=odd,args=(list,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("Loading.....")
        logging.info("Even and Odd numbers printed Successfully using Multi Processing")
except:
    logging.error("something went wrong")
finally:
    print("Good Job")