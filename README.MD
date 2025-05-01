📬 API para Envío de Correos – con estilo y sin dramas

¡Ey! Después de horas de pelearme con errores, rutas 404, codificaciones locas y validaciones rebeldes…
¡Aquí está mi API funcional para enviar correos!

Sí, funciona. Y sí, está bonita. Te cuento más 👇

🚀 ¿Qué hace esta app?
Una API sencilla (pero poderosa) construida con Python y Flask que te permite:

✅ Enviar correos de forma segura
✅ Validar que el email sea real (nada de correos inventados tipo pepe@noexiste.com)
✅ Usar Mailtrap para hacer pruebas sin quemar tus credenciales reales
✅ Recibir respuestas claras si algo falla

⚙️ Tecnologías y librerías usadas
🐍 Python 3

🌶️ Flask

✉️ smtplib, MIMEText y Header (para enviar correos y controlar acentos como dios manda)

🔒 Mailtrap (para evitar dramas con Gmail)

🧪 Postman para testear la API como se debe

📩 Cómo probarla

1. Clona el repositorio:


git clone https://github.com/tuusuario/nombre-repo.git
cd nombre-repo


2. Instala los requirements:

pip install -r requirements.txt

3. Configura tus credenciales de Mailtrap directamente en el script 

(MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD)

4. Lanza el servidor:

python app.py
Prueba el endpoint con Postman o curl:

5. Prueba el endpoint con Postman

🔥 Bonus track

Si te salta un error... respira, no es el fin. Esta app te devuelve mensajes claritos para que sepas qué está pasando.

💡 Spoiler: el error más loco que me salió fue por una ñ escondida en un .env... 😅

💬 ¿Feedback, ideas, bugs?

¡Bienvenidos! Puedes abrir issues, forkar, clonar, copiar o simplemente curiosear.
Estoy aprendiendo, creciendo y compartiendo el proceso, sin filtros.

🧙‍♂️ Que el código te acompañe

