from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_NEXT_BUTTON = (By.XPATH, './/div[contains(@class, "Order_NextButton")]/button[contains(text(), "Далее")]')
    FIELD_FIRSTNAME = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Имя")]')
    FIELD_SECONDNAME = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Фамилия")]')
    FIELD_ADDRESS = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Адрес: куда привезти заказ")]')
    FIELD_SUBWAY = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Станция метро")]')
    BUTTON_SUBWAY = [(By.XPATH, './/div[contains(@class, "select-search__select")]//div[contains(text(), "Бульвар Рокоссовского")]/parent::button'), (By.XPATH, './/div[contains(@class, "select-search__select")]//div[contains(text(), "Черкизовская")]/parent::button')]
    FIELD_PHONE = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Телефон")]')
    FIELD_DATE = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Когда привезти самокат")]')
    FIELD_RENTAL_PERIOD = (By.XPATH, './/div[contains(@class, "Dropdown-placeholder")]')
    DROP_MENU_PERIOD_BUTTON = (By.XPATH, './/div[contains(@class, "Dropdown-menu")]')
    DROP_MENU_PERIOD = [(By.XPATH, './/div[contains(@class, "Dropdown-option") and text()="двое суток"]'), (By.XPATH, './/div[contains(@class, "Dropdown-option") and text()="шестеро суток"]')]
    CHECKBOX_COLOR_SCOOTER = [(By.XPATH, './/div[contains(@class, "Order_Checkboxes")]//input[@id="black"]'), (By.XPATH, './/div[contains(@class, "Order_Checkboxes")]//input[@id="grey"]')]
    FIELD_COMMENT_FOR_DELIVERY = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Комментарий для курьера")]')
    ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')
    YES_BUTTON = (By.XPATH, './/div[contains(@class, "Order_Buttons")]//button[text()="Да"]')
    ORDER_COMPLETED_TEXT = (By.XPATH, './/div[contains(@class, "Order_ModalHeader")]')


