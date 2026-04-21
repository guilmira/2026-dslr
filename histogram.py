# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 10:48:26 by guilmira          #+#    #+#              #
#    Updated: 2026/04/02 18:14:59 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import matplotlib.pyplot as plt
from describe import DataManager


#PENDIENTE: hay que terminar describe. DEJARLO LISTO TAMBIEN, que imprima la media, el count de los datos etcetera.

#parece que hay simbolos raros en el csv y hay que convertir todo a numerico

#tengo las siguientes dudas: ¿estan los datos mal? ¿hay que pasarlos a numerico
#como se construye la tabla de la primera parte del subject?

#antes de soltar 42 esta ronda, a ver si consigues representar de las 3 maneras los datos

#dejar 2 evaluaciones listas. para que cuando te pille la semana jodida de abril, poder quitartela rapida. irte a la semana del 19.

class HistogramGenerator:
    def __init__(self, dataManager):
        self.dataManagerObject = dataManager

        print(self.dataManagerObject._df.dtypes)
        print(self.dataManagerObject._df.head())

    def create_histograms(self):
        df = self.dataManagerObject._df
        if df is None or df.empty:
            print("No hay datos.")
            return

        numeric_cols = df.select_dtypes(include='number').columns
        if not numeric_cols.any():
            print("No hay columnas para generar histogramas.")
            return

        for col in numeric_cols:
            plt.figure()
            df[col].hist(bins=20, edgecolor='black')
            plt.title(f"Histograma de {col}")
            plt.xlabel(col)
            plt.ylabel("Frecuencia")
            plt.grid(False)
            plt.savefig(f"{col}_histogram.png")
            print(f"Histograma guardado: {col}_histogram.png")
            plt.show()  # Descomentar si quieres mostrarlo en pantalla

#Diseño modular. Diferentes clases que hacen solo una funcion especifica. Data
if __name__ == "__main__":
    manager = DataManager(sys.argv)
    manager.process_data()

    hist = HistogramGenerator(manager)
    hist.create_histograms()