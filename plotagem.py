import matplotlib.pyplot as plt

class Circuit:
    def __init__(self, structure, niveis):
        self.structure = structure
        self.niveis = niveis
        self.positions = []  # Lista para armazenar as posições de componentes e conexões
        self.x = 0  # Inicializa x de forma consistente
        self.x_prox = 0  # Inicializa x de forma consistente

    def draw(self):
        # Primeira passagem: calcular posições
        y_ax = self._calculate_positions(self.structure, 0)

        # Segunda passagem: desenhar com base nas posições calculadas
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        plt.axis('off')
        plt.title("Circuito com Resistores em Série e Paralelo\n")
        ax.plot([-1, 0], [0, 0], 'k-')  # Linha inicial
        # ax.plot([self.x + 4*self.x_prox, self.x + 4*self.x_prox + 1], [0, y_ax], 'k-')  # Linha final

        for element in self.positions:
            self._draw_element(ax, *element)

        plt.show()

    def _calculate_positions(self, component, y):
        """Calcula as posições de cada componente e retorna a largura ocupada."""
        if isinstance(component, str):  # Resistor individual
            print(component, self.niveis[component][0], self.niveis[component][1])
            self.x = self.niveis[component][1]*2
            self.x_prox = (self.niveis[component][0] - self.niveis[component][1])/2
            self.positions.append(("resistor", self.x, y, self.x_prox, component))  # Inclui o nome do resistor
            return y

        tipo = component[0]
        if tipo == "S":  # Série
            for sub_component in component[1:]:
                self._calculate_positions(sub_component, y)
        elif tipo == "P":  # Paralelo
            subcomponents = component[1:]
            num_subcomponents = len(subcomponents)
            height_offset = 5  # Espaçamento vertical entre ramos

            # Determinar altura máxima (topo e base)
            top_y = y + (num_subcomponents - 1) * height_offset / 2
            bottom_y = y - (num_subcomponents - 1) * height_offset / 2

            # Adicionar linhas verticais iniciais e finais
            self.positions.append(("vertical", self.x, bottom_y, self.x_prox, top_y))
            
            # Calcular posições de cada ramo paralelo
            for i, sub_component in enumerate(subcomponents):
                sub_y = top_y - i * height_offset
                self._calculate_positions(sub_component, sub_y)

            # x_end = self.x + 3  # Espaço horizontal para os blocos paralelos
            self.positions.append(("vertical", self.x, bottom_y, self.x_prox, top_y))
        return y

    def _draw_element(self, ax, element_type, x, y, s, label=None):
        """Desenha um elemento com base em seu tipo e posições."""
        if element_type == "vertical":
            ax.plot([x+4*s, x+4*s], [y, label], 'k-')  # Linha vertical
        if element_type == "resistor":
            ax.plot([x, x + s], [y, y], 'k-')  # Fio antes do resistor
            ax.plot([x + s, x + 2.5*s], [y, y + 0.5], 'k-')  # Fio inclinado
            ax.plot([x + 2.5*s, x + 2.5*s], [y + 0.5, y - 0.5], 'k-', lw=2)  # Resistor
            ax.plot([x + 2.5*s, x + 3*s], [y - 0.5, y], 'k-')  # Fio inclinado
            ax.plot([x + 3*s, x + 4*s], [y, y], 'k-')  # Fio após o resistor
            ax.text(x + 2*s, y + 0.8, label, ha="center")  # Nome do resistor
