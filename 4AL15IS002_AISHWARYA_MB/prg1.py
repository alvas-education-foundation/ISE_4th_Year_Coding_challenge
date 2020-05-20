# Remote logger module
# Code to add with local python scripts
import urllib.parse , urllib.request
import argparse
import time
import requests

def sendLog2Server(line, sfileName):
    print(line)
    mydata = {'log': line, 'sFName': sfileName}
    resp = requests.post('<api-link>', data=mydata)
    print(resp.text)

def checkLogFile():
    pass

def readLastLine(fileName):
    with open(fileName, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        return last_line

def main(args):
    prev_line = ''
    sleepTime = args.sec if args.sec!=0 else (args.min*60 if args.min!=0 else args.hrs*60*60)
    #time.sleep(2)
    for x in range(0,args.runTime*60*60,sleepTime):
        last_line = readLastLine(args.fileName)
        if prev_line != last_line:
            try:
                sendLog2Server(last_line, args.serFName)
            except Exception as e:
                raise e
            finally:
                prev_line = last_line
        print("Waiting for {} seconds in {}/{}".format(sleepTime,x,args.runTime*60*60))
        time.sleep(sleepTime)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="send logs to remote server")
    parser.add_argument('--sec', type=int, default=0, help='Time in Seconds')
    parser.add_argument('--min', type=int, default=0, help='Time in Minutes')
    parser.add_argument('--hrs', type=int, default=0, help='Time in Hours')
    parser.add_argument('--runTime', type=int, default=0, help='Total run time in HRS')
    parser.add_argument('--fileName', type=str, default='log.txt', help='Log file name')
    parser.add_argument('--serFName', type=str, default='syslog.txt', help='Server Log file name')
    args = parser.parse_args()
    main(args)