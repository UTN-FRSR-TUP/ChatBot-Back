# 🤖 Chatbot 
## Descripción
Chatbot realizado por integrantes del Equipo UTN MMXXIII. El programa utiliza una API que permite la comunicación entre los requerimientos del usuario (desde el FrontEnd) y las respuestas del motor de Inteligencia Artificial utilizado (en el Backend).
Asimismo, según el modelo de negocio planteado, la aplicación permite personalizar el nombre, icono y colores del chatbot y establecer información específica sobre la compañía como una temática específica (por ejemplo, seguros), o en el caso que se requiera horarios de atención, canales de comunicación, etc. Ésta información puede ser cargada mediante un documento PDF del negocio en el Backend y operar como contexto de trabajo de la IA. 

## Tecnologías
La aplicación web está desarrollada con React, Vite y React Bootstrap. El backend esta realizado en python, FastAPI y utiliza el motor IA Cohere.

## Características Principales
- Personalización del nombre, icono y colores del chatbot.
- Interfaz de usuario amigable construida con React y React Bootstrap.
- Comunicación mediada por una IA para responder a los mensajes del usuario.
- Funcionalidad de chat con integración de PDF, para introducir información personalizada.

## Requisitos del Sistema
- Node.js (versión 14 o superior)
- npm (versión 6 o superior)
- Python 3.x
- Pip
- FastAPI
- Cohere
- PyPDF2

## Instrucciones de Instalación
Para probar la aplicación localmente, sigue estos pasos:

### [Frontend](https://github.com/UTN-FRSR-TUP/ChatBot-Front.git)

- Clona el repositorio de Git del Frontend: git clone https://github.com/UTN-FRSR-TUP/ChatBot-Front.git

- Navega al directorio del proyecto: cd ChatBot-Front

- Instala las dependencias necesarias: npm install

- Ejecuta la aplicación en modo de desarrollo: npm run dev

### [Backend](https://github.com/UTN-FRSR-TUP/ChatBot-Back.git)
- Clona el repositorio de Git del Backend: https://github.com/UTN-FRSR-TUP/ChatBot-Back.git
- Navega al directorio del proyecto: cd ChatBot-Back
- Instala las dependencias utilizando pip: pip install -r requirements.txt
- Variables de entorno: Crea tu apiKey de Cohere y guardala en un archivo .env

## Uso Básico del backend
- Ejecuta el servidor FastAPI: uvicorn main:app --reload
El servidor se iniciará en http://localhost:8000. Puedes interactuar con el chatbot enviando solicitudes POST a http://localhost:8000/chat/.

- Ejemplo de solicitud. Puedes interactuar con el chatbot utilizando cualquier cliente HTTP. Aquí hay un ejemplo usando cURL:

bash
curl -X 'POST' \
  'http://localhost:8000/chat/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hola, ¿cómo estás?"
}'

- Recuerda que al ser licencias de pruebas puede existir demora en la respuesta de la IA.


## Uso enviando peticiones desde el FrontEnd
- Para probar la aplicación con el backend en local, es necesario modificar la URL del fetch en el código fuente para que apunte al backend local [http://localhost:8000/chat/](http://localhost:8000/chat/). Luego, inicia la aplicación siguiendo las instrucciones de instalación e interactúa con el Chatbot.

- Recuerda que al ser licencias de pruebas puede existir demora en la respuesta de la IA.

## Version online
También puedes probar nuestro chatbot ingresando al siguiente enlace: [https://utn-frsr-tup.github.io/ChatBot-Front/](https://utn-frsr-tup.github.io/ChatBot-Front/)

- Recuerda que al ser licencias de pruebas puede existir demora en la respuesta de la IA. Esta version tiene cargado un PDF sobre educación en programación y la creciente demanda de desarrolladores de software. Por lo que sólo responderá preguntas al respecto. 

## Contribución
Este proyecto ha sido desarrollado por el grupo UTN MMXXIII de la Tecnicatura en Programación de la UTN. Las contribuciones estaran permitidas luego de aprobado el trabajo.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Autor(es)
Grupo UTN MMXXIII de la Tecnicatura en Programación de la UTN:
- [Ponce Maria Elena](https://github.com/hechizera10)
- [Martinez Gonzalo Exequiel](https://github.com/Scravt)
- [Fiuri Franco](https://github.com/FrancoFiuri)
- [Piris Matias](https://github.com/MatiasNPiris)

