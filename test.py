import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ventana transparente con círculo flotante")

    # Hacer la ventana principal completamente transparente
    root.attributes('-transparentcolor', root['bg'])  # Hace que el color de fondo de la ventana sea transparente
    root.geometry('400x400')
    # root.overrideredirect(True)  # Elimina la barra de título y bordes de la ventana

    # Crear un canvas con fondo transparente
    canvas = tk.Canvas(root, width=400, height=400, bg=root['bg'], highlightthickness=0)
    canvas.grid(row=0,column=0)

    lbl = tk.Label(root,bg=root['bg'])
    lbl.grid(row=0,column=1)

    def imagen(ruta, ancho, alto):
        imagen = Image.open(ruta)
        imagen = imagen.resize((ancho, alto))
        imagen_tk = ImageTk.PhotoImage(imagen)
        return imagen_tk
    
    img = imagen('templates/gato.png',400,400)
    # Dibujar un círculo en el canvas
    canvas.create_image(0,0, image=img)

    # Permitir mover la ventana arrastrándola
    def move_window(event):
        root.geometry(f'+{event.x_root}+{event.y_root}')

    canvas.bind("<B1-Motion>", move_window)

    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()


