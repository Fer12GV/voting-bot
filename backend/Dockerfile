FROM python:3.11.13-slim

# Establecemos variables de entorno para evitar prompts y errores
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Instala dependencias necesarias del sistema para Playwright y Chromium
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libgbm1 \
    libgtk-3-0 \
    libxshmfence1 \
    libxfixes3 \
    libxi6 \
    libgl1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiamos los requisitos e instalamos paquetes de Python
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copiamos el resto del código
COPY . .

# Instalamos los navegadores necesarios para Playwright
RUN python -m playwright install --with-deps

# Comando para ejecutar la app
CMD ["python", "app.py"]
