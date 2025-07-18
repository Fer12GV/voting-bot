# 🗳️ LSV-TECH Voting Bot

Este es un bot automatizado de votación desarrollado por **LSV-TECH** utilizando **Python 
---

## 🚀 Características

- ✅ Interfaz web sencilla para ingresar el número de votos.
- 🧠 Automatización completa usando `Playwright` en modo headless.
- 🧪 Muestra de logs de estado de cada intento en pantalla.
- 📦 Contenedorizado con Docker para fácil despliegue.
- 🌐 Responsive y fácil de usar desde navegador.

---

---

## 🚀 Estructura del proyecto

```
voting-bot/
├── backend/
│ ├── app.py # Servidor Flask
│ ├── constants.py # Constantes de scraping
│ ├── scraper.py # Script principal de scraping con Playwright
│ ├── Dockerfile # Imagen Docker para el backend
│ └── requirements.txt # Dependencias Python
├── frontend/
│ ├── static/
│ │ ├── app.js # Lógica JS cliente
│ │ ├── styles.css # Estilos CSS
│ │ └── airplane.gif # GIF de carga
│ └── templates/
│ └── index.html # Página HTML principal
├── docker-compose.yml # Orquestación Docker
└── .gitignore # Archivos ignorados por Git
```

---


---

## ⚙️ Instalación y Uso

### ✅ Requisitos

- Docker y Docker Compose instalados en tu máquina.
- Acceso a internet para descargar imágenes y dependencias.

---

### 🔧 Variables clave configuradas
- Estas constantes están definidas en backend/constants.py:
```bash
VOTE_ATTEMPTS = 1
URL_INICIAL = "https://empresas.eluniversal.com.co/premios-al-reconocimiento/votacion"
TEXTO_BTN_VOTAR = "Votar"
TEXTO_CATEGORIA = "EMPRESAS TECNOLÓGICAS"
TEXTO_EMPRESA = "LSV-TECH"
```

### 🖥️ Funcionalidad técnica
- Cuando el usuario indica un número de votos, se envía una petición POST al endpoint /votar.
- El servidor Flask ejecuta scraper.py usando asyncio y Playwright para abrir un navegador invisible, navegar por 
el sitio web de votación, y realizar el voto por la empresa deseada.
- El proceso se repite según el número de intentos indicados.
- El frontend muestra mensajes de progreso y resultados del votado.
- Ingreso del número de votos.
- Comunicación en tiempo real vía **WebSocket** con mensajes del estado del bot.
- GIF animado mientras el scraper trabaja.
- Actualización automática del estado al finalizar la votación.

---

## ⚙️ Instalación y ejecución

1. Clona el repositorio y entra al directorio:

```bash
git clone https://github.com/Fer12GV/voting-bot.git
cd voting-bot
```

2. 🐳 Ejecutar con Docker:
- Opción 1
```bash
sudo docker-compose build
sudo docker-compsoe up -d
```

- Opción 2
```bash
docker-compose up --build
```

3. Luego abre tu navegador y ve a: 
- http://localhost:8000


## 🧼 Notas

- El GIF de carga (airplane.gif) se muestra mientras se ejecuta el proceso.
- El archivo .gitignore incluye exclusiones para Python, Flask, Linux, Ubuntu, Windows etc.
- La aplicación corre por defecto en el puerto 8000 gracias al docker-compose.yml.

---

## 🧠 Lógica del Bot

- En el backend (`app.py`), se recibe la cantidad de votos.
- Se ejecuta la lógica de scraping (automatización).

---

## 🖼️ Interfaz

- `index.html`: Formulario + visualización del estado.
- `app.js`: Controla el formulario, activa el GIF, etc.
- `airplane.gif`: Se muestra durante la ejecución del bot.

---

## 🤖 Tecnología usada

- Flask
- Docker
- HTML + CSS + JavaScript

---

## 📬 Contacto
Desarrollado por Ing. Fernando Garrido · ✨ Especialistas en automatización inteligente.

---

## 📃 Licencia

MIT License