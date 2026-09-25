from playwright.sync_api import Page, Locator, expect


class WebHandlers:

    def __init__(self, page: Page, parent_locator: dict):
        self.page = page
        self.parent_locator = parent_locator

    def _get_locator(self, element: str) -> Locator:
        locator = self.parent_locator[element]
        strategy = locator["strategy"]

        if strategy == "role":
            return self.page.get_by_role(
                locator["type"],
                name=locator["name"]
            )

        if strategy == "label":
            return self.page.get_by_label(locator["name"])

        if strategy == "text":
            return self.page.get_by_text(
                locator["value"],
                exact=False
            )

        if strategy == "css":
            return self.page.locator(
                locator["value"]
            )
        
        if strategy == "text_parent":
            return (
                self.page.get_by_text(
                    locator["text"],
                    exact=True
                )
                .locator("..")
                .locator(locator["child"])
            )
                

        raise ValueError(
            f"Unsupported locator strategy: {strategy}"
        )

    def fill(self, element: str, value):
            locator = self._get_locator(element)
            locator.clear()
            locator.fill(str(value))

    def click(self, element: str):
        self._get_locator(element).click()

    def get_value(self, element: str) -> str:
        return self._get_locator(element).input_value()

    def get_text(self, element: str) -> str:
        return self._get_locator(element).inner_text()
    
    def select(self, element: str, option: str):
        locator = self._get_locator(element)
        locator.click()

        options = self.page.get_by_role("option", name=option, exact=True)
        self.page.pause()
        options.first.click()
        self.page.wait_for_timeout(500)
        actual = locator.locator(".mat-mdc-select-min-line").inner_text().strip()
        self.page.pause()
        assert actual == option, (
            f"Failed to select {option}. "
            f"Actual selected value: {actual}"
        )


    def is_visible(self, element: str) -> bool:
        locator = self._get_locator(element)
        expect(locator).to_be_visible()
        return True

    def is_enabled(self, element: str) -> bool:
        return self._get_locator(element).is_enabled()
