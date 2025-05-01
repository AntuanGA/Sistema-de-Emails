from flask import request, jsonify
from flask_mail import Message
from app import app, mail  # Importamos la app y mail desde app.py

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()

    to_email = data.get("to_email")
    subject = data.get("subject")
    message = data.get("message")

    if not to_email or not subject or not message:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        msg = Message(subject, sender=app.config["MAIL_USERNAME"], recipients=[to_email])
        msg.body = message
        mail.send(msg)
        return jsonify({"message": "Correo enviado con éxito ✅"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    