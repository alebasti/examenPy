import numpy as np
import funciones as fn


departamentos=np.empty([10,4], str)
compradores=[]
ventas=[]
op=0
while op!=5:
    op=fn.menu()
    if op==1:
        print("")
        fn.mostrardpto(departamentos)
        print("")
        departamentos,compradores,ventas=fn.comprardpto(departamentos,compradores,ventas)
    elif op==2:
        fn.mostrardpto(departamentos)
    elif op==3:
        fn.mostrarcompradores(compradores)
    elif op==4:
        fn.calcularprecios(ventas)
    else:
        fn.salir()
  