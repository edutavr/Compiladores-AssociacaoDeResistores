import matplotlib.pyplot as plt

class Circuit:
    def __init__(self, components):
        self.components = components
    
    def draw(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        x = 0
        y = 0
        ax.plot([x, x + 1], [y, y], 'k-')  # Linha inicial
        x += 1
        
        for component in self.components:
            self._draw_resistor(ax, x, y, component)
            x += 3
                # x = self._draw_parallel_group(ax, x, y, component)

        ax.plot([x, x + 1], [y, y], 'k-')  # Linha final
        plt.axis('off')
        plt.title("Circuito com Resistores em Série e Paralelo\n")
        plt.show()

    def _draw_resistor(self, ax, x, y, resistor):
        ax.plot([x, x + 1], [y, y], 'k-')  # Fio antes do resistor
        ax.plot([x + 1, x + 1.5], [y, y + 0.5], 'k-')  # Fio inclinado
        ax.plot([x + 1.5, x + 1.5], [y + 0.5, y - 0.5], 'k-', lw=2)  # Resistor
        ax.plot([x + 1.5, x + 2], [y - 0.5, y], 'k-')  # Fio inclinado
        ax.plot([x + 2, x + 3], [y, y], 'k-')  # Fio após o resistor
        ax.text(x + 1.5, y + 0.6, resistor, ha="center")