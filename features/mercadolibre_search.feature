Feature: Busqueda en Mercadolibre
  Scenario: Busqueda de "iPhone 13" en Mercadolibre
    Given el usuario se encuentra en la pagina de inicio de Mercadolibre
    When el usuario escribe "iPhone 13"
    Then aparecen resultados que contienen el texto “iPhone”
