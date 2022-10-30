"""
    Título: Estructura de datos no lineal en la que cada nodo
    puede apuntar a dos nodos en la cual cada nodo puede tener
    una rama izquierda y una rama derecha
    Autor: Miguel Angel Machuca Yavita
    Fecha: 21/09/2022
    Version: 3.0
"""
from tkinter import Canvas
from Node import *


class Tree(Canvas):
    """ Método crear instancia de la clase Arbol {objeto} establecer value de tipo objeto """

    def __init__(self, tk):
        super().__init__(tk, bg='green', width=855)
        super().grid(row=0, column=0, sticky='nsew')
        self.__root = None
        self.__nodeQuantity = 0

    def dibujar(self):
        super().delete("all")
        self.__dibujar1(self.__root, 427, 30)

    def __dibujar1(self, nodeCurrent, x, y):  # 200, 15
        if self.__isNone(nodeCurrent):
            super().create_oval(x - 11, y - 11, x + 11, y + 11, fill="yellow")
            # super().create_text(x - 1, y + 3, text="Null", fill="white")
            return
        if self.isLeaf(nodeCurrent):
            super().create_oval(x - 11, y - 11, x + 11, y + 11, fill="blue")
            super().create_text(x, y, text=nodeCurrent.getData(), fill="yellow")
            return
        super().create_oval(x - 11, y - 11, x + 11, y + 11, fill="blue")
        super().create_text(x, y, text=nodeCurrent.getData(), fill="yellow")
        alt = self.__altura(nodeCurrent) - 1

        ch = pow(2, alt) - 1
        dx = ch * 13 + 20
        dy = 40

        super().create_line(x, y + 11, x - dx, y + dy)  # izquierda
        super().create_line(x, y + 11, x + dx, y + dy)  # derecha

        self.__dibujar1(nodeCurrent.getBranchIzq(), x - dx, y + dy)
        self.__dibujar1(nodeCurrent.getBranchDer(), x + dx, y + dy)

    def __setRoot(self, value):
        """ Método setRoot sirve para introducir un nodo en el Árbol actual. """
        self.__root = Node(value)

    def __getRoot(self):
        """ Método getRoot sirve para obtener el nodo raíz del Árbol actual. """
        return self.__root

    def cleanTree(self):
        self.__root = None

    def getNodeQuantity(self):
        """ Método getRoot sirve . """
        return self.__nodeQuantity

    def setNodeQuantity(self, value):
        """ Método getRoot sirve . """
        self.__nodeQuantity = value

    def factor_equilibrio(self, nodo_actual):
        if nodo_actual is None:
            return 0
        altura_izq = self.__altura(nodo_actual.getBranchIzq())
        altura_der = self.__altura(nodo_actual.getBranchDer())
        return altura_der - altura_izq

    def esta_equilibrado(self):
        return self.__esta_equilibrado(self.__root)

    def __esta_equilibrado(self, nodo_actual):
        if nodo_actual is None:
            return True
        if self.isLeaf(nodo_actual):
            return True
        factor = self.factor_equilibrio(nodo_actual)
        if not (factor == -1 or factor == 0 or factor == 1):
            return False
        esta_balanceado_izq = self.__esta_equilibrado(nodo_actual.getBranchIzq())
        esta_balanceado_der = self.__esta_equilibrado(nodo_actual.getBranchDer())
        return esta_balanceado_izq and esta_balanceado_der

    def __rotacion_simple_izq(self, nodo_actual):
        nodo_der = nodo_actual.getBranchDer()
        nodo_actual.setBranchDer(nodo_der.getBranchIzq())
        nodo_der.setBranchIzq(nodo_actual)
        return nodo_der

    def __rotacion_simple_der(self, nodo_actual):
        nodo_izq = nodo_actual.getBranchIzq()
        nodo_actual.setBranchIzq(nodo_izq.getBranchDer())
        nodo_izq.setBranchDer(nodo_actual)
        return nodo_izq

    def __rotacion_doble_izq(self, nodo_actual):
        nodo_actual.setBranchDer(self.__rotacion_simple_der(nodo_actual.getBranchDer()))
        return self.__rotacion_simple_izq(nodo_actual)

    def __rotacion_doble_der(self, nodo_actual):
        nodo_actual.setBranchIzq(self.__rotacion_simple_izq(nodo_actual.getBranchIzq()))
        return self.__rotacion_simple_der(nodo_actual)

    def rebalance(self, node):
        nodeCurrent = node
        while nodeCurrent is not None:
            height_right = self.__altura(nodeCurrent)
            height_left = self.__altura(nodeCurrent)
            if nodeCurrent.getBranchDer is not None:
                height_right = self.__altura(nodeCurrent.getBranchDer())

            if nodeCurrent.getBranchIzq is not None:
                height_left = self.__altura(nodeCurrent.getBranchIzq())

            if abs(height_left - height_right) > 1:
                if height_left > height_right:
                    left_child = nodeCurrent.getBranchIzq()
                    if left_child is not None:
                        h_right = (self.__altura(left_child.getBranchDer()) if (left_child.getBranchDer() is not None) else 0)
                        h_left = (self.__altura(left_child.getBranchIzq()) if (left_child.getBranchIzq() is not None) else 0)
                    if h_left > h_right:
                        self.rotate_left(nodeCurrent)
                        break
                    else:
                        self.double_rotate_right(nodeCurrent)
                        break
                else:
                    right_child = nodeCurrent.getBranchDer()
                    if right_child is not None:
                        h_right = (self.__altura(right_child.getBranchDer()) if (right_child.getBranchDer() is not None) else 0)
                        h_left = (self.__altura(right_child.getBranchIzq()) if (right_child.getBranchIzq() is not None) else 0)
                    if h_left > h_right:
                        self.double_rotate_left(nodeCurrent)
                        break
                    else:
                        self.rotate_right(nodeCurrent)
                        break
            nodeCurrent = self.__parent(nodeCurrent)

    def __parent(self, node):
        parent = None
        if self.isEmpty():
            return None
        else:  # Caso general
            mainNode = self.__getRoot()
            while mainNode is not None:
                if node.getData() < mainNode.getData():
                    parent = mainNode
                    mainNode = mainNode.getBranchIzq()
                else:
                    if node.getData() > mainNode.getData():
                        parent = mainNode
                        mainNode = mainNode.getBranchDer()
                    else:
                        return parent
            return

    def rotate_left(self, node):
        aux = self.__parent(node).getData()
        self.__parent(node).setData(node.getData())
        self.__parent(node).setBranchDer(Node(aux))
        self.__parent(node).setBranchIzq(node.getBranchIzq())

    def rotate_right(self, node):
        # aux = self.__parent(node).getData()
        aux = 100
        self.__parent(node).setData(node.getData())
        self.__parent(node).setBranchIzq(Node(aux))
        self.__parent(node).setBranchDer(node.getBranchDer())

    def double_rotate_left(self, node):
        self.rotate_right(node.getRight().getRight())
        self.rotate_left(node)

    def double_rotate_right(self, node):
        self.rotate_left(node.getLeft().getLeft())
        self.rotate_right(node)

    def balancear(self):
        self.__root = self.__equilibrar(self.__root)
        return self.__root


    def __equilibrar(self, nodo_actual):
        if nodo_actual is None:
            return None
        else:
            if self.isLeaf(nodo_actual):
                return nodo_actual
            else:
                nodo_actual.setBranchIzq(self.__equilibrar(nodo_actual.getBranchIzq()))
                nodo_actual.setBranchDer(self.__equilibrar(nodo_actual.getBranchDer()))

                factor_equilibrio = self.factor_equilibrio(nodo_actual)
                factor_equilibrio_izq = self.factor_equilibrio(nodo_actual.getBranchIzq())
                factor_equilibrio_der = self.factor_equilibrio(nodo_actual.getBranchDer())

                if factor_equilibrio == -2 and factor_equilibrio_izq != 1:
                    nodo_actual = self.__rotacion_simple_der(nodo_actual)
                if factor_equilibrio == 2 and factor_equilibrio_der != -1:
                    nodo_actual = self.__rotacion_simple_izq(nodo_actual)

                if factor_equilibrio == -2 and factor_equilibrio_izq != -1:
                    nodo_actual = self.__rotacion_doble_izq(nodo_actual)
                if factor_equilibrio == 2 and factor_equilibrio_der != 1:
                    nodo_actual = self.__rotacion_doble_der(nodo_actual)

                return nodo_actual

    def __addNodeIteratively(self, value):
        if self.isEmpty():
            self.__setRoot(value)
        else:  # Caso general
            previousNode = None
            mainNode = self.__getRoot()
            while mainNode is not None:
                previousNode = mainNode
                if value < mainNode.getData():
                    mainNode = mainNode.getBranchIzq()
                elif value > mainNode.getData():
                    mainNode = mainNode.getBranchDer()
                else:
                    return  # Salir, posiblemente el value exista en el arbol
            newNode = Node(value)
            if value < previousNode.getData():
                previousNode.setBranchIzq(newNode)
            else:
                if value > previousNode.getData():
                    previousNode.setBranchDer(newNode)

    def __addNodeRecursive(self, nodeCurrent, value):
        if nodeCurrent is None:
            newNode = Node(value)
            nodeCurrent = newNode
        if nodeCurrent.getData() > value:
            self.__addNodeRecursive(nodeCurrent.getBranchIzq(), value)
        else:
            if nodeCurrent.getData() < value:
                self.__addNodeRecursive(nodeCurrent.getBranchDer(), value)
            else:
                return

    def addNode(self, value):
        self.__nodeQuantity += 1
        return self.__addNodeIteratively(value)

    def isEmpty(self):
        if self.__root is None:
            return True
        return False

    def __isNone(self, nodeCurrent):
        if nodeCurrent is None:
            return True
        else:
            return False

    def isLeaf(self, verifyNode):
        return verifyNode.getBranchIzq() is None and \
               verifyNode.getBranchDer() is None

    def searchX(self, value):
        if self.isEmpty():
            return False
        else:  # Caso general
            mainNode = self.__getRoot()
            while mainNode is not None:
                if value < mainNode.getData():
                    mainNode = mainNode.getBranchIzq()
                else:
                    if value > mainNode.getData():
                        mainNode = mainNode.getBranchDer()
                    else:
                        return mainNode.getData() is value
            return False

    def inOrden(self):
        nodeList = []
        self.__inOrden(self.__root, nodeList)
        return nodeList

    def __inOrden(self, currentNode, nodeList):
        if currentNode is not None:
            self.__inOrden(currentNode.getBranchIzq(), nodeList)
            nodeList.append(currentNode.getData())
            self.__inOrden(currentNode.getBranchDer(), nodeList)

    def postOrden(self):
        nodeList = []
        self.__postOrden(self.__root, nodeList)
        return nodeList

    def __postOrden(self, currentNode, nodeList):
        if currentNode is not None:
            self.__postOrden(currentNode.getBranchIzq(), nodeList)
            self.__postOrden(currentNode.getBranchDer(), nodeList)
            nodeList.append(currentNode.getData())

    def preOrden(self):
        nodeList = []
        self.__preOrden(self.__root, nodeList)
        return nodeList

    def __preOrden(self, currentNode, nodeList):
        if currentNode is not None:
            nodeList.append(currentNode.getData())
            self.__preOrden(currentNode.getBranchIzq(), nodeList)
            self.__preOrden(currentNode.getBranchDer(), nodeList)

    def amplitud(self):
        return self.__amplitud(self.__root)

    def __amplitud(self, currentNode):
        if currentNode is None:
            return 0
        else:
            if self.isLeaf(currentNode):
                if self.nivelNodo(currentNode) + 1 is self.__altura(self.__root):
                    return 1
                return 0
            else:
                izq = self.__amplitud(currentNode.getBranchIzq())
                der = self.__amplitud(currentNode.getBranchDer())
                return izq + der

    def altura(self):
        return self.__altura(self.__root)

    def __altura(self, currentNode):
        if currentNode is None:
            return 0
        else:
            if self.isLeaf(currentNode):
                return 1
            else:
                izq = self.__altura(currentNode.getBranchIzq())
                der = self.__altura(currentNode.getBranchDer())
                return izq + 1 if izq > der else der + 1

    def __cantidad(self, currentNode):
        if currentNode is None:
            return 0
        else:
            if self.isLeaf(currentNode):
                return 1
            else:
                izq = self.__cantidad(currentNode.getBranchIzq())
                der = self.__cantidad(currentNode.getBranchDer())
                return izq + der + 1

    def cantidad(self):
        return self.__cantidad(self.__root)

    def nivelNodo(self, currentNode):
        contador = 0
        if self.__getRoot() is currentNode:
            return contador
        else:  # Caso general
            mainNode = self.__root
            while mainNode is not None:
                if currentNode.getData() < mainNode.getData():
                    mainNode = mainNode.getBranchIzq()
                    contador += 1
                else:
                    if currentNode.getData() > mainNode.getData():
                        mainNode = mainNode.getBranchDer()
                        contador += 1
                    else:
                        return contador

    def eliminar(self, value):
        mainNode = self.__root
        nodo_anterior = None
        while mainNode is not None and mainNode.getData() != value:
            nodo_anterior = mainNode
            if value > mainNode.getData():
                mainNode = mainNode.getBranchDer()
            else:
                mainNode = mainNode.getBranchIzq()
        if mainNode is None:
            return
        if self.isLeaf(mainNode):
            self.eliminar_caso_1(nodo_anterior, mainNode)

        else:
            if (mainNode.getBranchDer() is not None and mainNode.getBranchIzq() is None) \
                    or (mainNode.getBranchDer() is None and mainNode.getBranchIzq() is not None):
                self.eliminar_caso_2(nodo_anterior, mainNode)
            else:
                self.eliminar_caso_3(mainNode)

    def eliminar_caso_1(self, nodo_anterior, mainNode):
        if nodo_anterior is None:
            self.__setRoot(None)
        else:
            if mainNode is nodo_anterior.getBranchDer():
                nodo_anterior.setBranchDer(None)
            else:
                nodo_anterior.setBranchIzq(None)

    def eliminar_caso_2(self, nodo_anterior, mainNode):
        if nodo_anterior is None:
            if mainNode.getBranchDer() is not None:
                self.__setRoot(mainNode.getBranchDer())
            else:
                self.__setRoot(mainNode.getBranchIzq())
        else:
            if mainNode is nodo_anterior.getBranchDer():
                if mainNode.getBranchDer() is not None:
                    nodo_anterior.setBranchDer(mainNode.getBranchDer())
                else:
                    nodo_anterior.setBranchIzq(mainNode.getBranchIzq())
            else:
                if mainNode.getBranchDer() is not None:
                    nodo_anterior.setBranchDer(mainNode.getBranchDer())
                else:
                    nodo_anterior.setBranchIzq(mainNode.getBranchIzq())

    def eliminar_caso_3(self, mainNode):
        nodo_actual = mainNode.getBranchDer()
        anterior = None
        while nodo_actual.getBranchIzq() is not None:
            anterior = nodo_actual
            nodo_actual = nodo_actual.getBranchIzq()
        auxiliar_value = mainNode.getData()
        mainNode.setData(nodo_actual.getData())
        nodo_actual.setData(auxiliar_value)
        if anterior is None:
            mainNode.setBranchDer(None)
        else:
            anterior.setBranchIzq(None)

    def str(self):
        return self.__createRepresentation(self.__root, "Raíz", "", True)

    def __createRepresentation(self, currentNode, representation, nivel, es_derecho):
        representation += nivel
        if nivel != "":
            representation += "\b\b" + \
                              (" \u251C\u2500HD" if es_derecho else " \u2514\u2500HI") + "\u2500"

        if currentNode is None:
            representation += "\u06DD\n"
            return representation

        representation += "(" + str(currentNode.getData()) + ")" + "\n"
        # Hijo derecho
        representation = self.__createRepresentation(currentNode.getBranchDer(),
                                                     representation, nivel + "      \u2502", True)
        # Hijo izquierdo
        representation = self.__createRepresentation(currentNode.getBranchIzq(),
                                                     representation, nivel + "       ", False)
        return representation
