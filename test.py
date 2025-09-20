import numpy as np;

a = np.random.randn(1,3);

b = np.random.randn(3,3);

c = a * b;

#print (c.shape);


k = np.array([[1,1],[1,-1]]);

l = np.array([[2],[3]]);

d = a + b;

print (d);



A = np.random.randn(4,3)

B = np.sum(A, axis = 1, keepdims = True) 

print (B.shape)
