from tkinter import Label, Tk, Button, Entry, Canvas, Frame
from Tree import *

window = Tk()


def addNode():
    global tree
    tree.addNode(txtEntry.get())
    tree.dibujar()


def deleteNode():
    global tree
    tree.eliminar(txtEntry.get())
    tree.dibujar()


def searchNode():
    global tree
    value = txtEntry.get()
    if tree.searchX(int(value)):
        txtResult["text"] = "El valor " + value + " está en el arbol"
    else:
        txtResult["text"] = "El valor " + value + " no está en el arbol"


def quantityNode():
    global tree
    result = tree.cantidad()
    txtResult["text"] = "La Cantidad de Nodo es: " + str(result)


def preOrden():
    global tree
    nodes = ""
    result = tree.preOrden()
    for i in range(0, len(result)):
        nodes = nodes + " [ "+str(result[i]) + " ] "
    txtResult["text"] = "PreOrden: " + nodes


def postOrden():
    global tree
    nodes = ""
    result = tree.postOrden()
    for i in range(0, len(result)):
        nodes = nodes + " [ "+str(result[i]) + " ] "
    txtResult["text"] = "PostOrden: " + nodes


def inOrden():
    global tree
    nodes = ""
    result = tree.inOrden()
    for i in range(0, len(result)):
        nodes = nodes + " [ " + str(result[i]) + " ] "
    txtResult["text"] = "InOrden: " + nodes


def amplitude():
    global tree
    result = tree.amplitud()
    txtResult["text"] = "La Amplitud del arbol es: " + str(result)


def altitude():
    global tree
    result = tree.altura()
    txtResult["text"] = "La Altura del arbol es: " + str(result)


def swing():
    global tree
    tree.balancear()
    tree.dibujar()


def cleaning():
    global tree
    tree.cleanTree()
    tree.dibujar()


def testing():
    global tree
    # result = tree.parent(int(txtEntry.get()))
    txtResult["text"] = "El resultado es: "


window.title("Arbol Binario de Busqueda")
window.geometry("1050x500")
frame1 = Frame(window, bg="black")
tree = Tree(frame1)
tree.dibujar()

lblTitle = Label(window, text="Estructuras ABB", bd="5", font=('Times New Roman', 20), fg="blue")

txtEntry = Entry(window, bg="white")
txtEntryParent = Entry(window, bg="white")
btnAdd = Button(window, text="Agregar un Valor", command=addNode)
btnDelete = Button(window, text="Eliminar un Valor", command=deleteNode)
btnSearch = Button(window, text="Buscar un Valor", command=searchNode)
btnQuantity = Button(window, text="Cantidad de Nodos", command=quantityNode)
btnPreOrden = Button(window, text="PreOrden", command=preOrden)
btnPostOrden = Button(window, text="PostOrden", command=postOrden)
btnInOrden = Button(window, text="InOrden", command=inOrden)
btnAmplitude = Button(window, text="Amplitud del Arbol", command=amplitude)
btnAltitude = Button(window, text="Altura del Arbol", command=altitude)
btnSwing = Button(window, text="Balancear Arbol", command=swing)
btnCleaning = Button(window, text="Limpiar Arbol", command=cleaning)
btnTesting = Button(window, text="Test", command=testing)
txtResult = Label(window, bg="green", fg="yellow", bd="5", font=('Segeo UI', 10))

lblTitle.place(relx=0.34, rely=0.05)
frame1.place(relx=0.02, rely=0.17)
btnAdd.place(relx=0.85, rely=0.06, relwidth=0.13, relheight=0.06)
btnDelete.place(relx=0.85, rely=0.13, relwidth=0.13, relheight=0.06)
btnSearch.place(relx=0.85, rely=0.2, relwidth=0.13, relheight=0.06)
btnQuantity.place(relx=0.85, rely=0.27, relwidth=0.13, relheight=0.06)
btnPreOrden.place(relx=0.85, rely=0.34, relwidth=0.13, relheight=0.06)
btnPostOrden.place(relx=0.85, rely=0.41, relwidth=0.13, relheight=0.06)
btnInOrden.place(relx=0.85, rely=0.48, relwidth=0.13, relheight=0.06)
btnAmplitude.place(relx=0.85, rely=0.55, relwidth=0.13, relheight=0.06)
btnAltitude.place(relx=0.85, rely=0.62, relwidth=0.13, relheight=0.06)
btnSwing.place(relx=0.85, rely=0.69, relwidth=0.13, relheight=0.06)
btnCleaning.place(relx=0.85, rely=0.76, relwidth=0.13, relheight=0.06)
btnTesting.place(relx=0.85, rely=0.83, relwidth=0.13, relheight=0.06)
txtEntry.place(relx=0.758, rely=0.06, relwidth=0.08, relheight=0.06)
txtEntryParent.place(relx=0.6, rely=0.06, relwidth=0.08, relheight=0.06)
txtResult.place(relx=0.23, rely=0.8, relwidth=0.40, relheight=0.07)

window.mainloop()
