import random
import numpy as np

# Q = list(np.random.randint(-5, 5, size=7))
# j = random.randint(-5, 5)

# print('Q list : %s' % Q)
# print('j list : %s' % j)

Q = [-2, -5, -4, 0, -1, -1, -4]
j = 4
print('Q list : %s' % Q)
print('j list : %s' % j)
for i in range(1, len(Q)+1):
    print('loop')
    if j in Q:
        print('j is in the list.')
        break
    elif (j+i and j-i) in Q:
        print((j+i or j+i) in Q)
        print(j, i, j+i)
        print(j-i in Q)
        print('j is in between %s and %s.' % ((j+i), (j-i)))
        break
    elif j+i > j-i and j+i in Q:
        print('j closest value in Q is : %s' % (j+i))
        break
    elif j-i < j+i and j-i in Q:
        print('j closest value in Q is : %s' % (j-i))
        print('j-i = ' + str(j-i))
        print('j+i = ' + str(j+i))
        break



# stop = 0
# while stop != 1:
#     Q = [-2, -5, -4, 0, -1, -1, -4]
#     j = 4
#     print('Q list : %s' % Q)
#     print('j list : %s' % j)
#     for i in range(1, len(Q)+1):
#         print('loop')
#         if j in Q:
#             print('j is in the list.')
#             #break
#         elif j+i and j-i in Q:
#             print('j is in between %s and %s.' % ((j+i), (j-i)))
#             #break
#         elif j+i > j-i and j+i in Q:
#             print('j closest value in Q is : %s' % (j+i))
#             #break
#         elif j-i < j+i and j-i in Q:
#             print('j closest value in Q is : %s' % (j-i))
#             print('j-i = ' + str(j-i))
#             print('j+i = ' + str(j+i))
#             #break
#     stop = 1
#     print('end')
