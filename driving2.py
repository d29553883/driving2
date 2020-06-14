country = input('哪國人')
age = input('幾歲 :')
age = int(age)
if country == '台灣': 
   if age >= 18 :
   	   print('你可以考駕照')
   else:
   	   print('不能考駕照')
elif country == '美國':
   if age >= 16 :
       print('你可以考駕照')
   else :
       print('不能考駕照')

    