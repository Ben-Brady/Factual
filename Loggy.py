from datetime import timezone
import datetime

# Getting the current date  
# and time

def GetTime():
    dt = datetime.datetime.now()
    utc_time = dt.replace(tzinfo = timezone.utc)
    return(utc_time.timestamp())


Query = (input ("Would you like to log?(Y/N)")).lower()

if Query == "y":
    Log = ("Log-"+str(GetTime()))
    def Add(message):
        print (message)
        f = open("Logs/"+str(Log), "a")
        f.write('\n'+str(GetTime())+": "+message)
        f.close()
        return

if Query == "n":
    def Add(message):
        print (message)
        return