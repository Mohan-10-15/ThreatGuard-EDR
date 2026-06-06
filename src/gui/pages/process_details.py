import customtkinter as ctk


class ProcessDetailsWindow(
    ctk.CTkToplevel
):

    def __init__(
        self,
        parent,
        process_data
    ):

        super().__init__(
            parent
        )

        self.title(
            "Process Details"
        )

        self.geometry(
            "900x650"
        )

        self.resizable(
            False,
            False
        )

        title = ctk.CTkLabel(

            self,

            text=
            f"Process: {process_data['name']}",

            font=(
                "Segoe UI",
                22,
                "bold"
            )

        )

        title.pack(
            pady=15
        )

        textbox = ctk.CTkTextbox(
            self
        )

        textbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        details = f"""
PID:
{process_data.get('pid','N/A')}

Path:
{process_data.get('path','N/A')}

SHA256:
{process_data.get('sha256','N/A')}

CPU:
{process_data.get('cpu','N/A')}

Memory:
{process_data.get('memory','N/A')}

Connections:
{process_data.get('connections','N/A')}

Threat Score:
{process_data.get('score','N/A')}

Threat Category:
{process_data.get('category','N/A')}

Reputation:
{process_data.get('reputation','N/A')}

IOC Match:
{process_data.get('ioc_match','N/A')}

IOC Severity:
{process_data.get('ioc_severity','N/A')}

Behavior Score:
{process_data.get('behavior_score','N/A')}

Behavior Reasons:
{process_data.get('behavior_reasons','N/A')}
"""

        textbox.insert(
            "1.0",
            details
        )

        textbox.configure(
            state="disabled"
        )