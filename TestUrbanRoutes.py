import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de
        # confirmación del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDREES_TO
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort(self):
        comfort_tap = UrbanRoutesPage.tap_comfort
        assert UrbanRoutesPage.tap_comfort == comfort_tap

    def test_phone_number(self):
        put_phone_number = UrbanRoutesPage.phone_number
        assert UrbanRoutesPage.phone_number == put_phone_number

    def test_add_card(self):
        put_add_card = UrbanRoutesPage.add_card
        assert UrbanRoutesPage.add_card == put_add_card

    def test_driver_comment(self):
        write_driver_comment = UrbanRoutesPage.driver_comment
        assert UrbanRoutesPage.driver_comment == write_driver_comment

    def test_ask_for_items(self):
        get_items = UrbanRoutesPage.ask_for_items
        assert UrbanRoutesPage.ask_for_items == get_items

    def test_order_ice_cream(self):
        get_ice_cream = UrbanRoutesPage.order_ice_cream
        assert UrbanRoutesPage.order_ice_cream == get_ice_cream

    def test_smart_button(self):
        push_smart_button = UrbanRoutesPage.smart_button
        assert UrbanRoutesPage.smart_button == push_smart_button

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()