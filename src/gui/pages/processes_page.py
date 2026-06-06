import customtkinter as ctk
from tkinter import ttk


class ProcessesPage(ctk.CTkFrame):

    def __init__(
        self,
        parent
    ):

        super().__init__(parent)

        self.search_var = ctk.StringVar()

        self.create_search()

        self.create_table()

        self.create_buttons()

    def create_search(self):

        search_frame = ctk.CTkFrame(
            self
        )

        search_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        search_box = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search Process...",
            textvariable=self.search_var,
            height=35
        )

        search_box.pack(
            fill="x",
            padx=10,
            pady=10
        )

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

            "CPU %",

            "Memory %",

            "Connections",

            "Threat %",

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
                width=140,
                anchor="center"
            )

        self.table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def create_buttons(self):

        button_frame = ctk.CTkFrame(
            self
        )

        button_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.quarantine_btn = ctk.CTkButton(
            button_frame,
            text="Quarantine"
        )

        self.quarantine_btn.pack(
            side="left",
            padx=5
        )

        self.tree_btn = ctk.CTkButton(
            button_frame,
            text="Process Tree"
        )

        self.tree_btn.pack(
            side="left",
            padx=5
        )

    def populate(
        self,
        processes
    ):

        self.table.delete(
            *self.table.get_children()
        )

        search_text = (
            self.search_var.get()
            .lower()
            .strip()
        )

        for proc in processes:

            if (
                search_text
                and search_text not in
                proc["name"].lower()
            ):
                continue

            self.table.insert(
                "",
                "end",
                values=(

                    proc["pid"],

                    proc["name"],

                    round(
                        proc["cpu"],
                        2
                    ),

                    round(
                        proc["memory"],
                        2
                    ),

                    proc["connections"],

                    proc["score"],

                    proc["category"],

                    proc["reputation"]

                )
            )