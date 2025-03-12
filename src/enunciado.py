def buscarPalabra(objetivo, palabras,):
    for palabra in palabras : 
        if palabra == objetivo:
            return True
    return False




nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]

edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}


while True:
    nombre = input("Buscar un nombre: ")
    estaElnombre = buscarPalabra(nombre, nombres)

    if estaElnombre == True:
        print(estaElnombre ,"tiene", edades)
    else:
        print("El nombre no existe")

        




   




        


 




    






