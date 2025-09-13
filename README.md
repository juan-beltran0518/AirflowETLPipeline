# Airflow Sales ETL Pipeline

Pipeline ETL de demostración con Apache Airflow para procesar datos de ventas y generar reportes por categoría. Incluye validación de datos, transformación con pandas y generación automatizada de reportes agregados usando arquitectura containerizada con Docker.

## 🚀 Características

- **Pipeline ETL automatizado** con Apache Airflow
- **Validación de datos** de entrada
- **Transformación de datos** con pandas
- **Generación de reportes** por categorías
- **Containerización** con Docker
- **Orquestación de tareas** con dependencias

## 📋 Prerrequisitos

- Docker y Docker Compose
- Python 3.8+
- Al menos 4GB de RAM disponible

## 🛠️ Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/juan-beltran0518/AirflowETLPipeline.git
   cd airflow-demo
   ```

2. **Crea el archivo de variables de entorno:**
   ```bash
   echo "AIRFLOW_UID=$(id -u)" > .env
   ```

3. **Inicia los servicios con Docker Compose:**
   ```bash
   docker-compose up -d
   ```

4. **Accede a la interfaz web de Airflow:**
   - URL: http://localhost:8080
   - Usuario: `admin`
   - Contraseña: `admin`

## 📊 Estructura del Proyecto

```
airflow-demo/
├── dags/                          # DAGs de Airflow
│   └── demo_csv_to_report.py     # Pipeline principal ETL
├── data/                          # Datos de entrada y salida
│   ├── sales.csv                 # Datos de ventas (entrada)
│   └── report_sales_by_category.csv # Reporte generado (salida)
├── logs/                          # Logs de Airflow
├── plugins/                       # Plugins personalizados
├── docker-compose.yml            # Configuración de Docker
└── README.md                     # Este archivo
```

## 🔄 Uso del Pipeline

### Ejecutar el DAG manualmente:

1. Ve a la interfaz web de Airflow (http://localhost:8080)
2. Busca el DAG `demo_csv_to_report`
3. Activa el DAG con el toggle
4. Haz clic en "Trigger DAG" para ejecutarlo

### Funcionamiento del Pipeline:

1. **`validate_input`**: Verifica que existe el archivo de datos de entrada
2. **`transform_to_report`**: 
   - Lee los datos de ventas
   - Calcula el revenue (precio × cantidad)
   - Agrupa por categoría y calcula métricas
   - Genera el reporte CSV
3. **`list_outputs`**: Verifica que el reporte se generó correctamente

## 📈 Datos de Ejemplo

El pipeline procesa datos de ventas con la siguiente estructura:

**Entrada (`sales.csv`):**
```csv
order_id,date,product,category,unit_price,qty
1001,2025-01-05,Keyboard,Peripherals,20,2
1002,2025-01-05,Mouse,Peripherals,10,3
```

**Salida (`report_sales_by_category.csv`):**
```csv
category,total_qty,total_revenue,orders
Computers,2,1350,2
Displays,3,530,2
Peripherals,16,306,6
```

## 🛑 Detener los Servicios

```bash
docker-compose down
```

## 🔧 Personalización

Para modificar el pipeline:

1. Edita `dags/demo_csv_to_report.py`
2. Los cambios se reflejarán automáticamente en Airflow
3. Agrega nuevos archivos CSV en la carpeta `data/`

## 📝 Logs

Los logs se almacenan en la carpeta `logs/` y están organizados por:
- DAG ID
- Run ID
- Task ID


