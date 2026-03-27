# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 09:44:52 by guilmira          #+#    #+#              #
#    Updated: 2026/03/27 10:48:10 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

VIRTUAL_ENV_NAME = venv
#--------------------------------------------------------------------------------------------------------------VERSION
PYTHON_OS= python3  #cambiar si el interprete tiene otro nombre, i.e., python
#--------------------------------------------------------------------------------------------------------------SOURCES
DEPS = matplotlib pandas
SRC1 = describe.py
SRC_G1 = histogram.py
SRC_G2 = scatter_plot.py
SRC_G3 = pair_plot.py
#--------------------------------------------------------------------------------------------------------------RULES
#Sobre test
#test + CONDITION = TRUE OR FALSE
#test -d = la CONDITION es si existe o no el directorio

all: install help

install:
	@test -d $(VIRTUAL_ENV_NAME) || $(PYTHON_OS) -m venv $(VIRTUAL_ENV_NAME)

help:
	@echo "Comandos para ejecutar el proyecto en el entorno virtual:"
	@echo "Para activar: 		 'source $(VIRTUAL_ENV_NAME)/bin/activate'"
	@echo "Para dependencias:	 'make deps'"
	@echo "Para desactivar: 	 'deactivate'"

deps:
	@test -d $(VIRTUAL_ENV_NAME) || { echo "No existe el entorno virtual. Ejecuta 'make install' primero."; exit 1; }
	@test "$$VIRTUAL_ENV" = "$(PWD)/$(VIRTUAL_ENV_NAME)" || { echo "No estás dentro del entorno virtual. Haz 'make help' primero y activa el entorno"; exit 1; }
	pip install --upgrade --quiet $(DEPS)

run:
	@test -d $(VIRTUAL_ENV_NAME) || { echo "No existe el entorno virtual. Ejecuta 'make install' primero."; exit 1; }
	@test "$$VIRTUAL_ENV" = "$(PWD)/$(VIRTUAL_ENV_NAME)" || { echo "No estás dentro del entorno virtual. Haz 'make help' primero y activa el entorno"; exit 1; }
	$(PYTHON_OS) $(SRC1)

graphs:
	$(PYTHON_OS) $(SRC_G1)
	$(PYTHON_OS) $(SRC_G2)
	$(PYTHON_OS) $(SRC_G3)


clean:
	@rm -rf __pycache__
	@rm -rf theta.txt result.png
	
fclean: clean
	@rm -rf $(VIRTUAL_ENV_NAME)
