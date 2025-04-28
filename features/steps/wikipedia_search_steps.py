from behave import given, when, then
from selenium import webdriver
from pages.wikipedia_page import Wikipedia_Busqueda

@given('el usuario se encuentra en la pagina de inicio de Wikipedia')
def step_given_wikipedia_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://es.wikipedia.org/')
    context.wikipedia_page = Wikipedia_Busqueda(context.driver)

@when('el usuario escribe "Python (lenguaje de programación)"')
def step_when_wikipedia_search(context):
    context.wikipedia_page.search("Python (lenguaje de programación)")

@then('aparecen resultados que contienen el texto “Python”')
def step_then_wikipedia_search(context):
    assert "Python" in context.wikipedia_page.isElementPresent()