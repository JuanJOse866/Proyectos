NOMBRE=(input("Ingresar su nombre completo: "))
SALDOACTUAL=2175000
FORMADERETIRO=int(input("Si espera retirar por cajero imprima el numero 1  "
                 "Si espera retirar por codigo presione el numero 2   Ingresar:  "))
if FORMADERETIRO==1:
    CAJERO=input("Selecciona tu banco 1.Banco de Bogota 2.Bancolombia 3.AV villas  ingresar: ")
    CONTRASEÑA=int(input("Ingresar contraseña: "))
    print("Su saldo actual es de: ", SALDOACTUAL)
    DINERO=int(input("Cuanto dinero desea retirar: "))
    if DINERO>SALDOACTUAL:
        print("No hay saldo suficiente")
        
    else:
        print("Su retiro se ha realizado exitosamente")
        SALDOACTUAL-=DINERO
        print("Saldo disponible: ", SALDOACTUAL)
else:
    CONTRASEÑA=int(input("ingresar su contraseña: "))
    print("Su saldo disponible es de: ", SALDOACTUAL)
    DINERO=int(input("Cuanto dinero deseas retirar: "))
    if DINERO>SALDOACTUAL:
        print("Saldo insuficiente")
    else:
         print("Su retiro se ha realizado exitosamente")
         SALDOACTUAL-=DINERO
         print("Saldo disponible:", SALDOACTUAL)
