from selenium.webdriver.common.action_chains import ActionChains


class BrowserActions:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def hover(self, element):
        self.actions.move_to_element(element).perform()

    def double_click(self, element):
        self.actions.double_click(element).perform()

    def right_click(self, element):
        self.actions.context_click(element).perform()
