# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 10:13:10 by guilmira          #+#    #+#              #
#    Updated: 2026/03/27 10:51:48 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#codeando todo sin una sola linea de GPT

class dataVisualizer:
    
    def __init__(self):
        self._fileName = None
        self._dataSet = None
        
        
    def file_reader(self):
        print("Type name of the file to iniziate visualizer:")
        if self._fileName is None:
            print(f"Testeando valor de Nonetype: {self._fileName}")

if __name__ == "__main__":
    visual = dataVisualizer()
