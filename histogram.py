# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 10:48:26 by guilmira          #+#    #+#              #
#    Updated: 2026/04/02 18:06:25 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import matplotlib.pyplot as plt
from describe import DataManager

#parece que hay simbolos raros en el vsv y hay que convertir todo a numerico

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