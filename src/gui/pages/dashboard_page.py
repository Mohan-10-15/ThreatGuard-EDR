import customtkinter as ctk

from src.gui.cards import StatusCard
from src.gui.charts import LiveChart


class DashboardPage(ctk.CTkFrame):

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent
        )

        self.create_header()

        self.create_cards()

        self.create_charts()

    def create_header(
        self
    ):

        title = ctk.CTkLabel(

            self,

            text="Security Overview",

            font=(
                "Segoe UI",
                28,
                "bold"
            )

        )

        title.pack(
            pady=(10, 5)
        )

        subtitle = ctk.CTkLabel(

            self,

            text=
            "Real-time endpoint monitoring and threat visibility",

            text_color="gray"

        )

        subtitle.pack(
            pady=(0, 10)
        )

    def create_cards(
        self
    ):

        card_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        card_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.cpu_card = StatusCard(
            card_frame,
            "CPU %",
            color="#252526"
        )

        self.cpu_card.pack(
            side="left",
            padx=10,
            pady=10
        )

        self.ram_card = StatusCard(
            card_frame,
            "RAM %",
            color="#252526"
        )

        self.ram_card.pack(
            side="left",
            padx=10,
            pady=10
        )

        self.threat_card = StatusCard(
            card_frame,
            "Threats",
            color="#252526"
        )

        self.threat_card.pack(
            side="left",
            padx=10,
            pady=10
        )

        self.critical_card = StatusCard(
            card_frame,
            "Critical",
            color="#252526"
        )

        self.critical_card.pack(
            side="left",
            padx=10,
            pady=10
        )

        self.registry_card = StatusCard(
            card_frame,
            "Registry",
            color="#252526"
        )

        self.registry_card.pack(
            side="left",
            padx=10,
            pady=10
        )

    def create_charts(
        self
    ):

        chart_frame = ctk.CTkFrame(
            self,
            fg_color="#1B1B1B"
        )

        chart_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        left_frame = ctk.CTkFrame(
            chart_frame,
            fg_color="#202020"
        )

        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        right_frame = ctk.CTkFrame(
            chart_frame,
            fg_color="#202020"
        )

        right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        cpu_title = ctk.CTkLabel(

            left_frame,

            text=
            "Live CPU Utilization (%)",

            font=(
                "Segoe UI",
                16,
                "bold"
            )

        )

        cpu_title.pack(
            pady=(10, 0)
        )

        cpu_desc = ctk.CTkLabel(

            left_frame,

            text=
            "Real-time processor activity",

            text_color="gray"

        )

        cpu_desc.pack()

        ram_title = ctk.CTkLabel(

            right_frame,

            text=
            "Live Memory Utilization (%)",

            font=(
                "Segoe UI",
                16,
                "bold"
            )

        )

        ram_title.pack(
            pady=(10, 0)
        )

        ram_desc = ctk.CTkLabel(

            right_frame,

            text=
            "Real-time RAM usage",

            text_color="gray"

        )

        ram_desc.pack()

        self.cpu_chart = LiveChart(
            left_frame,
            "CPU"
        )

        self.ram_chart = LiveChart(
            right_frame,
            "RAM"
        )

    def update_stats(
        self,
        stats,
        metrics
    ):

        self.cpu_card.update_value(
            f"{metrics['cpu']}%"
        )

        self.ram_card.update_value(
            f"{metrics['memory']}%"
        )

        self.threat_card.update_value(
            stats["threats_detected"]
        )

        self.critical_card.update_value(
            stats["critical_threats"]
        )

        self.registry_card.update_value(
            stats["registry_entries"]
        )

        if stats["critical_threats"] > 0:

            self.critical_card.configure(
                fg_color="#8B0000"
            )

        else:

            self.critical_card.configure(
                fg_color="#252526"
            )

        self.cpu_chart.update_chart(
            metrics["cpu"]
        )

        self.ram_chart.update_chart(
            metrics["memory"]
        )