print("1 - soma\n")
print("2 - subtração\n")
print("3 - multiplicação\n")
print("4 - divisão\n\n")
c = int(input(" "))
import os
os.system('clear') or None
a = int(input("Digite o primeiro numero\n"))
b = int(input("Digite o segundo numero\n\n"))
if c == 1:
    print(a + b)
         
elif c == 2:
	print(a - b)
	
elif c == 3:
    print( a * b)
    
else:
    try:
      print(a / b)
      
    except:
        print("Não é possível fazer a divisão\n")