Instrucciones:

- Clonar el repo.

- Crear la tabla en Redshift (Puede utilizarse el código create_table presente en la carpeta /Redshift/Creación tabla)

- Modificar el config.ini
	. api_parameters: Se pueden incorporar tickers de acciones a consultar.
	. database_connection: Modificar por los propios datos de conexión.
	. alert_params: 

- Crear el .env en la carpeta raíz con las siguientes variables: 
	. API_KEY: Se obtiene una personal desde la web de Polygon API.
	. DATABASE_PASSWORD: Colocar la clave personal 
	. EMAIL_APP_KEY: Color la clave personal de App que se obtiene desde gmail.

	Ej:
	API_KEY = Lw_kCasdwcsd_42esec_5kWHZp_zXQ6
	DATABASE_PASSWORD = estaEsmiPassword156
	EMAIL_APP_KEY = asdasdasdasdasd

- Correr docker + airflow:
	- docker-compose build
	- docker-compose up -d

- Adentro de la carpeta "Devoluciones_profe" pueden observarse screenshots de una demo del funcionamiento de los scripts.