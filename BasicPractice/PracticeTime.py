import time;
import calendar
from datetime import date

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#Calander

print ("Calander for Aug 1947")
cal = calendar.month(1947, 8)
print ("Here is the calendar:")
print (cal)
