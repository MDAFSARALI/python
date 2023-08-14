class C_2d_vector:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C_3d_vector(C_2d_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
v2d=C_2d_vector(1,3)
v3d=C_3d_vector(1,9,5)
print (v2d)
print (v3d)