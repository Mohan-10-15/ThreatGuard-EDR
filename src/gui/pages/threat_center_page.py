import customtkinter as ctk
from tkinter import ttk


class ThreatCenterPage(
    ctk.CTkFrame
):

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent
        )

        title = ctk.CTkLabel(

            self,

            text="Threat Center",

            font=(
                "Segoe UI",
                24,
                "bold"
            )

        )

        title.pack(
            pady=10
        )

        columns = (

            "PID",

            "Process",

            "Score",

            "Category",

            "IOC",

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
                width=150,
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

            if (

                proc["category"]

                not in [

                    "HIGH",

                    "CRITICAL"

                ]

            ):

                continue

            self.table.insert(

                "",

                "end",

                values=(

                    proc["pid"],

                    proc["name"],

                    proc["score"],

                    proc["category"],

                    proc["ioc_match"],

                    proc["reputation"]

                )

            )