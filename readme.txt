Chatbot con FastAPI y Cohere
Este proyecto consiste en un chatbot implementado en Python utilizando FastAPI como framework web y 
Cohere para el procesamiento del lenguaje natural. El chatbot responde a consultas de los usuarios 
siguiendo ciertas reglas predefinidas y puede interactuar con documentos PDF para proporcionar respuestas contextualizadas.

Requisitos previos
Asegúrate de tener instaladas las siguientes herramientas y bibliotecas:

Python 3.x
Pip
FastAPI
Cohere
PyPDF2

(se sugiere creacion de entorno virtual)

Instalación
Clona este repositorio en tu máquina local:

bash
git clone https://github.com/tu_usuario/tu_proyecto.git
Accede al directorio del proyecto:

bash
cd tu_proyecto

Instala las dependencias utilizando pip:
pip install -r requirements.txt

Variables de entorno 
Crea tu apiKey de Cohere y guardala en un archivo .env



Uso
Ejecuta el servidor FastAPI:

uvicorn main:app --reload
El servidor se iniciará en http://localhost:8000. Puedes interactuar con el chatbot enviando solicitudes POST a http://localhost:8000/chat/.

Ejemplo de solicitud
Puedes interactuar con el chatbot utilizando cualquier cliente HTTP. Aquí hay un ejemplo usando cURL:

bash
curl -X 'POST' \
  'http://localhost:8000/chat/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hola, ¿cómo estás?"
}'


Contribución
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu nueva funcionalidad (git checkout -b feature/nueva-funcionalidad).
Haz tus cambios y realiza commits describiendo tus modificaciones (git commit -am 'Agrega nueva funcionalidad').
Haz push de tus cambios a tu repositorio (git push origin feature/nueva-funcionalidad).
Abre un pull request en el repositorio original.


Licencia
Este proyecto está bajo la licencia MIT.