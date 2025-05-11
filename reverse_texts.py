def reverseWords(arr):
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(arr)
    
    # Step 1: Reverse the entire array
    reverse(0, n - 1)

    # Step 2: Reverse each word
    start = 0
    while start < n:
        if arr[start] == ' ':
            start += 1
            continue
        end = start
        while end < n and arr[end] != ' ':
            end += 1
        reverse(start, end - 1)
        start = end

# Example usage
arr = list("perfect makes practice")
reverseWords(arr)
print(''.join(arr))  # Output: "practice makes perfect"

# ------------------------------------My code ----------------------------
# def reverse(st):
#     rev_st = st[::-1]
#     t = 0
#     temp = []
#     st_output = []
#     for i in range(len(rev_st)):
#         if t==0 and rev_st[i]!=' ':
#             temp.append(rev_st[i])
#         else: 
#             t1 = (''.join(temp[::-1])) + " "
#             temp = []
#             st_output.append(t1)
#     t1 = (''.join(temp[::-1])) + " "
#     st_output.append(t1)
#     st_output1 = ''.join(st_output)
#     return st_output1

# st = ['h','i',' ','h','o','w',' ','r',' ','u']
# print(reverse(st))