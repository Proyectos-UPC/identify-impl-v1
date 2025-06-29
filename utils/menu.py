from sistema import SistemaBiometrico

def ejecutar_menu():
    sistema = SistemaBiometrico()
    print("\nBienvenido a Identia")
    while True:
        print("\n1. Solicitar un proceso biométrico")
        print("2. Resolver proceso biométrico")
        print("3. Cobrar transacciones")
        print("4. Listar procesos biométricos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.solicitar_proceso()
        elif opcion == "2":
            sistema.resolver_proceso()
        elif opcion == "3":
            print("a. Listar transacciones")
            print("b. Pagar todas")
            print("c. Pagar individual")
            sub = input("Seleccione una opción: ")
            if sub == "a":
                sistema.listar_transacciones()
            elif sub == "b":
                sistema.pagar_todo()
            elif sub == "c":
                sistema.pagar_individual()
        elif opcion == "4":
            sistema.listar_procesos()
        elif opcion == "5":
            print("Gracias por usar Identia. Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
