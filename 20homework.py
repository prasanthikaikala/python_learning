#print all letter except vowels(continue)
 def except_vowel(c):
     new_str=c
     vowel=('a','e','i','o','u')
     for i1 in c.lower():
         if i1 in vowels:
             new_str=newstr.replace(i1,"")
     return new_str
