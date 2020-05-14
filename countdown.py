import time
import subprocess

start = 10

for i in range(1, start+1):
  print(i)
  time.sleep(1)

# Un while est peut être plus adapté

subprocess.Popen(['C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe', 'C:\\Users\\noesa\\Desktop\\telephone-ring-01a.wav'])
