class PageManager:

    def __init__(self):

        self.pages = {}

    def add_page(
        self,
        name,
        page
    ):

        self.pages[name] = page

    def show_page(
        self,
        name
    ):

        for page in self.pages.values():

            page.pack_forget()

        self.pages[name].pack(
            fill="both",
            expand=True
        )