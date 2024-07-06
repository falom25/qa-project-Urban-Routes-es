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


## Video de las pruebas 

https://drive.google.com/file/d/1GLWljlb8xchlMo3qqaagd1Cuulq2XNMN/view?usp=sharing

## Resultados de las pruebas

A continuación, se presentan los resultados de la ejecución de las pruebas en mi entorno:

/Users/falom/PycharmProjects/my_first_python_project/pythonProject/venv/bin/python /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/falom/projects/qa-project-Urban-Routes-es/main.py 
Testing started at 8:41 PM ...
Launching pytest with arguments /Users/falom/projects/qa-project-Urban-Routes-es/main.py --no-header --no-summary -q in /Users/falom/projects/qa-project-Urban-Routes-es

============================= test session starts ==============================
collecting ... collected 9 items

main.py::TestUrbanRoutes::test_set_route 
main.py::TestUrbanRoutes::test_open_taxi_modal_and_select_comfort 
main.py::TestUrbanRoutes::test_add_phone_number 
main.py::TestUrbanRoutes::test_add_phone_code 
main.py::TestUrbanRoutes::test_add_credit_card 
main.py::TestUrbanRoutes::test_message_to_driver 
main.py::TestUrbanRoutes::test_order_ice_creams 
main.py::TestUrbanRoutes::test_blanket_and_tissues_switch 
main.py::TestUrbanRoutes::test_request_taxi 

=================== 9 passed, 1 warning in 66.06s (0:01:06) ====================
PASSED                          [ 11%]PASSED [ 22%]PASSED                   [ 33%]PASSED                     [ 44%]PASSED                    [ 55%]PASSED                  [ 66%]PASSED                   [ 77%]PASSED         [ 88%]PASSED                       [100%]
Process finished with exit code 0