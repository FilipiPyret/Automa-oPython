#Passo a passo 

#1- Abrir o sistema da empresa;
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login;
 
import time
import pyautogui

pyautogui.PAUSE = 0.5

    #pyautogui.click -> clicar com o mouse;    
    #pyautogui.write -> escrever um testo;
    #pyautogui.press -> pressionar alguma tecla;
    #pyautogui.hotkey -> aperta um conjunto de teclas (ctrl C, ctrl V, Alt, Tab);

    #Abrir navegador; 
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
    
    #entrar no site do sistema;
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

    #aqui pode ser que ele demore para carregar o site;
time.sleep(2)

#2- Fazer login;

pyautogui.press("tab")
pyautogui.write("filipipirett@gmail.com")
pyautogui.press("tab")
pyautogui.write("filipilindo")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")

#3- Abrir/Importar a base de dados de produtos para cadastrar;
#pip install pandas numpy openpyxl

import pandas   

tabela = pandas.read_csv("produtos .csv")

print(tabela)

#4- Cadastrar produtos;
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    pyautogui.click(x=675, y=256)
    
#5- Repetir tudo isso ate acabar a lista de produtos; 