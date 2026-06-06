import customtkinter as ctk
from tkinter import ttk


class ThreatsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent
    ):

        super().__init__(parent)

        self.create_table()

    def create_table(self):

        style = ttk.Style()

        style.theme_use(
            "default"
        )

        style.configure(
            "Treeview",
            background="#1e1e1e",
            foreground="white",
            fieldbackground="#1e1e1e",
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            background="#2d2d2d",
            foreground="white"
        )

        columns = (

            "PID",

            "Process",

            "Threat Score",

            "Category",

            "Reputation"

        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        for col in columns:

            self.table.heading(
                col,
                text=col
            )

            self.table.column(
                col,
                width=180,
                anchor="center"
            )

        self.table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def populate(
        self,
        processes
    ):

        self.table.delete(
            *self.table.get_children()
        )

        for proc in processes:

            if proc["category"] not in [

                "HIGH",

                "CRITICAL"

            ]:

                continue

            self.table.insert(
                "",
                "end",
                values=(

                    proc["pid"],

                    proc["name"],

                    proc["score"],

                    proc["category"],

                    proc["reputation"]

                )
            )