# Código original que funciona
# from flask import Flask, request, jsonify
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Cargar variables desde .env

# app = Flask(__name__)

# MAIL_SERVER = os.getenv("MAIL_SERVER")
# MAIL_PORT = int(os.getenv("MAIL_PORT"))
# MAIL_USERNAME = os.getenv("MAIL_USERNAME")
# MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

# @app.route("/enviar-email", methods=["POST"])
# def enviar_email():
#     data = request.get_json()
#     to_email = data.get("to_email")
#     subject = data.get("subject")
#     message = data.get("message")

#     if not to_email or not subject or not message:
#         return jsonify({"error": "Faltan campos en el cuerpo del mensaje"}), 400

#     try:
#         msg = MIMEText(message, "plain", "utf-8")
#         msg["Subject"] = Header(subject, "utf-8")
#         msg["From"] = MAIL_USERNAME
#         msg["To"] = to_email

#         with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
#             server.starttls()
#             server.login(MAIL_USERNAME, MAIL_PASSWORD)
#             server.send_message(msg)

#         return jsonify({"mensaje": "Correo enviado con éxito (Mailtrap)"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)


# código con mejoras
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import re
import logging

from dotenv import load_dotenv
load_dotenv()  # Carga el archivo .env automáticamente

app = Flask(__name__)

# Configuración de logs
logging.basicConfig(level=logging.INFO)

# Cargar configuraciones de variables de entorno
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

@app.route("/enviar-email", methods=["POST"])
def enviar_email():
    data = request.get_json()
    to_email = data.get("to_email")
    subject = data.get("subject")
    message = data.get("message")

    # Validación de campos
    if not to_email or not subject or not message:
        return jsonify({"error": "Faltan campos en el cuerpo del mensaje"}), 400
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", to_email):
        return jsonify({"error": "Correo electrónico no válido"}), 400

    try:
        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        msg["From"] = MAIL_USERNAME
        msg["To"] = to_email

        with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
            server.starttls()
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            server.send_message(msg)

        logging.info(f"Correo enviado con éxito a {to_email}")
        return jsonify({"mensaje": "Correo enviado con éxito"}), 200

    except smtplib.SMTPAuthenticationError:
        logging.error("Fallo de autenticación SMTP")
        return jsonify({"error": "Fallo de autenticación SMTP"}), 401

    except smtplib.SMTPConnectError:
        logging.error("Error de conexión con el servidor SMTP")
        return jsonify({"error": "Error de conexión con el servidor SMTP"}), 500

    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)















# from flask import Flask, request, jsonify
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header  # Importamos Header para UTF-8 en el asunto
# import os

# app = Flask(__name__)

# # Cargar configuraciones de la variable de entorno
# MAIL_SERVER = os.getenv("MAIL_SERVER")
# MAIL_PORT = os.getenv("MAIL_PORT")
# MAIL_USERNAME = os.getenv("MAIL_USERNAME")
# MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

# @app.route("/enviar-email", methods=["POST"])
# def enviar_email():
#     # Obtener los datos del cuerpo de la solicitud
#     data = request.get_json()
#     to_email = data.get("to_email")
#     subject = data.get("subject")
#     message = data.get("message")
    
#     # Verificar si faltan campos
#     if not to_email or not subject or not message:
#         return jsonify({"error": "Faltan campos en el cuerpo del mensaje"}), 400

#     try:
#         # Crear el mensaje con codificación utf-8
#         msg = MIMEText(message, "plain", "utf-8")
        
#         # Asunto con codificación UTF-8
#         msg["Subject"] = Header(subject, "utf-8")  # Usamos Header para asegurar UTF-8 en el asunto
#         msg["From"] = MAIL_USERNAME
#         msg["To"] = to_email

#         # Enviar el correo
#         with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
#             server.starttls()
#             server.login(MAIL_USERNAME, MAIL_PASSWORD)
#             server.send_message(msg)

#         return jsonify({"mensaje": "Correo enviado"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500



# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

# Prueba 2o mil 

# from flask import Flask, request, jsonify
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import formataddr
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# # Carga las variables de entorno y forza strings
# MAIL_SERVER   = str(os.getenv("MAIL_SERVER", "smtp.gmail.com"))
# MAIL_PORT     = int(os.getenv("MAIL_PORT", 587))
# MAIL_USERNAME = str(os.getenv("MAIL_USERNAME", ""))  # Asegúrate de que no esté vacío
# MAIL_PASSWORD = str(os.getenv("MAIL_PASSWORD", ""))


# @app.route("/enviar-email", methods=["POST"])
# def enviar_email():
#     data = request.get_json()
#     to_email = data.get("to_email")
#     subject  = data.get("subject")
#     message  = data.get("message")
    
#     if not all([to_email, subject, message]):
#         return jsonify({"error": "Faltan campos en el cuerpo del mensaje"}), 400

#     try:
#         # Crea el cuerpo en UTF-8
#         msg = MIMEText(message, "plain", "utf-8")
        
#         # Codifica todos los encabezados en UTF-8
#         msg["Subject"] = Header(subject, "utf-8")
#         msg["From"]    = formataddr((str(Header("Remitente App", "utf-8")), MAIL_USERNAME))
#         msg["To"]      = formataddr((str(Header("Destinatario", "utf-8")), to_email))

#         # Enviar el correo
#         with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
#             server.starttls()
#             server.login(MAIL_USERNAME, MAIL_PASSWORD)
#             server.send_message(msg)

#         return jsonify({"mensaje": "Correo enviado con éxito"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

# prueba 21 millll 
# from flask import Flask, request, jsonify
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import formataddr
# import os
# import quopri
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# # Cargar configuraciones de las variables de entorno
# MAIL_SERVER = str(os.getenv("MAIL_SERVER", "smtp.gmail.com"))
# MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
# MAIL_USERNAME = str(os.getenv("MAIL_USERNAME", ""))
# MAIL_PASSWORD = str(os.getenv("MAIL_PASSWORD", ""))

# @app.route("/enviar-email", methods=["POST"])
# def enviar_email():
#     # Obtener los datos del cuerpo de la solicitud
#     data = request.get_json()
#     to_email = data.get("to_email")
#     subject = data.get("subject")
#     message = data.get("message")
#     print(f"MAIL_USERNAME: {MAIL_USERNAME}, MAIL_PASSWORD: {MAIL_PASSWORD}")
#     # Verificar si faltan campos
#     if not all([to_email, subject, message]):
#         return jsonify({"error": "Faltan campos en el cuerpo del mensaje"}), 400

#     try:
#         # Codificar el mensaje y asunto en UTF-8 para garantizar que todo se transmita correctamente
#         message = quopri.encodestring(message.encode("utf-8")).decode("utf-8")
        
#         # Crear el mensaje con codificación utf-8
#         msg = MIMEText(message, "plain", "utf-8")
        
#         # Asunto con codificación UTF-8
#         msg["Subject"] = Header(subject, "utf-8")
        
#         # Formatear el remitente y destinatario usando codificación UTF-8
#         msg["From"] = formataddr((str(Header("Remitente App", "utf-8")), MAIL_USERNAME))
#         msg["To"] = formataddr((str(Header("Destinatario", "utf-8")), to_email))

#         # Enviar el correo
#         with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
#             server.starttls()
#             server.login(MAIL_USERNAME, MAIL_PASSWORD)
#             server.send_message(msg)

#         return jsonify({"mensaje": "Correo enviado con éxito"}), 200

#     except Exception as e:
#         # Si ocurre un error, retornar el mensaje de error
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

# Prueba 22 millll

# from flask import Flask, request, jsonify
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# import os
# import quopri
# from email.utils import formataddr

# app = Flask(__name__)

# # Cargar configuraciones de la variable de entorno
# MAIL_SERVER = os.getenv("MAIL_SERVER")
# MAIL_PORT = os.getenv("MAIL_PORT")
# MAIL_USERNAME = os.getenv("MAIL_USERNAME")
# MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

# @app.route("/enviar-email", methods=["POST"])
# def enviar_email():
#     # Obtener los datos del cuerpo de la solicitud
#     data = request.get_json()

#     # Depuración para ver lo que recibimos
#     print(f"Datos recibidos: {data}")  # Esto ayudará a ver si todo está correcto

#     to_email = data.get("to_email")
#     subject = data.get("subject")
#     message = data.get("message")
    
#     # Verificar si faltan campos
#     if not all([to_email, subject, message]):
#         return jsonify({"error": "Faltan campos en el cuerpo del mensaje"}), 400

#     try:
#         # Codificar el mensaje en utf-8 y asegurarnos de que es compatible
#         message = quopri.encodestring(message.encode("utf-8")).decode("utf-8")

#         # Crear el mensaje con codificación utf-8
#         msg = MIMEText(message, "plain", "utf-8")

#         # Asunto con codificación UTF-8
#         msg["Subject"] = Header(subject, "utf-8")

#         # Formatear el remitente y destinatario usando codificación UTF-8
#         msg["From"] = formataddr((str(Header("Remitente App", "utf-8")), MAIL_USERNAME))
#         msg["To"] = formataddr((str(Header("Destinatario", "utf-8")), to_email))

#         # Enviar el correo
#         with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
#             server.starttls()
#             server.login(MAIL_USERNAME, MAIL_PASSWORD)
#             server.send_message(msg)

#         return jsonify({"mensaje": "Correo enviado con éxito"}), 200

#     except Exception as e:
#         # Si ocurre un error, retornar el mensaje de error
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)







    

