try:
   f = open("test.txt", mode = 'r', encoding = 'utf-8')
   text = f.read()
   print(text)   
finally:
   f.close()
