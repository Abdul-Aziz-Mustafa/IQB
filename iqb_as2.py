key =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
a_v =[1.45,0.77,0.98,1.53,1.12,0.53,1.24,1,1.07,1.34,1.2,0.73,0.59,1.17,0.79,0.79,0.82,1.14,1.14,0.61]
b_v=[0.97,1.30,0.80,0.26,1.28,0.81,0.71,1.6,0.74,1.22,1.67,0.65,0.62,1.23,0.9,0.72,1.2,1.65,1.19,1.29]

alpha = dict(zip(key,a_v))   
beta = dict(zip(key,b_v))     

def a_score(seq):  
    a_s= 0
    la = len(seq)
    for i in range(la):  
        a_s += alpha[seq[i]]
    return a_s

#!-------------------------------------------------------------------------------------------------!#
def b_score(seq):  
    b_s = 0
    lb = len(seq)
    for i in range(lb):     
        b_s += beta[seq[i]]
    return b_s

#!-----------------------------------------------------------------------------------------------#!
def high_p_a_val(i,p_val):
    n = 0
    for j in range(i, i+p_val):
        if a_score(seq[j]) >= 1:
            n += 1
    return n  

def high_p_b_val(i,p_val):
    n = 0
    for j in range(i, i+p_val):
        if b_score(seq[j]) >= 1:
            n += 1
    return n            
#!--------------------------------------------
def extend_a(arr,p1,p2,length_seq): 
    while p1 < length_seq:
        if a_score(seq[p1-3:p1+1]) >= 4:
            arr[p1] = 'H'
        else:
            break
        p1 += 1
    while p2 >= 0:
        if a_score(seq[p2:p2+4]) >= 4:
            arr[p2] = 'H'
        else:
            break
        p2 -= 1
#!-------------------------------------------
def extend_b(arr,p1,p2,length_seq):
    while p1 < length_seq:
        if b_score(seq[p1-3:p1+1]) >= 4:
            arr[p1] = 'S'
        else:
            break
        p1 += 1
    while p2 >= 0:
        if b_score(seq[p2:p2+4]) >= 4:
            arr[p2] = 'S'
        else:
            break
        p2 -= 1 

#!-------------------------------------------------------------------------------------------------!#

def alfa_f_helix(seq): 
    if_helix = []
    ll=len(seq)
    for i in range(ll):
        if_helix.append('_')
    if ll <= 5:
        print("wrong sequence")
        return
    for i in range(ll-5):
        n=high_p_a_val(i,6)
        if n >= 4:
            for j in range(i, i + 6):
                if if_helix[j] != 'H':
                    if_helix[j] = 'H'
            p1 = i+6
            p2 = i-1
            extend_a(if_helix,p1,p2,ll)
   
    alpha_helix = ""
    for i in range(len(if_helix)):
        alpha_helix += if_helix[i]
    return alpha_helix


#!-------------------------------------------------------------------------------------------------!#
def beta_f_sheet(seq): 
    if_beta = []
    ll=len(seq)
    for i in range(ll):
        if_beta.append('_')
    if ll < 5:
        print("Sequence length must be atleast 5 for this algorithm to work")
        return
    for i in range(ll-4):
  
        n=high_p_b_val(i,5)

        if n >= 3:
            for j in range(i, i+5):
                if if_beta[j] != 'S':
                    if_beta[j] = 'S'
            p3 = i+5
            p4 = i-1
            extend_b(if_beta,p3,p4,ll)
    
    b_sheet = ""
    for i in range(len(if_beta)):
        b_sheet += if_beta[i]
    return b_sheet

#!------------------------------------------------------------
def fun(seq1,seq2,seq,res):
    ll=len(seq)
    i=0
    while i < ll:
        if (seq1[i] == 'H' and seq2[i] == '_') or (seq1[i] == '_' and seq2[i] == 'H'):
            res[i] = 'H'
            i += 1
        elif (seq1[i] == '_' and seq2[i] == 'S') or (seq1[i] == 'S' and seq2[i] == '_') :
            res[i] = 'S'
            i += 1
        elif seq1[i] == '_' and seq2[i] == '_':
            res[i] = '-'
            i += 1
        else:
            n = 0
            while (seq1[i] == 'H' and seq2[i] == 'S') or (seq1[i] == 'S' and seq2[i] == 'H'):
                n += 1
                if i < ll-1:
                    i += 1
                else:
                    break
            if i == ll-1:
                i += 1 
            p1 = a_score(seq[i-fn:i])
            p2 = b_score(seq[i-n:i])
            if p1 > p2:
                for k in range(i-n,i):
                    res[k] = 'H'
            else:
                for k in range(i-n,i):
                    res[k] = 'S'
    return res                
    

#!-----------------------------------------------------------------------------------------!#
def conflict_case(seq1, seq2, seq):  
    result = []

    ll=len(seq)
    for i in range(ll):
        result.append("")
    fun(seq1, seq2, seq,result)
    i = 0
    ans = ""
    for i in range(len(result)):
        ans += result[i]
    return ans

#!------------------------------
def cmpr():
    print("The region of difference is denoted by '^': ")
    our = "-HHHHHHHHHHHSSSSSSSSSSSSSSHHHHHHHHHSSSSHHHHHHHHHHHH--HHHHHHHHHHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS----HSSSSSSSSSSSSSSSSSSSSS--SSSSSSSSSS---HHHHHH---------"
    web = "TTTT     HHHHHH EEEEEETTEEEEEEEETTEEEEEGGGG  HHHHH   HHHHHHH  GGG EEEETTEEE EEEEEEETTEEEEEE   TTTT        TTTEEEEEEEEETTEEEEEEEEEETTTT B    TTTTTTTEE "
    print(our)
    print(web,end="\n")
    i=0
    ll=len(our)
    while(i<ll):
        if our[i]==web[i]:
            print(our[i], end = "")
        elif our[i]=="S" and web[i]=="E":
            print("S", end = "")
        else:
            print("^", end = "")
        i+=1
   
    print(end="\n")
#!--------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    seq = "SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF" # INPUT SEQUENCE
    seq1 = alfa_f_helix(seq)  
    seq2 = beta_f_sheet(seq)  
    final_seq = conflict_case(seq1, seq2, seq)  

    print(seq)
    print(final_seq)
    cmpr()