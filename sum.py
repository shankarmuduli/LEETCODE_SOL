class Solution:
    def backspaceCompare(self, S, T):
        
        if not S or not T:
            return False
        for i in range(len(S)):
            if S[i]=="#" and i>0: 
                
                S.replace(S[i-1],"")
        
        for j in range(len(T)):
            if T[i]=="#" and i>0:
                T.replace(T[i-1],"")
       
        if l==m:
            return True
        return False
        

            
        
                
            

r=Solution()
print(r.backspaceCompare("ab#c","ad#c"))

