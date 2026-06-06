import customtkinter as ctk

from datetime import datetime

from src.gui.sidebar import Sidebar
from src.gui.page_manager import PageManager

from src.gui.pages.dashboard_page import DashboardPage
from src.gui.pages.processes_page import ProcessesPage
from src.gui.pages.analytics_page import AnalyticsPage
from src.gui.pages.threats_page import ThreatsPage
from src.gui.pages.threat_center_page import (
    ThreatCenterPage
)
from src.gui.pages.registry_page import RegistryPage
from src.gui.pages.reports_page import ReportsPage

from src.monitors.process_monitor import (
    scan_processes,
    get_latest_data,
    get_dashboard_stats
)

from src.monitors.system_monitor import (
    get_system_metrics
)


class Dashboard:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title(
            "ThreatGuard EDR"
        )

        self.root.geometry(
            "1800x1000"
        )

        self.sidebar = Sidebar(
            self.root,
            self.show_page
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content_frame = ctk.CTkFrame(
            self.root
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.page_manager = PageManager()

        self.dashboard_page = DashboardPage(
            self.content_frame
        )

        self.processes_page = ProcessesPage(
            self.content_frame
        )

        self.analytics_page = AnalyticsPage(
            self.content_frame
        )

        self.threats_page = ThreatsPage(
            self.content_frame
        )

        self.threat_center_page = (
            ThreatCenterPage(
                self.content_frame
            )
        )

        self.registry_page = RegistryPage(
            self.content_frame
        )

        self.reports_page = ReportsPage(
            self.content_frame
        )

        self.page_manager.add_page(
            "Dashboard",
            self.dashboard_page
        )

        self.page_manager.add_page(
            "Processes",
            self.processes_page
        )

        self.page_manager.add_page(
            "Analytics",
            self.analytics_page
        )

        self.page_manager.add_page(
            "Threats",
            self.threats_page
        )

        self.page_manager.add_page(
            "Threat Center",
            self.threat_center_page
        )

        self.page_manager.add_page(
            "Registry",
            self.registry_page
        )

        self.page_manager.add_page(
            "Reports",
            self.reports_page
        )

        self.page_manager.show_page(
            "Dashboard"
        )

        self.refresh()
    def show_page(
        self,
        page_name
        ):

        self.page_manager.show_page(
            page_name
        )

    def refresh(self):

        scan_processes()

        processes = get_latest_data()

        stats = get_dashboard_stats()

        metrics = get_system_metrics()

        self.sidebar.update_status(

            stats[
                "processes_scanned"
            ],

            stats[
                "threats_detected"
            ],

            datetime.now().strftime(
                "%H:%M:%S"
            )

        )

        self.dashboard_page.update_stats(
            stats,
            metrics
        )

        self.analytics_page.update_metrics(
            metrics
        )

        self.processes_page.populate(
            processes
        )

        self.threats_page.populate(
            processes
        )

        self.threat_center_page.populate(
            processes
        )

        self.root.after(
            3000,
            self.refresh
        )

    def run(self):

        self.root.mainloop()