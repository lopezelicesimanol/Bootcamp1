#Creamos la variable global y asignamos dentro
#de la funcion nuevo valor

name = "Imanol"

def use_global_value_in_function():
    global name
    name = "IMUX"
print("Name : " + name + " antes de modificarlo")

use_global_value_in_function()

print("Name : " + name )