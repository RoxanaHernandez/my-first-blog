class Empleado():
    nombre = ""
    apellido=""
    sueldo=""


    def __init__(self):
        self.nombre=input("Ingrese su nombre:")
        self.apellido=input("Ingrese su apellido:")
        self.sueldo=int(input("Ingrese su sueldo:"))

    def imprimirDatos(self): 
        return f"Nombre:{self.nombre}  Apellido: {self.apellido}  Sueldo: {self.sueldo}"

    
    def pagarImpuesto(self):
        if self.sueldo > 3000:
            print("Pagas Impuesto")
        else:
            print("Libre de Impuesto")

empleado=Empleado()  
empleado.imprimirDatos()
empleado.pagarImpuesto()  








    
     
    

    
  

        
    
