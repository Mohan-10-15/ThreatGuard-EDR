import customtkinter as ctk

from src.gui.charts import LiveChart


class AnalyticsPage(
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

            text="Analytics Dashboard",

            font=(
                "Segoe UI",
                24,
                "bold"
            )

        )

        title.pack(
            pady=(10, 5)
        )

        description = ctk.CTkLabel(

            self,

            text=
            "Real-time system performance monitoring "
            "(updates every 3 seconds)",

            text_color="gray"

        )

        description.pack(
            pady=(0, 10)
        )

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

        left = ctk.CTkFrame(
            chart_frame,
            fg_color="#202020"
        )

        left.pack(

            side="left",

            fill="both",

            expand=True,

            padx=5,

            pady=5

        )

        right = ctk.CTkFrame(
            chart_frame,
            fg_color="#202020"
        )

        right.pack(

            side="right",

            fill="both",

            expand=True,

            padx=5,

            pady=5

        )

        cpu_label = ctk.CTkLabel(

            left,

            text=
            "Live CPU Utilization (%)",

            font=(
                "Segoe UI",
                16,
                "bold"
            )

        )

        cpu_label.pack(
            pady=(10, 0)
        )

        cpu_subtitle = ctk.CTkLabel(

            left,

            text=
            "Real-time processor usage",

            text_color="gray"

        )

        cpu_subtitle.pack()

        ram_label = ctk.CTkLabel(

            right,

            text=
            "Live Memory Utilization (%)",

            font=(
                "Segoe UI",
                16,
                "bold"
            )

        )

        ram_label.pack(
            pady=(10, 0)
        )

        ram_subtitle = ctk.CTkLabel(

            right,

            text=
            "Real-time RAM usage",

            text_color="gray"

        )

        ram_subtitle.pack()

        self.cpu_chart = LiveChart(
            left,
            "CPU"
        )

        self.ram_chart = LiveChart(
            right,
            "RAM"
        )

    def update_metrics(
        self,
        metrics
    ):

        self.cpu_chart.update_chart(
            metrics["cpu"]
        )

        self.ram_chart.update_chart(
            metrics["memory"]
        )