import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        callback
    ):

        super().__init__(
            parent,
            width=220,
            corner_radius=0,
            fg_color="#121212"
        )

        self.callback = callback

        self.buttons = {}

        title = ctk.CTkLabel(

            self,

            text="🛡 ThreatGuard EDR",

            font=(
                "Segoe UI",
                22,
                "bold"
            ),

            text_color="#E0E0E0"

        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = ctk.CTkLabel(

            self,

            text="Endpoint Detection & Response",

            font=(
                "Segoe UI",
                11
            ),

            text_color="gray"

        )

        subtitle.pack(
            pady=(0, 20)
        )

        self.add_button(
            "Dashboard",
            "🏠 Dashboard"
        )

        self.add_button(
            "Processes",
            "🖥 Processes"
        )

        self.add_button(
            "Analytics",
            "📈 Analytics"
        )

        self.add_button(
            "Threats",
            "⚠ Threats"
        )

        self.add_button(
            "Threat Center",
            "🎯 Threat Center"
        )

        self.add_button(
            "Registry",
            "🗂 Registry"
        )

        self.add_button(
            "Reports",
            "📄 Reports"
        )

        self.highlight_page(
            "Dashboard"
        )

        spacer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        spacer.pack(
            expand=True,
            fill="both"
        )

        self.status_frame = ctk.CTkFrame(

            self,

            fg_color="#1B1B1B",

            corner_radius=10

        )

        self.status_frame.pack(

            fill="x",

            padx=10,

            pady=10

        )

        self.status_label = ctk.CTkLabel(

            self.status_frame,

            text=

            "Status: ACTIVE\n"
            "Processes: 0\n"
            "Threats: 0\n"
            "Last Scan: --",

            justify="left",

            anchor="w",

            text_color="#E0E0E0",

            font=(
                "Segoe UI",
                12
            )

        )

        self.status_label.pack(

            padx=10,

            pady=10,

            anchor="w"

        )

    def add_button(

        self,

        page_key,

        button_text

    ):

        btn = ctk.CTkButton(

            self,

            text=button_text,

            anchor="w",

            height=42,

            corner_radius=10,

            fg_color="#252526",

            hover_color="#303134",

            text_color="#E0E0E0",

            font=(
                "Segoe UI",
                14
            ),

            command=lambda:
            self.on_click(
                page_key
            )

        )

        btn.pack(

            fill="x",

            padx=10,

            pady=5

        )

        self.buttons[
            page_key
        ] = btn

    def on_click(

        self,

        page_name

    ):

        self.highlight_page(
            page_name
        )

        self.callback(
            page_name
        )

    def highlight_page(

        self,

        page_name

    ):

        for btn in self.buttons.values():

            btn.configure(

                fg_color="#252526",

                hover_color="#303134"

            )

        self.buttons[
            page_name
        ].configure(

            fg_color="#3A3D41",

            hover_color="#3A3D41"

        )

    def update_status(

        self,

        processes,

        threats,

        scan_time

    ):

        self.status_label.configure(

            text=

            f"Status: ACTIVE\n"

            f"Processes: {processes}\n"

            f"Threats: {threats}\n"

            f"Last Scan: {scan_time}"

        )