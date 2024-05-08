Jahaziel Ebed Kolansinsky Victoria 
Cohort 08
Sprint 07

"Pruebas automatizdas para Urban Routes"

DESCRICIÓN 

Dentro de esta prueba automatizada se busca pedir un taxi de tipo comfort en el cual 
sea agregada una dirección utilizando los espacios "desde" y "hasta", agregar un número 
de teléfono, número de tarjeta, código de la tarjeta y dejar un mensaje para el conductor.

Dentro de los requisitos se solicita pedir una manta y pañuelo así como 2 helados, 
una vez que se haya solicitados todos los requisitos se llama al taxi y se espera para visualizar
el tiempo de llegada y el conductor.

TECNOLOGÍAS UTILIZADAS

Para desarrollar estas pruebas se utilizó lenguaje Python  con tecnologías de pruebas Selenium y Pytest

Previamnnte se descargó el repositorio del proyecto 07 de la página de GitHub y fue descargado instalo 
la paqueteria de Pytest y Selenium.

Dentro del proyecto se crearon 3 archivos, data.py, UrbanroutesPage.py y TestUrbanRoutes.py

ARCHIVO DATA:PY

En el archivo data.py se guardo la URL de la pagina, el número de teléfono , número de tarjeta, 
mensaje para el conductor y direcciones que se utilizarían para la pruebas.

ARCHIVO URBANROUTESPAGE.PY 

En el archivo de UrbanRoutesPage.py se utilizó para escribir los localizadores y los métodos, los localizadores 
que se utilizarón fueron CSS_SELECTOR, ID y CLASS_NAME,
Dentro de los los métodos se utilizarón esperas de 3 segundos para ejecturar pruebas que tuviensen que esperar 
para agregar el texto, número y mensaje para el conductor.

ARCHIVO TESTURBANROUTES.PY

Se utilizó para las pruebas que se ejecutarían para la prueba automatizada, un método de clase para interseptar 
el código de teléfono y teardown para cerrar la prueba una vez se haya terminado de realizar la prueba.