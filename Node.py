"""
    Título: Estructura que me permite almacenar datos que se puede vincular entre si,
    denominada Nodo. Implementación de Estructura dinámica de tipo Nodo
    Autor: Miguel Angel Machuca Yavita
    Fecha: 05/09/2022
    Version: 1.0
"""


# clase dinámica que implementa un ADT TreeNode
class Node:
    """ Método crear instancia de TreeNode {objeto} establecer valor de tipo objeto """

    def __init__(self, value):
        self.__branchIzq = None
        self.__branchDer = None
        self.__data = value

    def getData(self):
        """ Método getData sirve para obtener el valor del nodo actual. """
        return self.__data

    def setData(self, data):
        """ Método setData sirve para introducir un valor al nodo actual. """
        self.__data = data

    def getBranchIzq(self):
        """ Método getBranchIzq sirve para obtener la rama izquierda del nodo actual. """
        return self.__branchIzq

    def setBranchIzq(self, branchIzq):
        """ Método setBranchIzq sirve para introducir un nodo como rama izquierda del nodo actual. """
        self.__branchIzq = branchIzq

    def getBranchDer(self):
        """ Método getBranchDer sirve para obtener la rama derecha del nodo actual. """
        return self.__branchDer

    def setBranchDer(self, branchDer):
        """ Método setBranchDer sirve para introducir un nodo como rama derecha del nodo actual. """
        self.__branchDer = branchDer
