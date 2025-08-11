from tkinter import*
from PIL import Image, ImageTk

class Olaf:# Libreria para correr animaciones en Tkinter
    # -------------------------------convertir imagen------------------------------------
    def imagen(ruta, ancho, alto):
        imagen = Image.open(ruta)
        imagen = imagen.resize((ancho,alto))
        imagen_tk = ImageTk.PhotoImage(imagen)
        return imagen_tk
# -------------------------------convertir lista de imagenes--------------------------
    def imagen_sec(lista_img):
        lista_tk = []
        for i in lista_img:
            imagen_tk = Olaf.imagen(i,250,250)
            lista_tk.append(imagen_tk)
        return lista_tk
# -------------------------------animacion for-------------------------------------
    def sec_for(canvas,lista_tk):
        global g_lista
        g_lista = lista_tk
        lbl= canvas
        for i in g_lista:
            lbl.delete("all")
            lbl.create_image(128, 128, image=i) #coordenadas de la imagen
            lbl.update_idletasks()  # Actualizar la interfaz de usuario
            lbl.after(50)  # Pausa


if __name__ == "__main__":
    raiz = Tk()

    raiz.mainloop()
