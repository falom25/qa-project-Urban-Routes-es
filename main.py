import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# No modificar
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
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
    return code

# Localizadores
class UrbanRoutesPage:
# Direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_for_taxi_button = (By.XPATH, '//button[@type="button" and @class="button round" and text()="Pedir un taxi"]')
    comfort_rate_button = (By.XPATH, '//div[@class="tcard-icon"]/img[@alt="Comfort"]')
# Numero de telefono
    phone_number_area = (By.CSS_SELECTOR, "div.np-text")
    phone_number_label = (By.CSS_SELECTOR, "label[for='phone']")
    phone_number_input = (By.CSS_SELECTOR, "input#phone")
    next_button = (By.CSS_SELECTOR, "button.button.full")
    phone_number_display = (By.XPATH, "//div[@class='np-text' and text()='+1 123 123 12 12']")
# Codigo de telefono
    code_label = (By.CSS_SELECTOR, "label[for='code']")
    code_input = (By.CSS_SELECTOR, "input#code")
    submit_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'button full') and text()='Confirmar']")
# Metodo de pago
    payment_method_button = (By.XPATH, '//div[@class="pp-text" and text()="Método de pago"]')
    add_credit_card_button = (By.XPATH, '//img[@class="pp-plus" and @alt="plus"]')
    credit_card_number_field = (By.ID, 'number')
    cvv_field = (By.CSS_SELECTOR, "div.card-code-input input.card-input")
    outside_click_area = (By.CSS_SELECTOR, "div.plc")
    add_card_button = (By.XPATH, '//button[@type="submit" and @class="button full" and text()="Agregar"]')
    close_button_payment_method = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    payment_method_card_label = (By.XPATH, '//div[@class="pp-value-text" and text()="Tarjeta"]')
# Mensaje para el conductor
    label_for_comment = (By.CSS_SELECTOR, 'label[for="comment"].label')
    message_to_driver_field = (By.ID, "comment")
# Helados
    ice_cream_plus_button = (By.XPATH,
                             "//div[@class='r-counter-label' and text()='Helado']/following-sibling::div[@class='r-counter']//div[@class='counter-plus']")
    ice_cream_counter = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/following-sibling::div[@class='r-counter']//div[contains(@class, 'counter-value')]")
# Manta y panuelos
    blanket_and_tissues_switch = (By.CSS_SELECTOR, "div.switch")
    blanket_and_tissues_checkbox = (By.CSS_SELECTOR, "div.switch input.switch-input")
# Pedir taxi e informacion
    request_taxi_button = (By.XPATH, "//button[@type='button' and .//span[text()='Pedir un taxi']]")
    order_popup = (
    By.XPATH, "//div[@class='order-body']//div[@class='order-header-title' and text()='Buscar automóvil']")
    driver_info = (By.XPATH, "//div[@class='order-header-title' and contains(text(), 'El conductor llegará en')]")

# Metodos
    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def open_taxi_modal(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.ask_for_taxi_button)).click()
        time.sleep(1)

    def select_comfort_rate(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.comfort_rate_button)).click()
        time.sleep(1)

    def add_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.phone_number_area)).click()
        wait.until(EC.element_to_be_clickable(self.phone_number_label)).click()
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)
        wait.until(EC.element_to_be_clickable(self.next_button)).click()
        time.sleep(2)

    def add_phone_code(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.code_label)).click()
        self.driver.find_element(*self.code_input).send_keys(retrieve_phone_code(self.driver))
        wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        time.sleep(2)

    def add_credit_card(self, card_number, cvv):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()
        wait.until(EC.element_to_be_clickable(self.add_credit_card_button)).click()

        credit_card_field = self.driver.find_element(*self.credit_card_number_field)
        credit_card_field.click()
        credit_card_field.send_keys(card_number)

        cvv_field = self.driver.find_element(*self.cvv_field)
        cvv_field.click()
        cvv_field.send_keys(cvv)
        time.sleep(2)

        self.driver.find_element(*self.outside_click_area).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.close_button_payment_method).click()
        time.sleep(2)

    def verify_credit_card_added(self):
        wait = WebDriverWait(self.driver, 10)
        payment_method_card_element = wait.until(EC.visibility_of_element_located(self.payment_method_card_label))
        return payment_method_card_element.is_displayed()

    def message_to_driver(self, message):
        label_field = self.driver.find_element(*self.label_for_comment)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", label_field)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.label_for_comment))
        label_field.click()
        message_field = self.driver.find_element(*self.message_to_driver_field)
        message_field.send_keys(message)
        time.sleep(2)

    def order_ice_creams(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.ice_cream_plus_button)).click()
        wait.until(EC.element_to_be_clickable(self.ice_cream_plus_button)).click()
        time.sleep(2)

    def order_blanket_and_tissues(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_switch)).click()
        time.sleep(2)

    def request_taxi(self):
        self.driver.find_element(*self.request_taxi_button).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.order_popup))
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.driver_info))
        time.sleep(2)

    def wait_for_driver_info_modal(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.driver_info_modal))
        time.sleep(2)

# Pruebas
class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.maximize_window()
        self.driver.get(data.urban_routes_url)
        time.sleep(5)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        # Añadir las siguientes líneas para obtener los valores de los campos de dirección y verificar la aserción
        from_value = self.driver.find_element(*routes_page.from_field).get_attribute("value")
        to_value = self.driver.find_element(*routes_page.to_field).get_attribute("value")
        assert from_value == address_from
        assert to_value == address_to
        time.sleep(2)

    def test_open_taxi_modal_and_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_taxi_modal()
        routes_page.select_comfort_rate()

    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.add_phone_number(phone_number)
        # Validacion
        current_value = self.driver.find_element(*routes_page.phone_number_input).get_attribute("value")
        assert current_value == phone_number

    def test_add_phone_code(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_phone_code()
        phone_number = data.phone_number
        # Validacion
        displayed_phone_number = self.driver.find_element(*routes_page.phone_number_display).text
        assert displayed_phone_number == phone_number, f"Esperado: {phone_number}, Actual: {displayed_phone_number}"

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        cvv = data.card_code
        routes_page.add_credit_card(card_number, cvv)
        # Validacion
        assert routes_page.verify_credit_card_added()

    def test_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.message_to_driver(message_for_driver)
        # Validacion
        displayed_message = self.driver.find_element(*routes_page.message_to_driver_field).get_attribute("value")
        assert displayed_message == message_for_driver

    def test_order_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_ice_creams()
        # Validacion
        ice_cream_counter_element = self.driver.find_element(*routes_page.ice_cream_counter)
        counter_value = ice_cream_counter_element.text
        assert counter_value == "2"

    def test_blanket_and_tissues_switch(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_tissues()
        # Validacion
        checkbox_element = self.driver.find_element(*routes_page.blanket_and_tissues_checkbox)
        return checkbox_element.is_selected()

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()
        # Verificacion
        driver_info_element = self.driver.find_element(*routes_page.driver_info)
        assert driver_info_element.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()