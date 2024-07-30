# Autor: Tiago Bela e Luan Oliveira
# Ultima modificação: 29/07/2024
# Utilidade: Quiz com alguns tópicos da bíblia

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def limpar_widgets():
    for widget in raiz.winfo_children():
        if isinstance(widget, (tk.Label, ttk.Combobox)):
            widget.destroy()

def combo_box_selecionado(dia, category):
    escolha = combo_vars[category][dia].get() # recebe a escolha do usuário ao combo_box
    verificar_valor_inserido(category)
    if category == 'criacoes' and escolha == dias_criacao[dia]: # verifica se a escolha esta contida na lista de criacoes
        label_resultado[category][dia].config(text="Parabéns! Correto!", fg="green")
        return
    if category == 'pragas' and escolha == pragas[dia-1]: # verifica se a escolha esta contida na lista de pragas
        label_resultado[category][dia].config(text="Parabéns! Correto!", fg="green")
        return
    label_resultado[category][dia].config(text="Errado!", fg="red")

def verificar_valor_inserido(category):
    valores_corretos = True
    for dia in range(1, 8 if category == 'criacoes' else 11): # laco que percorre toda a lista
        if category == 'criacoes' and combo_vars[category][dia].get() != dias_criacao[dia]:
            valores_corretos = False # caso o valor nao bateu 'valores_corretos' recebe false
            break
        elif category == 'pragas' and combo_vars[category][dia].get() != pragas[dia-1]:
            valores_corretos = False # caso o valor nao bateu 'valores_corretos' recebe false
            break
    if valores_corretos:
        if category == 'criacoes':
            botao_prosseguir.place(x=220, y=355) # ajusta o botao quando o valor bate corretamente
        elif category == 'pragas':
            botao_prosseguir_tela_pragas.place(x=220, y=455) # ajusta o botao quando o valor bate corretamente

def tela_final():
    limpar_widgets() # destroi os widgets da imagem anterior 
    janela_tela_livros.destroy() # destroi o canvas da tela anterior
    raiz.title("Tela final") # modifica o título

    global janela_tela_final
    imagem_tela_final = Image.open("img/tela_final.png") # carrega o caminho da caminho
    imagem_fundo_tela_final = ImageTk.PhotoImage(imagem_tela_final)
    janela_tela_final = tk.Canvas(raiz, width=imagem_tela_final.width, height=imagem_tela_final.height) # cria o canvas
    janela_tela_final.pack(fill="both", expand=True)
    janela_tela_final.create_image(0, 0, image=imagem_fundo_tela_final, anchor="nw") # coloca a imagem no canvas
    janela_tela_final.background_image = imagem_fundo_tela_final 


def verificar_livro():
    valor_inserido = caixa_texto_livros.get().strip() # pega o valor inserido no input
    if valor_inserido in livros:
        livros.remove(valor_inserido)
        label_informante_tela_livros.config(text=f"Tribos restantes: {len(livros)}") # informa o numero de livros que restam
        caixa_texto_livros.delete(0, tk.END)  # limpa o input da caixa de texto
        if not livros:
            botao_prosseguir_tela_livros.pack()
    if len(livros) == 0:
        botao_prosseguir_tela_livros.place(x=383, y=200) # ajusta o botao na tela

def quiz_livros():
    limpar_widgets() # limpa os widgets da tela passada
    janela_tela_tribos.destroy() # destroi o canvas da tela passada
    raiz.title("Os livros do antigo testamento") # modifica o título 
    
    global janela_tela_livros
    imagem_tela_livros = Image.open("img/etapa04.png")
    imagem_fundo_tela_livros = ImageTk.PhotoImage(imagem_tela_livros)
    janela_tela_livros = tk.Canvas(raiz, width=imagem_tela_livros.width, height=imagem_tela_livros.height)
    janela_tela_livros.pack(fill="both", expand=True)
    janela_tela_livros.create_image(0, 0, image=imagem_fundo_tela_livros, anchor="nw")
    janela_tela_livros.background_image = imagem_fundo_tela_livros

    global caixa_texto_livros, label_informante_tela_livros, botao_prosseguir_tela_livros, livros
    livros = [ "Gênesis", "Êxodo", "Levítico", "Números", "Deuteronômio",
               "Josué", "Juízes", "Rute", "1 Samuel", "2 Samuel",
               "1 Reis", "2 Reis", "1 Crônicas", "2 Crônicas", "Esdras",
               "Neemias", "Ester", "Jó", "Salmos", "Provérbios",
               "Eclesiastes", "Cânticos", "Isaías", "Jeremias", "Lamentações",
               "Ezequiel", "Daniel", "Oséias", "Joel", "Amós",
               "Obadias", "Jonas", "Miquéias", "Naum", "Habacuque",
               "Sofonias", "Ageu", "Zacarias", "Malaquias" ] # lista com todos os livros da bília

    caixa_texto_livros = tk.Entry(raiz, width=55)
    caixa_texto_livros.place(x=50, y=160)

    label_informante_tela_livros = tk.Label(raiz, text=f"Livros restantes: {len(livros)}") # informa o numero de livros
    label_informante_tela_livros.place(x=50, y=185)
    
    botao_prosseguir_tela_livros = tk.Button(raiz, text="Prosseguir", command=tela_final)
    botao_prosseguir_tela_livros.pack_forget()

    botao_verificar_tela_livros = tk.Button(raiz, text="Verificar", command=verificar_livro)
    botao_verificar_tela_livros.place(x=395, y=156)

def verificar_tribo():
    valor_inserido = caixa_texto_tribos.get().strip() # pega o valor inserido no input de texto
    if valor_inserido in tribos:
        tribos.remove(valor_inserido) # caso o valor inserido seja uma tribo válida remove da lista
        label_informante.config(text=f"Tribos restantes: {len(tribos)}") # informa o numero de tribos que restam
        caixa_texto_tribos.delete(0, tk.END)  # limpa o input
        if not tribos:
            botao_prosseguir_tela_tribos.pack()  # mostra o botão para prosseguir se todas as tribos ja foram inseridas
    if len(tribos) == 0:
        botao_prosseguir_tela_tribos.place(x=383, y=200) # ajusta na tela o botao de prosseguir

def quiz_tribos():
    limpar_widgets() # limpa os widgets da tela anterior
    janela_tela_praga.destroy() # destroi o canvas da tela anterior
    raiz.title("As 12 tribos") # modifica o titulo da janela
    raiz.geometry("500x400") # modifica o tamanho da tela
    
    global janela_tela_tribos
    imagem_tela_tribos = Image.open("img/etapa03.png")
    imagem_fundo_tela_tribos = ImageTk.PhotoImage(imagem_tela_tribos)
    janela_tela_tribos = tk.Canvas(raiz, width=imagem_tela_tribos.width, height=imagem_tela_tribos.height)
    janela_tela_tribos.pack(fill="both", expand=True)
    janela_tela_tribos.create_image(0, 0, image=imagem_fundo_tela_tribos, anchor="nw")
    janela_tela_tribos.background_image = imagem_fundo_tela_tribos

    global caixa_texto_tribos, label_informante, botao_prosseguir_tela_tribos, tribos
    tribos = [ "Rúben", "Simeão", "Levi", "Judá", "Dã", 
               "Naftali", "Gade", "Aser", "Issacar", "Zebulom", 
               "José", "Benjamim" ] # lista com as tribos

    caixa_texto_tribos = tk.Entry(raiz, width=55) # seta a caixa de texto das tribos e sua largura
    caixa_texto_tribos.place(x=50, y=160) # ajusta a caixa de texto na tela

    label_informante = tk.Label(raiz, text=f"Tribos restantes: {len(tribos)}") # informa o numero de tribos que faltam para proxima fase
    label_informante.place(x=50, y=185) # ajusta o label na tela
    
    botao_prosseguir_tela_tribos = tk.Button(raiz, text="Prosseguir", command=quiz_livros) # cria o botao de prosseguir
    botao_prosseguir_tela_tribos.pack_forget() 

    botao_verificar_tela_tribos = tk.Button(raiz, text="Verificar", command=verificar_tribo) # cria o botao de verificar
    botao_verificar_tela_tribos.place(x=395, y=156)

def quiz_pragas():
    limpar_widgets() # limpa os widgets
    janela_tela_criacao.destroy() # destroi o canvas da janela anterior
    raiz.title("As dez pragas") # modifica o titulo da nova tela
    raiz.geometry("500x500") # redimensiona a dimensao da janela
    
    global janela_tela_praga
    imagem_tela_praga = Image.open("img/etapa02.png") # carrega a imagem da etapa 02
    imagem_fundo_tela_praga = ImageTk.PhotoImage(imagem_tela_praga)
    janela_tela_praga = tk.Canvas(raiz, width=imagem_tela_praga.width, height=imagem_tela_praga.height)
    janela_tela_praga.pack(fill="both", expand=True)
    janela_tela_praga.create_image(0, 0, image=imagem_fundo_tela_praga, anchor="nw")
    janela_tela_praga.background_image = imagem_fundo_tela_praga

    global botao_prosseguir_tela_pragas
    imagem_prosseguir_tela_praga = Image.open("img/prosseguir.png")
    foto03 = ImageTk.PhotoImage(imagem_prosseguir_tela_praga.resize((50, 35)))
    botao_prosseguir_tela_pragas = tk.Label(raiz, image=foto03)
    botao_prosseguir_tela_pragas.pack(expand=True)
    botao_prosseguir_tela_pragas.bind("<Button-1>", lambda e: quiz_tribos())
    botao_prosseguir_tela_pragas.bind("<Enter>", lambda e: botao_prosseguir_tela_pragas.config(cursor="hand2"))
    botao_prosseguir_tela_pragas.bind("<Leave>", lambda e: botao_prosseguir_tela_pragas.config(cursor=""))
    botao_prosseguir_tela_pragas.image = foto03

    combo_vars['pragas'] = {}
    combo_boxes['pragas'] = {}
    label_resultado['pragas'] = {}

    global pragas
    pragas = [ "Água em sangue", "Rãs", "Piolhos", "Moscas",
               "Peste nos animais", "Úlceras", "Chuva de pedras",
               "Gafanhotos", "Trevas", "Morte dos primogênitos" ] # lista com as pragas 

    escolha_usuario_tela_praga = pragas

    for dia in range(1, 11):
        numero_praga = tk.Label(raiz, text=f"Praga {dia}:") # cria um label com os numeros das pragas
        numero_praga.place(x=50, y=25 + 40 * dia) # seta a posicao do texto na tela

        combo_var = tk.StringVar()
        combo_var.set("Escolha uma opção")
        combo_vars['pragas'][dia] = combo_var
        combo_box = ttk.Combobox(raiz, textvariable=combo_var, values=escolha_usuario_tela_praga, width=25)
        combo_box.place(x=150, y=25 + 40 * dia)
        combo_box.bind("<<ComboboxSelected>>", lambda event, d=dia: combo_box_selecionado(d, 'pragas'))
        combo_boxes['pragas'][dia] = combo_box

        label_resultado_tela_praga = tk.Label(raiz, text="") # coloca o label do resultado da escolha do usuário na tela
        label_resultado_tela_praga.place(x=350, y=25 + 40 * dia)
        label_resultado['pragas'][dia] = label_resultado_tela_praga

def quiz_criacao():
    global combo_vars, combo_boxes, label_resultado
    
    combo_vars = {'criacoes': {}, 'pragas': {}}
    combo_boxes = {'criacoes': {}, 'pragas': {}}
    label_resultado = {'criacoes': {}, 'pragas': {}}

    global dias_criacao # dicionário contendo os dias da criacao
    dias_criacao = { 1: "Luz", 2: "Céu, firmamento", 3: "Terra, mares, vegetação",
                     4: "Sol, Lua, Estrelas", 5: "Animais aquaticos, aves", 
                     6: "Animais terrestres, homem", 7: "Descansou" }

    escolha_usuario = ["Luz", "Céu, firmamento", "Terra, mares, vegetação",
                "Sol, Lua, Estrelas", "Animais aquaticos, aves", 
                "Animais terrestres, homem", "Descansou"] # vetor com os dias da semana

    for dia in range(1, 8):
        label_dia = tk.Label(raiz, text=f"Dia {dia}:") # cria um label na tela 
        label_dia.place(x=50, y=50 + 40 * dia) # coloca em uma posicao específica da tela

        combo_var = tk.StringVar() 
        combo_var.set("Escolha uma opção") # seta como a opcao default do combo box
        combo_vars['criacoes'][dia] = combo_var
        combo_box = ttk.Combobox(raiz, textvariable=combo_var, values=escolha_usuario, width=25)
        combo_box.place(x=150, y=50 + 40 * dia) # coloca em uma posicao específica da tela
        combo_box.bind("<<ComboboxSelected>>", lambda event, d=dia: combo_box_selecionado(d, 'criacoes')) # metodo para verificar o valor da escolha do usuário
        combo_boxes['criacoes'][dia] = combo_box

        label_resultado_tela_criacao = tk.Label(raiz, text="")
        label_resultado_tela_criacao.place(x=350, y=50 + 40 * dia)
        label_resultado['criacoes'][dia] = label_resultado_tela_criacao
    
def tela_principal():
    limpar_widgets() # limpa todos os widgets da tela passada
    janela_tela_principal.destroy() # destroi o canvas da tela inicial
    raiz.title("A criação") # setagem do título da nova tela

    global janela_tela_criacao, imagem_fundo_tela_criacao
    imagem_tela_criacao = Image.open("img/etapa01.png")
    imagem_fundo_tela_criacao = ImageTk.PhotoImage(imagem_tela_criacao)
    janela_tela_criacao = tk.Canvas(raiz, width=imagem_tela_criacao.width, height=imagem_tela_criacao.height)
    janela_tela_criacao.pack(fill="both", expand=True)
    janela_tela_criacao.create_image(0, 0, image=imagem_fundo_tela_criacao, anchor="nw")
    janela_tela_criacao.background_image = imagem_fundo_tela_criacao

    global botao_prosseguir
    imagem_prosseguir = Image.open("img/prosseguir.png") # carregar a imagem de prosseguir
    foto02 = ImageTk.PhotoImage(imagem_prosseguir.resize((50, 35)))
    botao_prosseguir = tk.Label(raiz, image=foto02)
    botao_prosseguir.pack(expand=True)
    botao_prosseguir.bind("<Button-1>", lambda e: quiz_pragas())
    botao_prosseguir.bind("<Enter>", lambda e: botao_prosseguir.config(cursor="hand2")) # modificar o cursor
    botao_prosseguir.bind("<Leave>", lambda e: botao_prosseguir.config(cursor="")) # modificar o cursor
    botao_prosseguir.image = foto02 
    
    quiz_criacao() # chama o método 'quiz_criacao' que contem toda a logica da tela de criacao

if __name__ == "__main__":
    global raiz # declaração da raíz de toda a aplicação
    raiz = tk.Tk()
    raiz.title("Tela Inicial") # setagem do título da tela inicial
    raiz.geometry("500x400") # setagem da dimensão inicial da tela [500, 400]
    raiz.resizable(False, False) # impede o usuário de redimensionar a tela

    global janela_tela_principal, imagem_fundo_tela_principal
    imagem_tela_principal = Image.open("img/fundo.png") # setagem do caminho da imagem
    imagem_fundo_tela_principal = ImageTk.PhotoImage(imagem_tela_principal)
    janela_tela_principal = tk.Canvas(raiz, width=imagem_tela_principal.width, height=imagem_tela_principal.height)
    janela_tela_principal.pack(fill="both", expand=True)
    janela_tela_principal.create_image(0, 0, image=imagem_fundo_tela_principal, anchor="nw") # instanciando a imagem no fundo da imagem
    janela_tela_principal.background_image = imagem_fundo_tela_principal

    global botao_inicial
    imagem_iniciar = Image.open("img/iniciar.png") # setagem do caminho da imagem
    foto01 = ImageTk.PhotoImage(imagem_iniciar.resize((55, 43)))
    botao_inicial = tk.Label(raiz, image=foto01)
    botao_inicial.pack(expand=True)
    botao_inicial.bind("<Button-1>", lambda e: tela_principal())
    botao_inicial.bind("<Enter>", lambda e: botao_inicial.config(cursor="hand2")) # modificar o cursor
    botao_inicial.bind("<Leave>", lambda e: botao_inicial.config(cursor="")) # modificar o cursor
    botao_inicial.place(x=220, y=340)
    botao_inicial.image = foto01

    raiz.mainloop() # mantem a raiz em loop durante a execucao do processo