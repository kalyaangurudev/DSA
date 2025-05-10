def reverse(st):
    rev_st = st[::-1]
    t = 0
    temp = []
    st_output = []
    for i in range(len(rev_st)):
        if t==0 and rev_st[i]!=' ':
            temp.append(rev_st[i])
        else: 
            t1 = (''.join(temp[::-1])) + " "
            temp = []
            st_output.append(t1)
    t1 = (''.join(temp[::-1])) + " "
    st_output.append(t1)
    st_output1 = ''.join(st_output)
    return st_output1

st = ['h','i',' ','h','o','w',' ','r',' ','u']
print(reverse(st))