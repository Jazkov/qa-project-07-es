import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado "
                            "el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi = (By.CLASS_NAME, 'button round')
    comfort_type = (By.CSS_SELECTOR, 'tcard-title')
    phone_number_text = (By.CSS_SELECTOR, 'np-text')
    close_button = (By.CSS_SELECTOR, 'close-button section-close')
    pay_button = (By.CSS_SELECTOR, 'pp-button filled')
    select_card = (By.CSS_SELECTOR, 'pp-title')
    card_pay = (By.CSS_SELECTOR, 'pp-row disabled')
    number = (By.ID, 'number')
    code = (By.ID, 'code')
    remove_focus = (By.CSS_SELECTOR, 'head')
    add_button = (By.CSS_SELECTOR, 'button full')
    comment_button = (By.ID, 'comment')
    requisites = (By.CSS_SELECTOR, 'reqs-header')
    items = (By.CSS_SELECTOR, 'r-sw-label')
    ice_cream = (By.CSS_SELECTOR, 'counter-value')
    modal_taxi = (By.CSS_SELECTOR, 'smart-button-secondary')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def tap_comfort(self):
        self.driver.find_element(*self.order_taxi).click()
        WebDriverWait(self.driver, 3)
        self.driver.find_element(self.comfort_type).click()

    def phone_number(self):
        self.driver.find_element(*self.phone_number_text).click()
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.phone_number_text).send_keys(data.PHONE_NUMBER)
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.close_button).click()
        assert UrbanRoutesPage.phone_number_text == data.PHONE_NUMBER

    def add_card(self):
        self.driver.find_element(*self.pay_button).click()
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.number).send_keys(data.CARD_NUMBER)
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.code).send_keys(data.CARD_CODE)
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.remove_focus).click()
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.add_button).click()
        self.driver.find_element(self.close_button).click()
        assert UrbanRoutesPage.number == data.CARD_NUMBER
        assert UrbanRoutesPage.code == data.CARD_CODE

    def driver_comment(self):
        self.driver.find_element(*self.comment_button).click()
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.comment_button).send_keys(data.MESSAGE_FOR_DRIVER)
        assert UrbanRoutesPage.comment_button == data.MESSAGE_FOR_DRIVER

    def ask_for_items(self):
        self.driver.find_element(*self.requisites).click()
        WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.items).click()

    def order_ice_cream(self):
        self.driver.find_element(self.ice_cream).click()
        WebDriverWait(self.driver, 3)
        for _ in range(2):
            self.driver.find_element(*self.requisites).click()
        WebDriverWait(self.driver, 3)

    def smart_button(self):
        self.driver.find_element(*self.modal_taxi).click()