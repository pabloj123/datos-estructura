def fibona(n): # definimos mi  funcion  con (n)
    if n >= 0: #  verifica si el valor de n es mayor o igual a cero.
        print("tabla(", n, ") = ", fibona1(n)) # esta función devuelve el valor del n
        fibona(n - 1) # a esto se lo conoce  recursiva  fibona(n - 1) se llama a sí misma con n - 1 como argumento. esto significa que la función
        #se ejecutará nuevamente

def fibona1(n): # definimos otra funcion para los siguientes pasos
    if n in (0, 1): # si n es 0 o 1, la función devuelve directamente el valor de n esto maneja los casos base de la serie
        return n  #si n es igual a 0 o 1 (se cumple la condición anterior)
    else:
        return fibona1(n - 1) + fibona1(n - 2)# i n no es 0 ni 1, entonces el valor de fibonacci para n es la suma de los valores

# el usario igresa el numero 
numero = int(input("Ingrese un número para generar la serie : "))

# imprime la serie  y hacemos llamar la variable numero 
print("Serie ", numero, "números:")
fibona(numero)