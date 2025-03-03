# Proyecto Instagram

Proyecto creado con Django para hacer una aplicación con funcionalidades parecidas a Instagram

## Advertencias

> **Advertencia:** Este proyecto es solo para fines educativos. No se recomienda su uso en producción.

## Instalación

Para instalar el proyecto, sigue estos pasos:
1. Clona el repositorio:
    
    ```bash
    git clone https://github.com/ThePowerty/libreria.git
    ```

2. Creamos el entorno virtual:
    
    ```bash
    python3 -m venv env
    ```

3. Activamos el entorno virtual:
    
    ```bash
    source env/bin/activate
    ```

4. Instalamos las dependencias
    
    ```bash
    pip3 install -r requirements.txt
    ```
---

# Requisitos

Antes de ejecutar el proyecto, asegúrate de tener un archivo `.env` configurado. Este archivo contiene variables de entorno necesarias para el funcionamiento del apartado de *contacto*.

## Configuración del archivo .env

1. Copia el archivo de ejemplo:
   
   ```bash
   cp .env.example .env
   ```

2. Editar y añadir tus credenciales a las variables de entorno

> **Advertencia:** Para el uso del apartado de *contacto* con Gmail es necesario tener una clave aplicación para añadirla a las variables de entorno.

> Para usar el apartado de *contacto* a traves de una configuración de un servidor smtp propio es necesario editar el apartado de `Configuración de correo` del archivo *settings*.