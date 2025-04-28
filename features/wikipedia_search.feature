Feature: Busqueda en Wikipedia
  Scenario: Busqueda de "Python (lenguaje de programación)" en Wikipedia
    Given el usuario se encuentra en la pagina de inicio de Wikipedia
    When el usuario escribe "Python (lenguaje de programación)"
    Then aparecen resultados que contienen el texto “Python”
