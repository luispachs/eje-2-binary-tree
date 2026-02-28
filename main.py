from bin import node

if __name__ == "__main__":
    print("seleccione una opcion")
    i = None
    tree = None
    print("1. Agregar un nodo")
    print("2. Eliminar un nodo")
    print("3. Buscar un nodo")
    print("4. Recorrer el arbol")
    print("5. Mostrar los que tienen dos hijos")
    print("6. Mostrar los que tienen un hijos")
    print("0. Salir")
    while i != 0:
        print("seleccione una opcion")
        try:
            i = int(input())
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue
        if i == 1:
            print("Ingrese el valor del nodo a agregar")
            try:
                value = int(input())
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            if tree == None:
                tree = node(value)
            else:
                tree.add(value)
        
        if i == 2:
            print("Ingrese el value a eliminar")
            try:
                value = int(input())
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            tree.delete(tree,value)
        if i == 3:
            print("ingrese el valor a buscar")
            try:
                value = int(input())
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            print("\nEl camino es:\n")
            tree.search(tree,value)
        if i == 4:
            print("Recorriendo inorder")
            tree.inorder(tree)
        if i == 5:
            print("mostrando los que tienen dos hijos")
            tree.showTwoChild(tree)
        if i == 6:
            print("mostrando los que tienen un hijo")
            tree.showOneChild(tree)
        if i == 7:
            print("Sumar Hijos")
            tree.sumChild(tree)
        if i == 0:
            break
    print( "Bye")