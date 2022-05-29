int_val, str_val_one , str_val_two, float_number = 1,"333", "AA", 2.12

#variable con texto
print("Primer texto: " + str_val_one)

#combinacion de dos varibles tipo texto
print(str_val_one+ str_val_two)  #333AA

#combinacion de dos varibles tipo numerico
print(int_val + float_number )  #3.22


#variables de tipo numerico y tipo string

print(str_val_one + str(float_number)) #"3332.22"
print("Ultimo texto: " + str(int_val)) # "ULTIMO TEXTO: 1"