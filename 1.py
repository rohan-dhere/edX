# baisc loops
i = 2
while i<=10:
    print(i)
    i += 2
print('Goodbye!')

for x in range(2,11,2):
 print (x)   
print('Goodbye!')


#counts up the number of vowels
vow = 0
for i in s :
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'): #filter vowels
        vow = vow + 1
print('Number of vowels: ',vow)


#number of times the string 'bob' occurs
count = 0 
for index,i in enumerate(s):
    if (i == 'b' and index < (len(s)-2) ): #if B is the 3rd last element in string
        if (s[index+1] =='o' and s[index+2] =='b'): #check B+1 position == o and B+2 position =B 
            count = count+1
            
print('Number of times bob occurs is: ', count)



#longest substring in which the letters occur in alphabetical order. 
substring = '' 
tmp = ''
for i in range(len(s)):
    tmp = tmp + s[i]
    if len(tmp) > len(substring): #if current substring is larger then replace old with new
        substring = tmp
    if i > len(s)-2: 
        break
    if s[i] > s[i+1]: #current letter is before or after of next letter in alphabets 
        tmp = ''

print("Longest substring in alphabetical order is: ", substring)
