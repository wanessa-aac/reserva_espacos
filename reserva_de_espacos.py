import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import messagebox
from backend import middleware
from backend.queries import get_reservas

# Função para inserir uma nova reserva no banco de dados

# Função para exibir as reservas em uma nova janela
def exibir_reservas():
    reservas = get_reservas()

    exibicao_reservas = ctk.CTkToplevel()
    exibicao_reservas.geometry("800x500")
    exibicao_reservas.title("Reservas")
    

    for idx, reserva in enumerate(reservas):
        label = ctk.CTkLabel(exibicao_reservas, text=f"Nome: {reserva[1]}, Bloco: {reserva[2]}, Apartamento: {reserva[3]},  local:{reserva[4]}, Data: {reserva[5]}")
        label.pack()

# Função chamada ao clicar no botão reservar
def on_reservar_click():
    nome = nome_entry.get()
    bloco = bloco_entry.get()
    apartamento = apartamento_entry.get()
    data = sel.get()
    local = combo_places.get()
    call_db = middleware.check_reserva(nome, bloco, apartamento, local, data)
   
   
    messagebox.showinfo(message=call_db)

# Configuração da janela principal
app = ctk.CTk()
app.geometry("960x680")
app.title("Sistema de Condomínio")
app.resizable(False, False)

# Entradas e botões
nome_label = ctk.CTkLabel(app, text="Nome:")
nome_label.pack()
nome_entry = ctk.CTkEntry(app)
nome_entry.pack()

bloco_label = ctk.CTkLabel(app, text="Bloco:")
bloco_label.pack()
bloco_entry = ctk.CTkEntry(app)
bloco_entry.pack()

apartamento_label = ctk.CTkLabel(app, text="Apartamento:")
apartamento_label.pack()
apartamento_entry = ctk.CTkEntry(app)
apartamento_entry.pack()

sel = ctk.StringVar() 
data_label = ctk.CTkLabel(app, text="Data (dd/mm/yyyy):",)
data_label.pack()
calendario = DateEntry(app, selectmode ="day", textvariable=sel)
calendario.pack()
calendario.bind("<Key>", lambda e: "break")
def my_upd(*args):
    print(sel.get())

# data_entry.s("01/01/2024")

espaco_label = ctk.CTkLabel(app,text="Espaços:")
espaco_label.pack()
places =["Salão de Festas","Piscina","Quadra de Tênis","Spa","Espaço Gourmet","Churrasqueira","Quadra"]
combo_places = ctk.CTkComboBox(app, values=places, state="readonly")
combo_places.set(places[0])
combo_places.pack()

reservar_button = ctk.CTkButton(app, text="Reservar", fg_color="green", hover_color="#014B05", command=on_reservar_click)
reservar_button.pack(pady=10)

exibir_button = ctk.CTkButton(app, text="Exibir Reservas", fg_color="gray", hover_color="#202020", command=exibir_reservas)
exibir_button.pack(pady=10)

# Execução da aplicação
app.mainloop() 