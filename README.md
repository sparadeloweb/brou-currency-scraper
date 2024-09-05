# 🏦 Currency Scraper API

Sorpresivamente, no existe una API para obtener la cotización Dólar -> Peso Uruguayo. Así que si por alguna razón lo necesitas, probá este script hecho en `Flask` y `Selenium`.

## 🚀 Instalación

### 1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/currency-scraper-api.git
cd currency-scraper-api
```

### 2. Configurá el entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usá `venv\Scripts\activate`
```

### 3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

### 4. Asegurate de tener `geckodriver` instalado y accesible en tu `PATH`.

Podés descargar `geckodriver` desde [la página oficial](https://github.com/mozilla/geckodriver/releases).

## 🛠 Uso

Para iniciar la API localmente, ejecutá:

```bash
python server.py
```

La API va a estar disponible en `http://127.0.0.1:5000`.

### Endpoint disponible

- `GET /currencies`: Devuelve un JSON con las cotizaciones de las monedas.

## 🐋 Despliegue en Fly.io

Fly.io es una plataforma que te permite desplegar aplicaciones de manera sencilla. Seguí estos pasos para desplegar tu API de scraping de monedas en Fly.io:

1. **Instalá el CLI de Fly.io:**

   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Iniciá sesión y creá tu aplicación en Fly.io:**

   Primero, iniciá sesión en tu cuenta de Fly.io. Si no tenés una cuenta, el CLI te va a guiar para crear una.

   ```bash
   flyctl auth login
   ```

   Luego, iniciá el proceso de creación de la aplicación en tu directorio de proyecto:

   ```bash
   flyctl launch
   ```

   Durante este proceso, se te va a pedir que nombres tu aplicación y elijas una región. Podés aceptar las opciones por defecto.

3. **Configurá el archivo `fly.toml`:**

   Asegurate de que tu archivo `fly.toml` (generado por `flyctl launch`) esté configurado correctamente. Por ejemplo:

   ```toml
   app = "nombre-de-tu-app"
   kill_signal = "SIGINT"
   kill_timeout = 5
   processes = []

   [build]
     image = "python:3.9-slim"

   [env]
     PORT = "5000"

   [[services]]
     internal_port = 5000
     protocol = "tcp"

     [[services.ports]]
       handlers = ["http"]
       port = 80

     [[services.ports]]
       handlers = ["tls", "http"]
       port = 443
   ```

4. **Aumentá los recursos de la máquina:**

   Si te encontrás con errores de memoria (como "Out of Memory"), considerá aumentar la memoria asignada a tu aplicación en Fly.io:

   ```bash
   flyctl scale memory 512
   ```

5. **Desplegá tu aplicación:**

   Desplegá tu aplicación en Fly.io utilizando el siguiente comando:

   ```bash
   flyctl deploy
   ```

   Esto va a construir tu aplicación y la va a desplegar en la nube de Fly.io.

6. **Verificá el estado de la aplicación:**

   Revisá los logs de tu aplicación para asegurarte de que todo esté funcionando correctamente:

   ```bash
   flyctl logs
   ```

   También podés verificar el estado de la aplicación con:

   ```bash
   flyctl status
   ```

## 🐞 Solución de Problemas

- **Error `Out of Memory` en Fly.io**: Aumentá la memoria de tu instancia usando `flyctl scale memory <cantidad>`.
- **Error de `WebDriverException` o problemas con Selenium**: Asegurate de que todos los binarios (como `geckodriver`) estén correctamente incluidos y configurados en el entorno de Fly.io.

