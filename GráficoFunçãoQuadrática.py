# recebimento dos valores de a,b e c

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

# valor de delta

delta = (b ** 2) - (4 * a * c)

# cálculo das raízes reais

x1 = (- b + (delta ** (1/2))) / (2 * a)
x2 = (- b - (delta ** (1/2))) / (2 * a)

# impressão das respostas

if x1 == x2:
    print(f"As raízes reais são iguais a {x1}")
else:
    print(f"As raízes reais são {x1:.1f} e {x2:.1f}")

# gerar os dados para plotar o gráfico

# criar as listas vazias

valores_de_x = []
valores_de_y = []

# gerar valores de x e y para alimentar o gráfico

for x in range (-10,11,1):
    valores_de_x.append(x)
    valores_de_y.append((a * (x ** 2)) + (b * x) + c)

print("Valores de x: ", valores_de_x)
print("Valores de y: ", valores_de_y)

# importar biblioteca gráfica

import matplotlib.pyplot as plt

# desenhar o gráfico

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(valores_de_x, valores_de_y, linewidth=2)
plt.title("Gráfico Equação 2º Grau\n", fontsize=15)
plt.xlabel("\nValores de X", fontsize=12)
plt.ylabel("Valores de Y\n", fontsize=12)
plt.scatter(valores_de_x, valores_de_y, color='red', marker="o")
plt.xticks(range(-10,11,1))
plt.xlim()
plt.ylim()
plt.show()