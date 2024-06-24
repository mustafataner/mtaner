# Python resmi imajını kullanarak başlıyoruz
FROM python:3.12-slim

# Gerekli bağımlılıkları yükleyelim
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome'u yükleyelim
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

# ChromeDriver'ı yükleyelim
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Python bağımlılıklarını yükleyelim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalayalım
COPY . /app
WORKDIR /app

# Uygulamayı çalıştıralım
CMD ["python", "app.py"]
