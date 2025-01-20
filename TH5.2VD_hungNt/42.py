import numpy as np 
a = np.array([(1,3,1,4),
              (3,9,5,15),
              (0,2,1,1),
              (0,4,2,3)])
print('Ma tran a:\n',a)
det_a = np.linalg.det(a)
print('det(a)=  ', det_a)