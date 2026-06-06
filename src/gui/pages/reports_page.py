import customtkinter as ctk
from tkinter import messagebox
import os

from src.reporting.pdf_report import (
    generate_report
)

from src.monitors.process_monitor import (
    get_dashboard_stats
)


class ReportsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent
    ):

        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="ThreatGuard Reports Center",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(
            pady=20
        )

        self.report_btn = ctk.CTkButton(
            self,
            text="Generate PDF Report",
            command=self.generate_pdf
        )

        self.report_btn.pack(
            pady=10
        )

        self.log_btn = ctk.CTkButton(
            self,
            text="Open Incident Log",
            command=self.open_log
        )

        self.log_btn.pack(
            pady=10
        )

        self.export_btn = ctk.CTkButton(
            self,
            text="Export Threat Data",
            command=self.export_data
        )

        self.export_btn.pack(
            pady=10
        )

        self.status = ctk.CTkTextbox(
            self,
            height=250
        )

        self.status.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def generate_pdf(self):

        try:

            stats = get_dashboard_stats()

            filename = generate_report(
                stats
            )

            self.status.insert(
                "end",
                f"PDF Generated: {filename}\n"
            )

            messagebox.showinfo(
                "Success",
                "PDF Report Generated"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def open_log(self):

        log_file = "incident_log.txt"

        if not os.path.exists(
            log_file
        ):

            self.status.insert(
                "end",
                "incident_log.txt not found\n"
            )

            return

        try:

            os.startfile(
                log_file
            )

            self.status.insert(
                "end",
                "Incident Log Opened\n"
            )

        except Exception as e:

            self.status.insert(
                "end",
                f"{e}\n"
            )

    def export_data(self):

        self.status.insert(
            "end",
            "Threat Data Exported\n"
        )