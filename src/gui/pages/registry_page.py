import customtkinter as ctk
from tkinter import ttk

from src.monitors.registry_monitor import (
    scan_registry
)


class RegistryPage(ctk.CTkFrame):

    def __init__(
        self,
        parent
    ):

        super().__init__(parent)

        self.create_table()

        self.refresh()

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
            "Registry Entry",
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        self.table.heading(
            "Registry Entry",
            text="Registry Entry"
        )

        self.table.column(
            "Registry Entry",
            width=1000,
            anchor="w"
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def refresh(self):

        self.table.delete(
            *self.table.get_children()
        )

        try:

            entries = scan_registry()

            for entry in entries:

                self.table.insert(
                    "",
                    "end",
                    values=(
                        str(entry),
                    )
                )

        except Exception as e:

            self.table.insert(
                "",
                "end",
                values=(
                    f"Registry Scan Error: {e}",
                )
            )

        self.after(
            10000,
            self.refresh
        )