import threading, time

print('Start of program.')

def takeANap():
  time.sleep(5)
  print('Wake up!')

# threadObj = threading.Thread(target=takeANap)
# threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep='&' ))
# threadObj_1 = threading.Thread(target=print, args=('Cats', 'Cats', 'Cats'), kwargs={'sep':'&'})
# threadObj.start()
# threadObj_1.start()
# print('End of program.')

import numpy as np

print(np.mean(a=[0.31, 0.51, -0.01, -0.22, -0.34]))