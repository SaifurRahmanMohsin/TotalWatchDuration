import os
import sys
import commands
from datetime import datetime

dir = sys.argv[1]
extensions = ['.mp4','.avi','.wmv','.mov','.mkv','.webm']
exts = tuple(extensions)
count = 0
sum = 0

for path, subdirs, files in os.walk(dir):
    for name in files:
        if name.endswith(exts):
            count = count + 1
            # print '/usr/local/bin/ffmpeg -i "%s" 2>&1 | grep Duration | cut -d \' \' -f 4 | sed s/,//' % os.path.join(path, name)
            (status,value)=commands.getstatusoutput('/usr/local/bin/ffmpeg -i "%s" 2>&1 | grep Duration | cut -d \' \' -f 4 | sed s/,//' % os.path.join(path, name))
            time=datetime.strptime(value, '%H:%M:%S.%f')
            hours=time.hour
            minutes=time.minute
            seconds=time.second
            totalSeconds=(seconds)+(minutes*60)+(hours*3600)
            sum += totalSeconds

avSeconds=sum
avMillis=sum-(avSeconds);

avMinutes=avSeconds/60;
avSeconds=avSeconds-(avMinutes*60);

avHours=avMinutes/60;
avMinutes=avMinutes-(avHours*60);

finalDuration=''
if avHours > 0:
    finalDuration += "%s hours, " % avHours

if avMinutes > 0:
    finalDuration += "%s minutes" % avMinutes

if avSeconds > 0:
    finalDuration += " and %s seconds" % avSeconds

print count
print finalDuration

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("Total Duration Found (%d files processed)" % count, "The total duration is %s" % finalDuration)
