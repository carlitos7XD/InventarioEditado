import speech_recognition as sr
import openpyxl
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Text, END, StringVar
from datetime import datetime

def reconocer_voz():
    # TODO: Implementar la lógica para reconocer voz


def exportar_a_excel(inventario):
    # TODO: Implementar la lógica para exportar a Excel


def exportar_a_pdf(inventario):
    # TODO: Implementar la lógica para exportar a PDF


def mostrar_grafico_salidas(inventario):
    # TODO: Implementar la lógica para mostrar gráfico de salidas


def main():
    inventario = {}

    root = Tk()
    root.title("Registro de Inventario")

    # Campos de entrada
    producto_var = StringVar()
    tipo_var = StringVar()

    Label(root, text="Producto:").grid(row=0, column=0)
    Entry(root, textvariable=producto_var).grid(row=0, column=1)


    # Botones
    Button(root, text="Registrar desde GUI", command=lambda: registrar_desde_gui(producto_var, cantidad_var, "añadir el resto")).grid(row=4, column=0, columnspan=2)


    # Widget de texto para mostrar el inventario
    text_widget = Text(root, height=10, width=50)
    text_widget.grid(row=9, column=0, columnspan=2)

    # Mostrar el inventario inicialmente
    mostrar_inventario(inventario, text_widget)

    root.mainloop()

if __name__ == "__main__":
    main()
