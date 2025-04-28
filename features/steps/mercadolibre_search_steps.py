from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_page import Mercadolibre_Busqueda

@given('el usuario se encuentra en la pagina de inicio de Mercadolibre')
def step_given_mercadolibre_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.mercadolibre_page = Mercadolibre_Busqueda(context.driver)

@when('el usuario escribe "iPhone 13"')
def step_when_mercadolibre_search(context):
    context.mercadolibre_page.search("iPhone 13")

@then('aparecen resultados que contienen el texto “iPhone”')
def step_then_mercadolibre_search(context):
    assert "iPhone" in context.mercadolibre_page.isElementPresent()