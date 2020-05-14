def anagrams(word, words):
    d={}
    l=list(words)
    print(l)
    if len(word)==len(words):
        count_equal=len(word)
        for i in range(len(word)):
            for j in range(len(l)):
                if word[i]==l[j]:
                    l[j]='*'
            
                    
        print(l)
        for i in l:
            if i=='*':
                count_equal-=1
        if count_equal==0:
            return True
        else:
            return False
print(anagrams('aabb','bbaa'))
            
                   

