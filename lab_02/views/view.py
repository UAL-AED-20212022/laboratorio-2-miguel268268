from models.LinkedList import *

def main():
   
    lista_ligada = LinkedList()
    
    
    while True:
        comandos = input().split(" ")
        if comandos[0] == "RPI":
            RPI(lista_ligada,comandos)
        if comandos[0] == "RPF":
            RPF(lista_ligada,comandos)
        if comandos[0] == "RPDE":
            RPDE(lista_ligada,comandos)
        if comandos[0] == "RPAE":
            RPAE(lista_ligada,comandos)
        if comandos[0] == "RPII":
            RPII(lista_ligada,comandos)
        if comandos[0] == "VNE":
            VNE(lista_ligada,comandos)
        if comandos[0] == "VP":
            VP(lista_ligada,comandos)
        if comandos[0] == "EPE":
            EPE(lista_ligada,comandos)
        if comandos[0] == "EUE":
            EUE(lista_ligada,comandos)
        if comandos[0] == "EP":
            EP(lista_ligada,comandos)
        



def RPI (lista_ligada,comandos):
    
    nome = comandos[1]

    lista_ligada.insert_at_start(nome)
    lista_ligada.traverse_list()

def RPF(lista_ligada,comandos):

    pais_fim = comandos[1]

    lista_ligada.insert_at_end(pais_fim)
    lista_ligada.traverse_list()

def RPDE(lista_ligada,comandos):

    pais_depois = comandos[1]
    pais_registado = comandos[2]

    lista_ligada.insert_after_item(pais_registado,pais_depois)
    lista_ligada.traverse_list()

def RPAE(lista_ligada,comandos):

    pais_antes = comandos[1]
    pais_registado = comandos[2]
    

    lista_ligada.insert_before_item(pais_registado,pais_antes)
    lista_ligada.traverse_list()

def RPII(lista_ligada,comandos):

    pais_novo = comandos[1]
    indice = int(comandos[2])
    



    lista_ligada.insert_at_index(indice,pais_novo)
    lista_ligada.traverse_list()

def VNE(lista_ligada,comandos):

    num_elemntos = lista_ligada.get_count()

    print(f"O número de elementos introduzidos são {num_elemntos}.")

def VP(lista_ligada,comandos):
    
    pais = comandos[1]


    if lista_ligada.search_item(pais) == True :
        print (f"O país {pais} encontra-se na lista")
    else:
        print (f"O país {pais} não se encontra-se na lista")




def EPE(lista_ligada,comandos):

    lista_ligada.delete_at_start()
    lista_ligada.traverse_list()

def EUE(lista_ligada,comandos):

    lista_ligada.delete_at_end()
    lista_ligada.traverse_list()

def EP(lista_ligada,comandos):

    pais = comandos[1]
    lista_ligada.delete_element_by_value(pais)
    print(f"O país {pais} foi eliminado da lista")
    lista_ligada.traverse_list()

