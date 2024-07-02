# Proyecto de Automatización de Pruebas con Selenium

## Descripción del Proyecto
Este proyecto tiene como objetivo automatizar pruebas utilizando Selenium para una aplicación web de rutas urbanas. Se implementan diversas funcionalidades como la solicitud de taxis, manejo de métodos de pago y comunicación con conductores.

## Tecnologías y Técnicas Utilizadas
- **Selenium WebDriver**: Utilizado para la automatización de pruebas interactivas en el navegador web.
- **Python**: Lenguaje de programación principal para escribir scripts de automatización.
- **Selectors**: Utilizados para localizar elementos en la interfaz de usuario.
- **WebDriverWait y Expected Conditions**: Utilizados para esperas explícitas y condiciones esperadas durante la ejecución de pruebas.

## Instrucciones para Ejecutar las Pruebas
1. **Configuración del Entorno:**
   - Asegúrate de tener Python instalado en tu sistema.
   - Instala Selenium, pytest y otras dependencias necesarias usando pip:
     ```bash
     pip install selenium pytest
     ```

2. **Configuración del Proyecto:**
   - Clona este repositorio desde GitHub:
     ```bash
     git clone https://github.com/tu-usuario/qa-project-urban-routes-es.git
     cd qa-project-urban-routes-es
     ```

3. **Casos de Prueba Automatizados:**
   - `test_set_route`: Configuración de la ruta desde un origen a un destino.
   - `test_open_taxi_modal_and_select_comfort`: Apertura del modal para solicitar un taxi y selección de la tarifa comfort.
   - `test_add_phone_number`: Adición del número de teléfono.
   - `test_add_phone_code`: Adición del código de confirmación del teléfono.
   - `test_add_credit_card`: Adición de una tarjeta de crédito.
   - `test_message_to_driver`: Envío de un mensaje al conductor.
   - `test_order_ice_creams`: Pedido de helados.
   - `test_blanket_and_tissues_switch`: Activación del interruptor para manta y pañuelos.
   - `test_request_taxi`: Solicitud de un taxi.

4. **Ejecución de las Pruebas:**
   - Ejecuta los casos de prueba utilizando pytest u otra herramienta de prueba compatible:
     ```bash
     pytest test_cases.py
     ```

5. **Interpretación de los Resultados:**
   - Observa la salida en la consola para verificar el éxito o fallo de cada prueba.

Este README proporciona una guía básica para entender el proyecto y ejecutar las pruebas de forma efectiva utilizando Selenium WebDriver y Python.


## Nota sobre las pruebas

En mi entorno, todas las pruebas son positivas. Sin embargo, he notado que al no utilizar `time.sleep`, las pruebas a menudo generan errores. Incluso durante los ejercicios de la lección, las soluciones que utilizan `WebDriverWait` generalmente producían errores a menos que se depuraran o se utilizara `time.sleep`. En mi proyecto ocurre lo mismo. Intenté usar esperas implícitas y explícitas, pero seguían generando errores o necesitaban adicionalmente un `time.sleep`.

Además, si cambio los localizadores por selectores más sencillos, no encuentran el elemento. 

Por esta razón, he mantenido el uso de `time.sleep` y localizadores específicos para asegurar que las pruebas se ejecuten correctamente en mi entorno.

## Resultados de las pruebas

A continuación, se presentan los resultados de la ejecución de las pruebas en mi entorno:

/Users/falom/PycharmProjects/my_first_python_project/pythonProject/venv/bin/python /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/falom/projects/qa-project-Urban-Routes-es/test_case.py
Testing started at 4:22 PM ...
Launching pytest with arguments /Users/falom/projects/qa-project-Urban-Routes-es/test_case.py --no-header --no-summary -q in /Users/falom/projects/qa-project-Urban-Routes-es

============================= test session starts ==============================
collecting ... collected 9 items

test_case.py::TestUrbanRoutes::test_set_route
test_case.py::TestUrbanRoutes::test_open_taxi_modal_and_select_comfort
test_case.py::TestUrbanRoutes::test_add_phone_number
test_case.py::TestUrbanRoutes::test_add_phone_code
test_case.py::TestUrbanRoutes::test_add_credit_card
test_case.py::TestUrbanRoutes::test_message_to_driver
test_case.py::TestUrbanRoutes::test_order_ice_creams
test_case.py::TestUrbanRoutes::test_blanket_and_tissues_switch
test_case.py::TestUrbanRoutes::test_request_taxi

=================== 9 passed, 1 warning in 78.74s (0:01:18) ====================
PASSED [ 11%]PASSED [ 22%]PASSED [ 33%]PASSED [ 44%]PASSED [ 55%]PASSED [ 66%]PASSED [ 77%]PASSED [ 88%]PASSED [100%]
Process finished with exit code 0

