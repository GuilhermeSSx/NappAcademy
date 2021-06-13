from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv


class Estrategia(ABC):
    """
    Classe Base para as estratégias (algoritmos)

    """
    @abstractmethod
    def execute(self, dados):
        """ Método em que o algoritmo é contido.
        Implementação do algoritmo na classe filha deve
        sobreescrever este método."""
        pass

    @abstractmethod
    def parametros_necessarios(self):
        """Sobreescrever este método para que retorne uma tupla
        com a lista de parâmetros necessários.
        Exemplo:
        ('algoritmo', 'dbname', 'host', 'user', 'password')
        """
        pass

    @abstractmethod
    def nome(self):
        """Sobreescrever este método para que
        retorne o nome do algoritmo utilizado."""
        pass


class Estrategia_SQLite(Estrategia):
    def execute(self, dados):
        lista_registros = []
        teste = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            for linha in cursor.fetchall():
                lista_registros.append(linha)
        #Modificação do desafio 06
        for item in lista_registros:
            teste.append((item[-2],item[-1]))   
        return teste

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'



class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        teste=[]
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_registros = []
                lista_registros2 = []
                lista_registros.append(line['total'])
                lista_registros2.append(line['vendido_em'])
                teste.append(dict(zip(lista_registros2, lista_registros)))
        return teste

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'


class Estrategia_Texto1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as txt:
            for line in txt:
                line = line.replace("\n","")
                if line.startswith("Arquivo") or line.startswith("*") or line.startswith("DATA"):
                    continue

                line = line.split("       ")
                lista_registros.append((line[4].strip(), float(line[3].strip()), line[0].strip()))
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto 1'


class Estrategia_Texto2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as txt:
            for line in txt:
                line = line.replace("\n","")
                if line.startswith("Arquivo") or line.startswith("*") or line.startswith("DATA"):
                    continue

                line = line.split("       ")
                lista_registros.append((line[1].strip(), float(line[2].strip()), line[0].strip()))
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto 2'
