def crea_cronologia(a, b):
   output=a+" "+str(b)
   cronologia_list.append(output)

def vedi_cronologia(numero, testo_input):
   while(numero=="cronos"):
      if cronologia_list==[]:
         print("Nessuna cronologia")
      else:
         print(f"{'*'*34}\nCronologia:")
         for i in cronologia_list:
               print(i)
         print(f"{'*'*34}")
      numero=input(testo_input)
   return numero

def def_tipo(x):
   if float(x)-int(float(x)) == 0:
      x=int(x)
   else:
      x=float(x)
   return x

cronologia_list=[]
if __name__=="__main__":
   print("Calcolatrice\n(per visualizzare la cronologia scrivi 'cronos')\n0")
   numero1=input("Inserisci un numero:\n")
   numero1=vedi_cronologia(numero1, "Inserisci un numero:\n")
   numero1=def_tipo(numero1)
   while(1):#
      operazione=input("+\t-\t x(*)\t /\n")
      operazione=vedi_cronologia(operazione, "+\t-\t x(*)\t /\n")
      numero2=input("Inserisci un numero:\n")
      numero2=vedi_cronologia(numero2, "Inserisci un numero:\n")
      numero2=def_tipo(numero2)
      testo=f"{numero1} {operazione} {numero2} ="
      print(f"\n{testo}")
      match operazione:
         case "+":
               numero1+=numero2
         case "-":
               numero1-=numero2
         case "x" | "*":
               numero1*=numero2
         case "/":
               if numero2==0:
                  print("Non puoi dividere per 0")
               else:
                  numero1/=numero2
      numero1=def_tipo(numero1)
      print(f"{numero1}\n")
      crea_cronologia(testo, numero1)