# Proyecto de Scraping de Datos Financieros de Yahoo Finance

## Descripción
Este proyecto realiza un scraping de datos financieros desde Yahoo Finance y otras fuentes usando Selenium y Python. El objetivo es obtener información financiera relevante y almacenarla en una base de datos PostgreSQL para su posterior análisis. Además, se realiza una auditoría de los datos extraídos para validar la integridad de la información.

## Arquitectura del Proyecto
El proyecto sigue una estructura de paquetes orientada a las buenas prácticas de producción, con los siguientes módulos y paquetes:

```
proyecto_scraping/
│
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── ejecucion/
│   │   ├── __init__.py
│   │   └── ejecutar.py
│   ├── scrapper/
│   │   ├── __init__.py
│   │   └── scrapper_yahoo.py
│   ├── modelo/
│   │   ├── __init__.py
│   │   └── modelo.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_scrapper.py
│   ├── test_modelo.py
│   └── test_ejecucion.py
└── logs/
    └── .gitkeep
```

### Descripción de Paquetes

1. **src/scrapper**: Contiene el módulo encargado de extraer la información financiera de Yahoo Finance. Este módulo incluye funciones para:
   - Cargar la URL de Yahoo Finance.
   - Obtener tablas HTML mediante XPath.
   - Transformar los datos para agregar columnas adicionales, como variaciones de precios y porcentajes de subida.
   - Capturar imágenes de las tablas como respaldo.

2. **src/modelo**: Contiene el módulo para la conexión y manejo de la base de datos PostgreSQL. Sus funciones principales incluyen:
   - Crear esquemas y tablas en la base de datos.
   - Insertar los datos extraídos en la base de datos.
   - Realizar auditorías de las tablas para garantizar la calidad de los datos, generando informes con estadísticas descriptivas y valores nulos.

3. **src/ejecucion**: Contiene el módulo encargado de centralizar la ejecución del proceso de scraping y almacenamiento. Importa tanto el scraper como el modelo y realiza las siguientes tareas:
   - Configura las rutas y los parámetros de conexión a la base de datos.
   - Ejecuta el scraper para obtener los datos desde Yahoo Finance.
   - Almacena los datos extraídos en las tablas correspondientes.
   - Realiza la auditoría para validar los datos.

4. **src/utils**: Incluye funciones auxiliares y reutilizables que permiten reducir la redundancia y mejorar la modularidad del proyecto. Por ejemplo, aquí podrían ubicarse funciones para manejar excepciones, formatear datos, etc.

5. **src/config**: Contiene los archivos de configuración del proyecto. El archivo `settings.py` permite centralizar todos los parámetros configurables, como las credenciales de la base de datos, la URL del scraper, etc.

6. **tests**: Contiene las pruebas unitarias para todos los módulos del proyecto. Se utiliza `unittest` o `pytest` para asegurar que cada parte del código funcione correctamente y evitar errores en producción.

7. **logs**: Directorio destinado a almacenar los archivos de registro generados durante la ejecución del proyecto. Esto es útil para el monitoreo y la depuración.

## Tecnologías Utilizadas
- **Python 3.8+**: Lenguaje de programación principal.
- **Selenium**: Para la automatización del navegador y el scraping de datos.
- **Pandas**: Para la manipulación y transformación de los datos extraídos.
- **SQLAlchemy**: Para la conexión y manejo de la base de datos PostgreSQL.
- **PostgreSQL**: Base de datos para almacenar los datos financieros extraídos.
- **pytest**: Para la realización de pruebas unitarias.

## Instalación y Configuración
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura la conexión a la base de datos PostgreSQL en el archivo `src/config/settings.py`:
   - Actualiza las variables `host`, `port`, `nombredb`, `user` y `password` con la información correspondiente.
4. Asegúrate de tener el driver de Chrome instalado y especifica su ruta en la variable `driver_ruta` dentro de `settings.py`.

## Uso
Para ejecutar el proyecto, simplemente ejecuta el script `ejecucion/ejecutar.py`:
```bash
python src/ejecucion/ejecutar.py
```
Este script automatizará todo el proceso de scraping, transformación, almacenamiento y auditoría de los datos.

## Auditoría de Datos
El módulo `modelo` realiza una auditoría de los datos almacenados en la base de datos. Los informes de auditoría incluyen:
- Estadísticas descriptivas de los datos.
- Número de valores nulos por columna.
- Dimensiones del DataFrame.

Estos informes se guardan en archivos `.txt` dentro de la carpeta `auditoria/logs/`.

## Consideraciones Adicionales
- **Headless Browser**: Se puede configurar el scraper para que funcione en modo headless (sin interfaz gráfica) descomentando la línea correspondiente en `scrapper_yahoo.py`.
- **Tiempo de Espera**: Para evitar bloqueos, se recomienda ajustar los tiempos de espera (`time.sleep()`) entre acciones del navegador.
- **Buenas Prácticas**: Se ha estructurado el proyecto siguiendo buenas prácticas como la separación de responsabilidades, modularidad del código, y el uso de un archivo de configuración centralizado.

## Licencia
Este proyecto está licenciado bajo la MIT License. Consulta el archivo `LICENSE` para más detalles.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un _issue_ o envía un _pull request_.

