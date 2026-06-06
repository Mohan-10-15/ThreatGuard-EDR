import customtkinter as ctk


class StatusCard(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        title,
        value="0",
        color="#252526"
    ):

        super().__init__(
            parent,
            corner_radius=12,
            fg_color=color,
            width=220,
            height=120
        )

        self.pack_propagate(False)

        self.title = ctk.CTkLabel(

            self,

            text=title,

            font=(
                "Segoe UI",
                14
            ),

            text_color="#E0E0E0"

        )

        self.title.pack(
            pady=(18, 5)
        )

        self.value = ctk.CTkLabel(

            self,

            text=value,

            font=(
                "Segoe UI",
                36,
                "bold"
            ),

            text_color="white"

        )

        self.value.pack(
            pady=(0, 10)
        )

    def update_value(
        self,
        value
    ):

        self.value.configure(
            text=str(value)
        )