def calc(notas):
    t = 0
    for _ in notas:
        t = t + 1


    soma_total = 0
    for i in range(t):
        soma_total = soma_total + notas[i]

    media = soma_total / t


    soma_quadrados = 0
    for i in range(t):
        diff = notas[i] - media
        soma_quadrados = soma_quadrados + (diff * diff)
    dp = (soma_quadrados / t) ** 0.5


    maior = notas[0]
    menor = notas[0]
    for i in range(1, t):
        if notas[i] > maior:
            maior = notas[i]
        if notas[i] < menor:
            menor = notas[i]

    return maior, menor, media, dp


turma1 = [1.1, 7.5, 0.8, 1.8, 1.5, 1.9, 10.0, 10.0, 9.3, 10.0, 7.7, 0.6, 0.5,
          8.7, 5.6, 7.0, 8.3, 7.0, 9.1, 7.4, 8.1, 7.0, 6.3, 0.6, 7.4, 2.8, 5.0, 1.4, 1.5, 0.5,
          8.3, 7.0, 2.9, 7.6, 10.0, 3.3, 1.9, 5.1, 7.0]
turma2 = [10.0, 8.2, 8.7, 5.5, 6.8, 8.6, 8.5, 6.1, 6.2, 8.5, 7.7, 10.0, 10.0,
          6.1, 8.4, 5.4, 5.6, 9.8, 2.1, 8.5, 3.3, 8.7, 8.5, 9.1, 9.7]

ma1, mi1, me1, dp1 = calc(turma1)
ma2, mi2, me2, dp2 = calc(turma2)

print("Dados da turma 1: Nota máxima =", ma1, ", Nota mínima =", mi1, ", Média da turma =","{:.2f}".format(me1), ", Desvio Padrão =", "{:.2f}".format(dp1))
print("Dados da turma 2: Nota máxima =", ma2, ", Nota mínima =", mi2, ", Média da turma =","{:.2f}".format(me2), ", Desvio Padrão =", "{:.2f}".format(dp2))