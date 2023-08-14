def rec_sum(k):
    if k==0: 
        return 0
    return (k +rec_sum(k-1))

f=rec_sum(1)
print (f)

# instead of using this we can also replace by this condition 
#  if k==1: 
        # return 1
    # return (k +rec_sum(k-1))