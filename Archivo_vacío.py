import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class CURPGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de CURP")
        self.geometry("650x800")
        self.configure(bg='#e3f2fd')  # Fondo azul claro

        # Estilo personalizado
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Usar tema clam para mejor apariencia

        # Configurar estilos
        self.style.configure('Main.TFrame', background='#e3f2fd')
        self.style.configure('Card.TFrame', background='white', relief='solid')
        self.style.configure('Main.TLabel', background='#e3f2fd', font=('Helvetica', 11))
        self.style.configure('Title.TLabel', background='#e3f2fd', font=('Helvetica', 24, 'bold'))
        self.style.configure('Subtitle.TLabel', background='#e3f2fd', font=('Helvetica', 14))
        self.style.configure('Card.TLabelframe', background='white', relief='solid')
        self.style.configure('Card.TLabelframe.Label', font=('Helvetica', 12, 'bold'), background='white')

        # Configurar botón personalizado
        self.style.configure('Generate.TButton', font=('Helvetica', 12, 'bold'), background='#1976d2', foreground='white', padding=(20, 10))

        self.create_widgets()

    def create_widgets(self):
        # Marco principal
        main_frame = ttk.Frame(self, padding="30", style='Main.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Título
        title_label = ttk.Label(main_frame, 
                              text="Generador de CURP",
                              style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Sección de datos personales
        self.create_personal_info(main_frame)

        # Sección de fecha de nacimiento
        self.create_birth_info(main_frame)

        # Sección de lugar de nacimiento
        self.create_location_info(main_frame)

        # Botón de generar
        generate_button = ttk.Button(main_frame, 
                                   text="Generar CURP",
                                   command=self.generar_curp,
                                   style='Generate.TButton')
        generate_button.grid(row=20, column=0, columnspan=2, pady=25)

        # Marco para el resultado
        result_frame = ttk.Frame(main_frame, style='Card.TFrame')
        result_frame.grid(row=21, column=0, columnspan=2, pady=15, sticky='ew')

        self.result_label = ttk.Label(result_frame, 
                                    text="CURP Generada: ",
                                    font=('Helvetica', 14, 'bold'), 
                                    foreground='#1976d2',
                                    background='white')
        self.result_label.grid(row=0, column=0, pady=15, padx=15)

    def create_personal_info(self, frame):
        # Etiquetas y entradas para nombre y apellidos
        ttk.Label(frame, text="Nombre(s):", style='Main.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_nombre = ttk.Entry(frame)
        self.entry_nombre.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Apellido Paterno:", style='Main.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_apellido_paterno = ttk.Entry(frame)
        self.entry_apellido_paterno.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Apellido Materno:", style='Main.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_apellido_materno = ttk.Entry(frame)
        self.entry_apellido_materno.grid(row=3, column=1, pady=5)

    def create_birth_info(self, frame):
        # Combobox para día, mes y año de nacimiento
        ttk.Label(frame, text="Día de Nacimiento:", style='Main.TLabel').grid(row=4, column=0, sticky=tk.W, pady=5)
        self.combo_dia = ttk.Combobox(frame, values=[str(i) for i in range(1, 32)], width=5)
        self.combo_dia.grid(row=4, column=1, pady=5)

        ttk.Label(frame, text="Mes de Nacimiento:", style='Main.TLabel').grid(row=5, column=0, sticky=tk.W, pady=5)
        self.combo_mes = ttk.Combobox(frame, values=[f"{i:02d}-Mes" for i in range(1, 13)], width=10)
        self.combo_mes.grid(row=5, column=1, pady=5)

        ttk.Label(frame, text="Año de Nacimiento:", style='Main.TLabel').grid(row=6, column=0, sticky=tk.W, pady=5)
        self.combo_año = ttk.Combobox(frame, values=[str(i) for i in range(1900, datetime.now().year + 1)], width=10)
        self.combo_año.grid(row=6, column=1, pady=5)

    def create_location_info(self, frame):
        # Combobox para sexo y estado
        ttk.Label(frame, text="Sexo:", style='Main.TLabel').grid(row=7, column=0, sticky=tk.W, pady=5)
        self.combo_sexo = ttk.Combobox(frame, values=["Hombre", "Mujer"], width=10)
        self.combo_sexo.grid(row=7, column=1, pady=5)

        ttk.Label(frame, text="Estado de Nacimiento:", style='Main.TLabel').grid(row=8, column=0, sticky=tk.W, pady=5)
        self.combo_estado = ttk.Combobox(frame, values=["CHIAPAS", "OTRO"], width=10)
        self.combo_estado.grid(row=8, column=1, pady=5)

    def es_bisiesto(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def validar_fecha(self, dia, mes, anio):
        dias_mes = {1: 31, 2: 29 if self.es_bisiesto(anio) else 28, 3: 31, 4: 30,
                    5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        return 1 <= dia <= dias_mes.get(mes, 31)

    def generar_curp(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()

        # Obtener fecha de los combos
        dia = int(self.combo_dia.get())
        mes = int(self.combo_mes.get().split('-')[0])
        anio = int(self.combo_año.get())

        # Validar fecha
        if not self.validar_fecha(dia, mes, anio):
            self.result_label.config(text="Fecha inválida, por favor corrige los datos.")
            return

        sexo = "H" if self.combo_sexo.get() == "Hombre" else "M"
        estado = self.combo_estado.get()

        # Generación de CURP
        curp = apellido_paterno[0].upper()
        for letra in apellido_paterno[1:]:
            if letra.lower() in 'aeiou':
                curp += letra.upper()
                break

        curp += apellido_materno[0].upper() if apellido_materno else "X"
        if nombre.split()[0].upper() in ["MARIA", "JOSE"] and len(nombre.split()) > 1:
            curp += nombre.split()[1][0].upper()
        else:
            curp += nombre[0].upper()

        curp += f"{str(anio)[-2:]}{mes:02d}{dia:02d}"
        curp += sexo

        estados = {
            'CHIAPAS': 'CS',
            # Resto de estados omitidos para este ejemplo
        }
        curp += estados.get(estado, "NE")

        def primer_consonante_interna(palabra):
            for letra in palabra[1:]:
                if letra.lower() not in 'aeiou':
                    return letra.upper()
            return "X"

        curp += primer_consonante_interna(apellido_paterno)
        curp += primer_consonante_interna(apellido_materno) if apellido_materno else "X"
        curp += primer_consonante_interna(nombre)

        curp += str(random.randint(0, 9)) + str(random.randint(0, 9))

        self.result_label.config(text="CURP Generada: " + curp)

if __name__ == "__main__":
    app = CURPGenerator()
    app.mainloop()
