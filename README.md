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

EJECUCIÓN DE PRUEBAS 

Para ejecutar las pruebas se requirio importar Selenium Webdriver, importar datos de data.py y los archivos que se 
encuentarn en UrbanRoutesPage.

Se utilizaron los métodos definidos en el archivo UrbanRoutesPage con sus localizadores y sus esperas dependiendo 
la prueba.

Para la prueba test_set_route se utilizaron localizadores ID para la opción "desde" y "hasta" así como también la 
URL de la pagina UrbanRoutes, se envió la infomación de las direcciones para desde y hasta con .send_keys también 
utilizando return para recuperar dichas direcciones.

Para la prueba test_select_comfort se utilizaron los localizadores de CLASS_NAME Y CSS_SELECTOR, y una espera de 3 
segundos después de cliquear para la selcción  del taxi y elegir la clase comfort.

Para la prueba test_phone_number se utilizó el localizador CSS_SELECTOR una espera de 3 segundos para dar click en el 
botón de número de teléfono y otra espera para recibir la informacíón del número de teléfono utilizando .send_keys.

Para las pruebas test_add_card se utilizaron localizadores CSS_SELCTOR y ID, al dar click sobre el botón de pay_buton 
se dio una espera de 3 segundos para que apareciera el apartado de la tarjeta y 3 segundos para recibir la información
del número de tarjeta y del código utilizando .send_keys para recibir la infromación de data.py, el botón de agregar 
tarjeta no se habilitaba hasta que perdiera el enfoque así que se simuló un click en la parte del encabezado para poder
clicquear el botón de agregar tarjeta.

Para la prueba de tes_driver_comment se utilizó un localidar ID, clicamos el botón de mensaje para el conductor y 
con .send_keys enviamos el mensaje que tenemos en el archivo data.py, utilizamos una espera de 3 segundos.

Para la prueba de test_ask_for_items utilizamos los localizadores de CSS_SELECTOR y cliqueamos en los requisitos del 
pedido para pedir manta y pañuelos.

Para la prueba test_order_ice_cream se utilizó el localizador CSS_SELECTOR para pedir 2 helados, para esta prueba se
usó un bucle "for" para hacer 2 clics y pedir los dos helados.

Finalmente para la prueba de test_smart_button se utilizó un localizador CSS_SELECTOR para dar clic sobre el botón
para solicitar al conductor.





