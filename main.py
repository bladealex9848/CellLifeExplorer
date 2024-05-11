import random
import matplotlib.pyplot as plt
import networkx as nx
import networkx.drawing.nx_agraph as nx_agraph

class Molecule:
    def __init__(self, type):
        self.type = type

class Organite:
    def __init__(self, type, molecules):
        self.type = type
        self.molecules = molecules

class Cell:
    def __init__(self, organites):
        self.organites = organites

    def metabolize(self):
        for organite in self.organites:
            for molecule in organite.molecules:
                if random.random() < 0.5:
                    print(f"La célula ha procesado una molécula de tipo {molecule.type} en el organito {organite.type}")
                else:
                    print(f"La célula no ha podido procesar una molécula de tipo {molecule.type} en el organito {organite.type}")

    def divide(self):
        new_organites = [Organite(organite.type, organite.molecules.copy()) for organite in self.organites]
        return Cell(new_organites)

    def visualize(self):
        G = nx.DiGraph()
        G.add_node("Cell")
        for organite in self.organites:
            G.add_node(organite.type)
            G.add_edge("Cell", organite.type)
            for molecule in organite.molecules:
                G.add_node(molecule.type)
                G.add_edge(organite.type, molecule.type)
        nx_agraph.write_dot(G, 'cell.dot')
        plt.figure(figsize=(10, 10))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=5000, edge_color='black', linewidths=1, font_size=12)
        plt.show()

# Creamos moléculas
molecule_a = Molecule("A")
molecule_b = Molecule("B")

# Creamos organitos con moléculas
mitochondria = Organite("Mitochondria", [molecule_a, molecule_b])
ribosome = Organite("Ribosoma", [molecule_a, molecule_b])

# Creamos una célula con organitos
cell = Cell([mitochondria, ribosome])

# Simulamos la vida en la célula
print("Simulando la vida en la célula...")
cell.metabolize()

# Simulamos la división de la célula
print("Dividiendo la célula...")
new_cell = cell.divide()
print("Nueva célula creada")

# Visualizamos la célula
print("Visualizando la célula...")
cell.visualize()