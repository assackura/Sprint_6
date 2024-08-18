from selenium.webdriver.common.by import By


class BasePageLocators:

    SCOOTER_LOGO = (By.XPATH, './/div[contains(@class, "Header_Logo")]/a[contains(@class, "Scooter")]')
    YANDEX_LOGO = (By.XPATH, './/div[contains(@class, "Header_Logo")]/a[contains(@class, "Yandex")]')
    UP_ORDER_BUTTON_MAIN_PAGE = (By.XPATH, './/div[contains(@class, "Header_Nav")]/button[contains(text(), "Заказать")]')