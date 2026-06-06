import customtkinter as ctk
from tkinter import ttk

from src.incidents.incident_engine import (
    get_incidents
)


class IncidentsPage(
    ctk.CTkFrame
):

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent
        )

        columns = (

            "Time",

            "Event",

            "Process",

            "Details"

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
                width=250
            )

        self.table.pack(
            fill="both",
            expand=True
        )

        self.refresh()

    def refresh(self):

        self.table.delete(
            *self.table.get_children()
        )

        incidents = (
            get_incidents()
        )

        for incident in incidents:

            self.table.insert(

                "",

                "end",

                values=(

                    incident["time"],

                    incident["event"],

                    incident["process"],

                    incident["details"]

                )

            )

        self.after(
            5000,
            self.refresh
        )