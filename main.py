import re
import tkinter as tk

def procesar_texto():
    #texto_original = input_entry.get()
    texto_original = input_entry.get("1.0", tk.END).strip()
    if texto_original != '':
        regex = r'[^a-zA-Z\s]'

        numero_total_palabras = 0
        longitud_media_palabras = 0
        numero_oraciones = len(list(filter(None,(re.sub(r'[0-9\s]','',texto_original)).split("."))))
        ultima_palabra_larga = ''
        palabras_largas = []

        for palabras in (re.sub(regex, ' ', texto_original)).split(" "):
            print(palabras)
            numero_total_palabras += 1 if len(palabras) != 0 else 0
            longitud_media_palabras += len(palabras)
            if len(ultima_palabra_larga) < len(palabras):
                palabras_largas = []
                palabras_largas.append(palabras)
                ultima_palabra_larga = palabras
            elif len(ultima_palabra_larga) == len(palabras):
                palabras_largas.append(palabras)
                ultima_palabra_larga = palabras
            

        #print(f"numero total de palabras: {str(numero_total_palabras)} ")
        resultado = f"total palabras: {numero_total_palabras} \n"
        resultado += f'Longitud media de palabras: {(longitud_media_palabras/numero_total_palabras if numero_total_palabras != 0 else numero_total_palabras):.2f} \n'
        resultado += f'Numero de oraciones en el texto: {numero_oraciones} \n'
        resultado += f'Palabra / palabras mas largas: {palabras_largas}'
        resultado_label.config(text=resultado, justify="left")
    else:
        resultado_label.config(text='Error al procesar texto \nIngrese texto para procesar!!!')


def iniciar():
    procesar_texto(input('Ingrese el texto a analizar: '))

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("Procesador de Texto")

    #input_entry = tk.Entry(ventana)
    input_entry = tk.Text(ventana, width=50, height=10)
    input_entry.pack(pady=40)

    mostrar_button = tk.Button(ventana, text="Procesar Resultado", command=procesar_texto)
    mostrar_button.pack(pady=5)

        # Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=10)

        # Calcular la posición para centrar la ventana
    ancho_ventana = 500  # Ancho deseado de la ventana
    alto_ventana = 400  # Alto deseado de la ventana

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    ventana.minsize(500, 500)
    ventana.mainloop()