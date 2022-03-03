import math

print("Enter the Plain Text Messsage M: ")
M = input()
M = M.replace(" ", "")
M = M.lower()

print("Enter the key word w: ")
w = input()
w = w.lower()

# Encryption
def encryptMessage(M):
    C = ""
    w_indx = 0
    M_len = float(len(M))
    M_lst = list(M)
    w_lst = sorted(list(w))
    
    k = len(w)
    
    row = int(math.ceil(M_len / k))
    
    fill_space = int((row * k) - M_len)
    M_lst.extend('X' * fill_space)  
    
    matrix = [M_lst[i: i + k]
            for i in range(0, len(M_lst), k)]
            
    for X in range(k):
        current_idx = w.index(w_lst[w_indx])
        C += ''.join([row[current_idx]
                        for row in matrix])
        
        w_indx +=1
    
    return C
    
# Driver Code
C = encryptMessage(M)
print("The plain text M is ", M)
print("The key word w is ", w)
print("Encrypted Message: {}".
        format(C))
