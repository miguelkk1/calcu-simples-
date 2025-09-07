while True:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    so = n1 + n2
    su = n1 - n2
    div = n1 / n2
    mul = n1 * n2

    print('A soma é {}\nA subtração é {}'.format(so, su))
    print('A divisão é o seguinte: {:.2f}\nJá a multiplicação é: {}'.format(div, mul))
    print('Muito legal, né?')
    continuar = input("Quer fazer outro cálculo? (s/n): ")
    if continuar.lower() != "s":
        print("Tranquilo! Até um próximo cálculo.")
        break