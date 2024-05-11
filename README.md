# CellLife Explorer

Este proyecto utiliza pygraphviz para visualizar la vida en una célula.

## Requisitos

* Python 3.11+
* Graphviz
* pygraphviz

## Instalación

### Paso 1: Instalar Graphviz (solo para Windows)

Si estás en un sistema operativo Windows, es posible que debas instalar Graphviz y agregar su ruta al PATH del sistema antes de instalar pygraphviz. Puedes descargar Graphviz desde su sitio web oficial: https://graphviz.org/download/

Después de instalar Graphviz, agrega la ruta del ejecutable a tu PATH del sistema:

1. Haz clic en el botón "Inicio" y busca "Editar variables de entorno del sistema" en el cuadro de búsqueda.
2. Haz clic en "Editar variables de entorno del sistema" en los resultados de la búsqueda.
3. En la ventana "Propiedades del sistema", haz clic en "Variables de entorno" en el lateral izquierdo.
4. En la sección "Variables del sistema", desplaza hasta encontrar la variable "Path" y haz clic en "Editar".
5. Haz clic en "Nuevo" y agrega la ruta del ejecutable de Graphviz (por ejemplo, `C:\Program Files\Graphviz\bin`).
6. Haz clic en "Aceptar" en todas las ventanas.

### Paso 2: Instalar pygraphviz

Una vez que tienes.Graphviz instalado, puedes instalar pygraphviz mediante el siguiente comando:
```
python -m pip install --config-settings="--global-option=build_ext" --config-settings="--global-option=-IC:\Program Files\Graphviz\include" --config-settings="--global-option=-LC:\Program Files\Graphviz\lib" pygraphviz
```
## Uso

Ejecutar el script `main.py` para visualizar la vida en una célula.

```
python main.py
```
Este proyecto utiliza pygraphviz para visualizar la vida en una célula. El script `main.py` contiene el código para la simulación y visualización.

## Contribución

Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y crea un pull request con tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT.