# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 10:13:10 by guilmira          #+#    #+#              #
#    Updated: 2026/04/02 18:20:23 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#MISSING
#All it has to do is display information for all numerical features like in the example
#bonus es darle mas fields, ademas de min max, media etc.

import sys
import csv
import pandas as pd

class DataManager:
    
    def __init__(self, arguments):
        
        self.df = None
        self._dataSet = []
        self._columnNames = []
        self._fileName = self.parameter_parser(arguments)
        
    def parameter_parser(self, arguments):
        
        if len(arguments) < 2:
            print("No se ha indicado fichero que leer")
            return None
        elif len(arguments) > 2:
            print("Demasiados argumentos introducidos. Introduzca un unico parametro con el nombre de fichero a leer")
            return None
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
    manager = DataManager(sys.argv)
    manager.process_data()
    manager.display_data()

# --- Slices en Python
    # slice = lista[inicio:fin:paso]
    # inicio -> índice donde empieza (inclusive)
    # fin -> índice donde termina (exclusive)
    
    # self._dataSet[:5] -> primeros 5 elementos (0 a 4)
    # self._dataSet[1:10:2] -> del 2º al 10º elemento, tomando de 2 en 2