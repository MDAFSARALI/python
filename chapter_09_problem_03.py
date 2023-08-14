# a=int (input("you need the multiplication table of\n"))
# for i in range (1,11):
#     print (f"{a}X{i}={a*i}")

    #Q)CODE by HARRY:
for i in range (2,20):
    with open (f"tables/Multiplication_table_of_{i}.txt",'w') as f:
        for j in range (1,11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')
