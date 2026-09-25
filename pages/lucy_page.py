from data.locators import LUCY_LOCATORS
from utils.web_handlers import WebHandlers


class LucyPage:

    def __init__(self, page):
        self.page = page
        self.web_handlers = WebHandlers(
            self.page,
            LUCY_LOCATORS
        )

    def is_loaded(self):
        return self.web_handlers.is_visible(
            "start_heading"
        )