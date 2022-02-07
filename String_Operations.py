#Pblm 1 - Write a program to count the numbers of characters in the string and store them in a dictionary data structure
# str=input("Enter String : ")
# f = {}
# for i in str: 
#     if i in f: 
#         f[i] += 1
#     else: 
#         f[i] = 1
# print(f)


#Pblm 2 - Write a program to use split and join methods.
# str = input("Enter the String : ")
# p = str.split()
# print(p)


# str = "Hii, My Name is Khushal, I am 19 years old studying in VIIT."
# x = str.split(", ")
# print(x)

# var1 = "Hello"
# var2 = "World"
# var3 = " ".join([var1,var2])
# print(var3)


#Pblm 3 -  Write a program to count frequency of characters in a given string.
# def count(s, c) :
# 	res = 0
# 	for i in range(len(s)) :
# 		if (s[i] == c):
# 			res = res + 1
# 	return res
	
# str= "Khushal"
# c = 'h'
# print(count(str, c))


#Pblm 4 - Find largest and smallest character in a given string.
# str = input("Enter the String : ")
# print(max(str))
# print(min(str))


#Pblm 5 - Write a while loop that starts at the last character in the string and works its way backwards to the first character in        the        string, printing each letter on a separate line.
# str = "Khushal"
# print(str[::-1])

# str = input("Enter the String : ")
# print ("The original string  is : ",str)   
# reverse_String = ""  
# count = len(str) 
# while count > 0:   
#     reverse_String += str[ count - 1 ] 
#     count = count - 1   
# print ("The reversed string using a while loop is : ",reverse_String)



#Pblm 6 - Write a function that counts the number of times given letter appears in a given string.
# def count(s, c) :
# 	res = 0
# 	for i in range(len(s)) :
# 		if (s[i] == c):
# 			res = res + 1
# 	return res
	
# str= input("Enter the String : ")
# c = input("Enter the alphabet whose frequency is to be counted : ")
# print(count(str, c))

#Pblm 7 - Write a function that that tells if a given substring appears in a given string

# def check(string, sub_str):
# 	if (string.find(sub_str) == -1):
# 		print("NO")
# 	else:
# 		print("YES")
			
# # driver code
# string = "Khushal"
# sub_str ="hal"
# check(string, sub_str)


#Pblm 8 - Write a function to compare 2 strings.


# def test(str1, str2):
#     if len(str1) == len(str2):
#         for i in range(0, len(str1)):
#             if str1[i] != str2[i]:
#                 return(i)
        
#         print(len(str1),len(str2))
#         return('Same')
#     else:
#         print(len(str1),len(str2))
#         return('Not same')

# print( test('Khushal', 'Khushal'))
# print( test('Khushal', 'Malu'))


#Pblm 9 -  Use string methods capitalize(), upper(), lower(),find(), strip(), startswith(), etc.
# str = input("Enter the String : ")
# print(str.capitalize())
# print(str.upper())
# print(str.lower())
# print(str.find('a'))
# print(str.startswith('k'))
# print(str.count(str))
# print(str.endswith('l'))


'''Pblm 10 - Take the following Python code that stores a string: str = 'X-DSPAM-Confidence:0.8475'.
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.'''

# str = 'X-DSPAM-Confidence:0.8475'
# k = str.find(':')
# print(k)
# p = str.find(' ', k)

# q = str[k+1:]
# r=float(q)
# print(r)


	







