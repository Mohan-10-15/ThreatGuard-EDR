import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class LiveChart:

    def __init__(
        self,
        parent,
        title
    ):

        self.figure = Figure(
            figsize=(4, 3),
            dpi=100
        )

        self.ax = self.figure.add_subplot(
            111
        )

        self.ax.set_title(
            title
        )

        self.ax.set_facecolor(
            "#1e1e1e"
        )

        self.figure.patch.set_facecolor(
            "#1e1e1e"
        )

        self.ax.tick_params(
            colors="white"
        )

        self.data = [0]

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=parent
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def update_chart(
        self,
        value
    ):

        self.data.append(value)

        if len(self.data) > 20:
            self.data.pop(0)

        self.ax.clear()

        self.ax.set_facecolor(
            "#1e1e1e"
        )

        self.ax.plot(
            self.data,
            linewidth=2
        )

        self.canvas.draw()