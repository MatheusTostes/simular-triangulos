# O objetivo aqui era criar uma interface grafica que pedisse 3 entradas, rodasse condições dizendo se esses 3 valores 
# poderiam formar um triangulo, em caso afirmativo, devolver as classificações do triângulo e plotar uma representação 
# do mesmo em escala reduzida.

# Resultado: https://i.imgur.com/5I6uX21.png


from tkinter import *                                                           # Importa tudo da biblioteca tkinter. 

janela = Tk()                                                                   # Instancia o tkinter com a variável janela.
janela.title("TIPO DE TRIÂNGULO")                                               # Renomeia o titulo janela.

def bt_click():                                                                 # Define uma função para o botão.
    print("btclick")                                                            # Teste para exibir no console se o botão foi acionado.

    v1 = V1.get()                                                               # Armazenamento dos valores de entrada.
    v2 = V2.get()
    v3 = V3.get()

    a = int(v1)                                                                 # Conversão dos valores de entrada de string para inteiros.
    b = int(v2)
    c = int(v3)


    if (a <= 0 or b <= 0 or c <= 0):                                            # Primeira condição de exisência de um triângulo.
        print("Valores invalidos.")  
        lb4["text"] = "Valores invalidos."                                      # Renomeia o label vazio para retornar quebra da condição.

    else: 
        if (a + b <= c or a + c <= b or b + c <= a):                            # Segunda condição de exisência de um triângulo.
            print("Valores nao podem formar um triangulo.")
            lb5["text"] = "Valores nao podem formar um triangulo."              # Renomeia o label vazio para retornar quebra da condição.

        else:                                                                   
            if (a == b and a == c):                                             # Condição de triângulo equilátero.
                 print("Triangulo equilatero.")                                 # Teste para exibir no console se a condição passou ou reprovou.
                 lb4["text"] = "Triangulo equilatero."                          # Renomeia o label 4 para avisar caso a condição passe.
                                                                                # Abaixo o processo se repete com condições distintas para cada tipo de triângulo.
            if (a == b and b !=c or a == c and a != b or c==b and c != a):
                 print("Triangulo isosceles.")
                 lb5["text"] = "Triangulo isosceles."

            if (a != b and b != c and a != c):
                 print("Triangulo escaleno.")
                 lb6["text"] = "Triangulo escaleno."

            if ((b ** 2  == (a ** 2 + c ** 2)) or (a ** 2  == (b ** 2 + c ** 2)) or (c ** 2  == (a ** 2 + b ** 2))):
                print("Triangulo retangulo.")
                lb7["text"] = "Triangulo retangulo."

            if (((b ** 2 < (a ** 2 + c ** 2))and a<=b and c<=a) or ((a ** 2 < (c ** 2 + b ** 2))and c <= a and b <= c) or ((c ** 2 < (b ** 2 + a ** 2))and b <= c and a <= b)):
                print("Triangulo acutangulo.")
                lb8["text"] = "Triangulo acutangulo."

            if (b ** 2 > (a ** 2 + c ** 2)) or (a ** 2 > (b ** 2 + c ** 2)) or (c ** 2 > (b ** 2 + a ** 2)):
                print("Triangulo obtusangulo.")
                lb9["text"] = "Triangulo obtusangulo."

    lbs = [lb4, lb5, lb6, lb7, lb8, lb9]                                         # Todo label que não for renomeado sob as condições acima será enviado para o final da janela,
    for lb in lbs:                                                               ## aos labels que irão fornecer informação (caso contrário, espaço seria desperdiçado com labels
        if lb["text"] == "":                                                     ## vazias).
            lb.grid(row=11)


            A = (0, 0)                                                           # A, B e C definem as coordenadas iniciais do triângulo dentro da célula da grade.
            B = (c, 0)
            hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
            dx = (b**2 - hc**2)**0.5
            if abs((c - dx)**2 + hc**2 - a**2) > 0.01: dx = -dx     
            C = (dx, hc)


            coords = [int((x + 1) * 10) for x in A+B+C]                          # Cria a variável coord para utilizar A, B, C e escalonar a figura.

            canvas = Canvas(janela, width=200, height=50)                        # Restringe a área que a figura ocupará.
            blue = canvas.create_polygon(*coords)                                # Cria a figura sobre a variável coords.
            canvas.grid(row=1, column=3, rowspan=4)                              # Posiciona a figura em uma celula específica da grade e une as 3 colunas abaixo dela para seu uso.

lb0 = Label(janela, text="Insira os valores dos lados")                          # Texto inicial sobre as entradas.
lb1 = Label(janela, text="A : ")                                                 # Texto que antecede as entradas à esquerda.
lb2 = Label(janela, text="B : ")
lb3 = Label(janela, text="C : ")


lb4 = Label(janela, text="")                                                     # Labels que serão usados pela função para informar o tipo de triângulo. 
lb5 = Label(janela, text="")
lb6 = Label(janela, text="")
lb7 = Label(janela, text="")
lb8 = Label(janela, text="")
lb9 = Label(janela, text="")

V1 = Entry(janela, width = 30)                                                   # Define as caixas de entrada e sua largura.
V2 = Entry(janela, width = 30)
V3 = Entry(janela, width = 30)

lb0.grid(row=0, column=2)                                                        # Posiciona na grade o lb0 (o mesmo para os demais labels abaixo).
lb1.grid(row=1, column=1)
lb2.grid(row=2, column=1)
lb3.grid(row=3, column=1)

lb4.grid(row=5, column=2)
lb5.grid(row=6, column=2)
lb6.grid(row=7, column=2)
lb7.grid(row=8, column=2)
lb8.grid(row=9, column=2)
lb9.grid(row=10, column=2)

V1.grid(row=1, column=2)                                                         # Posiciona na grade as caixas de entrada.
V2.grid(row=2, column=2)
V3.grid(row=3, column=2)


bt1 = Button(janela, text="Confirmar", command=bt_click)                         # Botão que chamará a função definida no inicio.

bt1.grid(row=4 ,column=2)                                                        # Posiciona o botão.

janela.geometry("300x200+500+200")                                               # Define o tamanho da janela.
janela.mainloop()                                                                # Mantém a execução da janela.
