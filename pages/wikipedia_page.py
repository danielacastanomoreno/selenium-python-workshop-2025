from selenium.webdriver.common.by import By
import time
from .base_page import BasePage


class Wikipedia_Busqueda(BasePage):
    ACTIVATE_SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/a')
    SEARCH_FIELD = (By.NAME, 'search')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/button')
    RESULTS_TITLE = (By.ID, 'firstHeading')

    def search(self, tema_a_buscar):
        self.click(self.ACTIVATE_SEARCH_BUTTON)
        self.enter_text(self.SEARCH_FIELD, tema_a_buscar)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.RESULTS_TITLE)
        texto = elemento.text
        return texto
