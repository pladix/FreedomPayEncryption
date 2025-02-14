from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64

app = Flask(__name__)

modulus_b64 = "ALLOloIfHQHp1hNA8qFca+emB2P4fMTGHwTDeQUxq54wzt1C3H6ZjhdnE6PWlMoymafT9QrV4ZS6MbGKo+dc6krKg9EdxbpNA+T8BAKnb/rXu/uVURI29qQWvmKZfB0RHiiBMlgG4g2b+kOTmVCNI7qyWP50Bk/PlvBs6CUiAdAqvZKSjB3fH99BTvQouTYg+YCwLnmXavTw3THId1t6jCKjpStW9v7i7FtE5C9+ZJu40pTflY1MXfznTQzij4mDHlRdiQPST2iGZEovwX/Ysk0m9bLfW8SO/+S1ijPWfPBwsRtpCoXZOgHP6GIvB5d0X+54S5MRFnf5Ltzx7IBIW48="
exponent = 65537

modulus_int = int.from_bytes(base64.b64decode(modulus_b64), "big")

public_key = rsa.RSAPublicNumbers(exponent, modulus_int).public_key()


@app.route("/encrypt", methods=["GET"])
def encrypt_card():
    
    card_number = request.args.get("card")
    expiration_date = request.args.get("expirationDate")
    security_code = request.args.get("securityCode")
    postal_code = request.args.get("postalCode")

    if not card_number or not expiration_date or not security_code:
        return jsonify({"error": "Parâmetros 'card', 'expirationDate' e 'securityCode' são obrigatórios"}), 400

    card_data_string = f"M{card_number}={expiration_date}:{security_code}:{postal_code or ''}"

    try:
        encrypted_data = public_key.encrypt(
            card_data_string.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        encrypted_b64 = base64.b64encode(encrypted_data).decode()

        return jsonify({"cardData": encrypted_b64})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
