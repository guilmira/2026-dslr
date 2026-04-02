# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 10:13:10 by guilmira          #+#    #+#              #
#    Updated: 2026/04/02 16:33:46 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#codeando todo sin una sola linea de GPT

import sys
import csv
import pandas as pd

class dataVisualizer:
    
    def __init__(self, arguments):
        
        self._fileName = self.parameter_parser(arguments)
        self._dataSet = []
        self._columnNames = []
        self.df = None
        
    def parameter_parser(self, arguments):
        
        if len(arguments) < 2:
            print("No se ha indicado fichero que leer")
            sys.exit(1)
        elif len(arguments) > 2:
            print("Demasiados argumentos introducidos. Introduzca un unico parametro con el nombre de fichero a leer")
            sys.exit(1)
        else:
            print(f"Datos cargados del fichero: {arguments[1]}")
            return arguments[1]


    def process_data(self):
        
        if self._fileName is None:
            sys.exit(1)
            
        try:
            with open(self._fileName, newline="") as csvfile:
                reader = csv.reader(csvfile)
                self._columnNames = next(reader)
                
                for row in reader:
                    if len(row) < 2:  # fila incompleta
                        continue
                    self._dataSet.append(row)
                
                self._df = pd.DataFrame(self._dataSet, columns=self._columnNames)
                
        except FileNotFoundError:   
            print(f"Error: {self._fileName} no existe.")
            sys.exit(1)
        
        

    def display_data(self, rows_to_show=None):
        if self._df is None or self._df.empty:
            print("Sin datos cargados")
            return
        
        #para mostrar todos los datos
        #pd.set_option('display.max_rows', None)
        #pd.set_option('display.max_colwidth', None)

        if rows_to_show is None:
            print(self._df)
        else:
            print(self._df.head(rows_to_show))



if __name__ == "__main__":
    visual = dataVisualizer(sys.argv)
    visual.process_data()
    visual.display_data()

# --- Slices en Python
    # slice = lista[inicio:fin:paso]
    # inicio -> índice donde empieza (inclusive)
    # fin -> índice donde termina (exclusive)
    
    # self._dataSet[:5] -> primeros 5 elementos (0 a 4)
    # self._dataSet[1:10:2] -> del 2º al 10º elemento, tomando de 2 en 2