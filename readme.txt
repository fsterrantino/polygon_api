Instrucciones:

- Clonar el repo.

- Crear la tabla en Redshift (Puede utilizarse el código create_table presente en la carpeta /Redshift/Creación tabla)

- Modificar el config.ini
	. api_parameters: Se pueden incorporar tickers de acciones a consultar.
	. database_connection: Modificar por los propios datos de conexión.

- Crear el .env en la carpeta raíz con las siguientes variables: 
	. API_KEY: Se obtiene una personal desde la web de Polygon API.
	. DATABASE_PASSWORD: Colocar la clave personal 

	Ej:
	API_KEY = Lw_kCasdwcsd_42esec_5kWHZp_zXQ6
	DATABASE_PASSWORD = estaEsmiPassword156

- Correr docker + airflow:
	- docker-compose build
	- docker-compose up -d

- Configurar la conexión a la DB desde la UI de Airflow: admin -> connections -> +
	- connection_id: Identificador único
	- connection_tyoe: Postgres
	- host: url del host de Redshift
	- Schema: Base de datos de Redshift
	- Login: Redshift user
	- Password: Redshift password
	- Port: Redshift port