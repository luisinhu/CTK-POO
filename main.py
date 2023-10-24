import customtkinter as ctk
from customtkinter import *
from classes import *

class JanelaPrincipal(ctk.CTk):
    def __init__(self, ):
        super().__init__()
        self.configuracao()
        self.page_cadastro_aluno()

    
    
    def configuracao(self):
        self.geometry('600x750+1+10')
        self.resizable(False, False)
    
    def escolha_prof_aluno(self, apagar_frame):

        apagar_frame.place_forget()

        self.frame_escolha = CTkFrame(self, width=500, height= 500)
        self.frame_escolha.place(x = 40, y = 100)
        
        self.label_escolha = CTkLabel(self.frame_escolha, text='Você é Aluno ou professor?')
        self.label_escolha.place(x= 180, y = 190)
        
        self.escolha_aluno = CTkButton(self.frame_escolha, text= 'Aluno', command=self.page_cadastro_aluno)
        self.escolha_aluno.place(x= 190,  y= 230)
        
        self.escolha_prof= CTkButton(self.frame_escolha, text= 'Professor', command=self.page_cadastro_prof)
        self.escolha_prof.place(x= 190,  y= 260)
        
    
    def telaLogin(self,apagar_frame):
        
        apagar_frame.place_forget()
        self.frame_login = CTkFrame(self, width=500, height= 500)
        self.frame_login.place(x = 40, y = 100)
    
        self.label_login = CTkLabel(self.frame_login, text= 'Login')
        self.label_login.place(x= 250,  y= 50)
    
        self.entry_matricula = CTkEntry(self.frame_login, width= 200, height=40, placeholder_text='matricula')
        self.entry_matricula.place(x= 160,  y= 80)

        self.entry_senha = CTkEntry(self.frame_login, width= 200, height=40, placeholder_text='senha')
        self.entry_senha.place(x= 160,  y= 140)

        self.radio_prof= CTkRadioButton(self.frame_login, text='Prof', value=1)
        self.radio_prof.place(x= 160,y= 195)

        self.radio_aluno= CTkRadioButton(self.frame_login, text='Aluno', value=2)
        self.radio_aluno.place(x= 160, y= 220)

        self.button_login = CTkButton(self.frame_login, text= 'Login')
        self.button_login.place(x= 190,  y= 260)

        self.label_login_ir_cadastro = CTkLabel(self.frame_login, text= 'Ainda não tem uma conta?', width=90)
        self.label_login_ir_cadastro.place(x= 190,  y= 320)

        self.button_cadastrarse = CTkButton(self.frame_login, text= 'Cadastrar-se',command= lambda: self.escolha_prof_aluno(self.frame_login))
        self.button_cadastrarse.place(x= 190,  y= 350)
        

    def page_cadastro_prof(self):
        self.frame_escolha.place_forget()
        
        self.frame_cadastro_prof = CTkFrame(self, width=500, height= 500)
        self.frame_cadastro_prof.place(x = 40, y = 100)
        
        self.label_escolha_prof = CTkLabel(self.frame_cadastro_prof, text='Casdastro do Prof', font= ('Arial Bold', 22))
        self.label_escolha_prof.place(x= 170, y = 60)
        
        self.entry_nome_prof = CTkEntry(self.frame_cadastro_prof, width= 200, height=40, placeholder_text='Nome')
        self.entry_nome_prof.place(x= 160,  y= 100)
    
        self.entry_matricula_prof = CTkEntry(self.frame_cadastro_prof, width= 200, height=40, placeholder_text='matricula')
        self.entry_matricula_prof.place(x= 160,  y= 150)

        self.entry_senha_prof = CTkEntry(self.frame_cadastro_prof, width= 200, height=40, placeholder_text='senha')
        self.entry_senha_prof.place(x= 160,  y= 200)
        
    
    def page_cadastro_aluno(self):
        
        self.frame_cadastro_aluno = CTkFrame(self, width=500, height= 500)
        self.frame_cadastro_aluno.place(x = 40, y = 100)
        
        self.label_escolha = CTkLabel(self.frame_cadastro_aluno, text='Casdastro do Aluno', font= ('Arial Bold', 22))
        self.label_escolha.place(x= 170, y = 60)
        
        self.entry_nome_aluno = CTkEntry(self.frame_cadastro_aluno, width= 200, height=40, placeholder_text='Nome')
        self.entry_nome_aluno.place(x= 160,  y= 100)
    
        self.entry_matricula_aluno = CTkEntry(self.frame_cadastro_aluno, width= 200, height=40, placeholder_text='matricula')
        self.entry_matricula_aluno.place(x= 160,  y= 150)

        self.entry_senha_aluno = CTkEntry(self.frame_cadastro_aluno, width= 200, height=40, placeholder_text='senha')
        self.entry_senha_aluno.place(x= 160,  y= 200)
        
        
        self.optionmenu = CTkOptionMenu(self.frame_cadastro_aluno, values=['1 INFO A','1 INFO B','1 ELET A','1 ELET B','1 EDIF A','1 EDIF B','1 QUIM A','1 QUIM B','2 INFO M','2 INFO V','2 ELET M','2 ELET V','2 EDIF M','2 EDIF V','2 QUIM M','2 QUIM V','3 INFO M','3 INFO V','3 ELET M','3 ELET V','3 EDIF M','3 EDIF V','3 QUIM M','3 QUIM V',],)
        
        self.optionmenu.place(x= 160,  y= 250)

        self.sexo = CTkOptionMenu(self.frame_cadastro_aluno, values=['Masculino', 'Feminino'])
        self.sexo.place(x= 160,y= 290)


        self.radio_var =StringVar(value='A')
        
        self.button_cadastrarse = CTkButton(self.frame_cadastro_aluno, text= 'Cadastrar-se', command= lambda: self.cadastrar_aluno())
        self.button_cadastrarse.place(x= 190,  y= 370)
        
        self.label_cadastroAl_login = CTkLabel(self.frame_cadastro_aluno, text= 'Já tem uma conta?', width=90)
        self.label_cadastroAl_login.place(x= 200,  y= 420)

        self.button_cadastrarse = CTkButton(self.frame_cadastro_aluno, text= 'Login', command=lambda: self.telaLogin(self.frame_cadastro_aluno))
        self.button_cadastrarse.place(x= 190,  y= 450)
    
    def cadastrar_aluno(self):
        nome = self.entry_nome_aluno.get()
        matricula = self.entry_matricula_aluno.get()
        senha = self.entry_senha_aluno.get()
        sexo = self.radio_var.get()
        turma = self.optionmenu.get()

        if nome and matricula and senha and turma:
            aluno = Aluno(nome, sexo, matricula, senha, turma)
            aluno.Cadastrar()
            print("Aluno cadastrado com sucesso!")
            # Limpar os campos do formulário após o cadastro (opcional)
            self.entry_nome_aluno.delete(0, 'end')
            self.entry_matricula_aluno.delete(0, 'end')
            self.entry_senha_aluno.delete(0, 'end')
            self.optionmenu.set('')  # Limpa a seleção da turma
        else:
            print("Preencha todos os campos obrigatórios.")

    
if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()