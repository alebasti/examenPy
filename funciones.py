def menu():
    print("-"*35)
    print("\t    Casa Feliz")
    print("-"*35)
    print("1)Comprar departamento")
    print("2)Mostrar departamentos disponibles")
    print("3)Ver listado de compradores")
    print("4)Mostrar ganancias totales")
    print("5)Salir")
    return validanum(int,"Ingrese una opcion: ",1,5)

def validanum(type,text,min=None,max=None):
    while True:
        try:
            num=type(input(text))
            if min!=None and max!=None:
                if min<=num<=max:
                    break
                else:
                    print(f"Debe ingresar un numero entre {min} y {max}")
            elif min!=None:
                if min<=num:
                    break
                else:
                    print(f"El numero ingresado debe ser mayor o igual a: {min}")
            elif max!=None:
                if num<=max:
                    break
                else:
                    print(f"el numero ingresado debe ser menor o igual a: {max}")
            else:
                break
        except:
            print("error. Se esperaba un numero")      
    return num

def validartipo():
    while True:
        tipo=input("Ingrese Tipo de departamento (A - B - C - D): ").upper()
        if tipo=="A" or tipo=="B" or tipo=="C" or tipo=="D":
            break
        else:
            print("Tipo de departamento invalido.")
    return tipo

def mostrardpto(departamentos):
    print("-"*20)
    print("Piso|\tTipo")
    print("-"*20)
    print("     A   B   C   D")
    num=11
    for f in range(10):
        num=num-1
        print(f"|{str(num).ljust(2)}|", end="")
        for c in range(4):
            if len(departamentos[f,c])==0:
                print(f"{str(departamentos[f,c]).ljust(3)}|",end="")
            else:
                print(f" X |",end="")            
        print("|")        
        

def validavacio(departamento, departamentos):
  cont=0
  flag=False
  for f in range(10):
    for c in range(4):
      cont+=1
      if departamento==cont:
        if len(departamentos[f,c])==0:
          flag=True
          break
        else:
          break
    if flag:
      break 
  if flag:
    return(f,c)
  else:
    return(-1,-1)
  


def comprardpto(departamentos,compradores,ventas):
    comprador = validanum(int,"Ingrese su rut sin guion y sin digito verificador: ",5000000,90000000)
    while True:
        dpto=validanum(int,"Ingrese N° de de piso (entre 1-10): ",1,10) 
        letra=validartipo()
        print("-"*43)
        print(f"Departamento seleccionado: {letra}{dpto}")
        resta=0
        num=0
        venta=letra
        if letra=="A":
            resta=3
        elif letra=="B":
            resta=2
        elif letra=="C":
            resta=1
        else:
            resta=0
        if dpto==1:
            num=40
        elif dpto==2:
            num=36
        elif dpto==3:
            num=32
        elif dpto==4:
            num=28
        elif dpto==5:
            num=24
        elif dpto==6:
            num=20
        elif dpto==7:
            num=16
        elif dpto==8:
            num=12
        elif dpto==9:
            num=8
        elif dpto==10:
            num=4
        departamento=num-resta
        f,c=validavacio(departamento,departamentos)
        if f==-1 and c==-1:
            print("No está disponible")
        else:
            break            
    if letra=="A":
        valordpto = 3800
    elif letra=="B":
        valordpto = 3000
    elif letra=="C":
        valordpto = 2800
    else:
        valordpto = 3500
    
    print(f"Valor del departamento: ${valordpto} UF")   
    ventas.append(venta)      
    compradores.append(comprador)
    departamentos[f,c]=departamento
    print("Departamento comprado con exito") 
    print("-"*43)      

    return departamentos, compradores , ventas
    
def mostrarcompradores(compradores):
   compradores.sort()
   print(compradores)

def calcularprecios(ventas):
    total=0
    cont1,cont2,cont3,cont4=0,0,0,0
    for f in range(len(ventas)):
        if "A" in ventas[f]:
            total += 3800
            cont1 += 1
        elif "B" in ventas[f]:
            total += 3000
            cont2 += 1
        elif "C" in ventas[f]:
            total += 2800
            cont3 += 1
        else:
            total += 3500
            cont4 += 1

        
    print("-"*43)
    print("Tipo de departamento\t  Cantidad\tTotal")
    print("-"*43)
    if cont1>0:
        print(f"A 3800 UF\t\t\t{cont1}\t${cont1*3800}")
        print("-"*43)
    if cont2>0:
        print(f"B 3000 UF\t\t\t{cont2}\t${cont2*3000}")
        print("-"*43)
    if cont3>0:
        print(f"C 2800 UF\t\t\t{cont3}\t${cont3*2800}")
        print("-"*43)
    if cont4>0:
        print(f"D 3500 UF\t\t\t{cont4}\t${cont4*3500}")
        print("-"*43)
    print(f"Total\t\t\t\t{cont1+cont2+cont3+cont4}\t${total}")

def salir():
   print("Alejandro Espinoza")
   print("12-10-2023")
   print("Cerrando el programa...")