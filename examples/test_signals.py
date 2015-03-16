import sys
import time

sys.path.append('../')

from LocationApi import *

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0 or (len(args) > 0 and "test" == args[0]): 
        print (getSignalfor("EMC Guest Cafe", "Pivotal", "CORP-W1F1"))
    elif "trace" == args[0] and len(args) > 1:
        while True: 
            time.sleep(3)
            print getSignalfor(args[1])