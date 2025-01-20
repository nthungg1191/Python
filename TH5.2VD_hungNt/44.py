import numpy as np 
b = np.array([(1,2,3,4),
              (-2,-1,4,1),
              (3,-4,-5,6),
              (1,2,3,4)])
print('Ma tran b:\n',b)
det_b=np.linalg.det(b)
print('det(b)=  ', det_b)