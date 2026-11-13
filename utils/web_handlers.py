from playwright.sync_api import Locator, Page, expect

import constant


class WebHandlers:
    def __init__(self, page: Page, parent_locator: dict):
        self.page = page
        self.parent_locator = parent_locator

    def _get_locator(self, element: str) -> Locator:
        locator = self.parent_locator[element]
        strategy = locator["strategy"]

        if strategy == "role":
            return self.page.get_by_role(locator["type"], name=locator["name"])

        if strategy == "label":
            return self.page.get_by_label(locator["name"])

        if strategy == "text":
            return self.page.get_by_text(locator["value"], exact=False)

        if strategy == "css":
            return self.page.locator(locator["value"])

        if strategy == "text_parent":
            return (
                self.page.get_by_text(locator["text"], exact=True)
                .locator("..")
                .locator(locator["child"])
            )

        raise ValueError(f"Unsupported locator strategy: {strategy}")

    # Basics
    def fill(self, element: str, value):
        self._get_locator(element).fill(str(value))

    def click(self, element: str):
        self._get_locator(element).click()

    def get_value(self, element: str) -> str:
        return self._get_locator(element).input_value()

    def get_text(self, element: str) -> str:
        return self._get_locator(element).inner_text()

    # DropDown
    def select(self, element: str, option: str):
        locator = self._get_locator(element)
        locator.click()

        options = self.page.get_by_role("option", name=option, exact=True)
        options.first.click()
        self.page.wait_for_timeout(constant.TIMEOUT)
        actual = locator.locator(".mat-mdc-select-min-line").inner_text().strip()
        assert actual == option, (
            f"Failed to select {option}. Actual selected value: {actual}"
        )

    def select_native(self, element: str, option: str) -> None:
        self._get_locator(element).select_option(label=option)

    def get_selected_option(self, element: str) -> str:
        return self._get_locator(element).input_value()

    # State Checks
    def is_visible(self, element: str) -> bool:
        return self._get_locator(element).is_visible()

    def is_enabled(self, element: str) -> bool:
        return self._get_locator(element).is_enabled()

    # Assertions / explicit waiting
    def expect_visible(self, element: str) -> None:
        expect(self._get_locator(element)).to_be_visible()

    def expect_text(self, element: str, expected: str) -> None:
        expect(self._get_locator(element)).to_have_text(expected)
