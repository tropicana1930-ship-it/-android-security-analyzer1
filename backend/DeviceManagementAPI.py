# Esqueleto de la API de gestión de dispositivos (Flask)
from flask import Flask, jsonify, request
from azure.identity import DefaultAzureCredential

app = Flask(__name__)

# Ruta de ejemplo para obtener la lista de dispositivos monitoreados
@app.route('/devices', methods=['GET'])
def get_devices():
    # Aquí se integraría la autenticación con Azure y la conexión a una base de datos.
    print("Intentando autenticación con Azure...")
    try:
        # La credencial por defecto intentará usar las credenciales de la entidad de servicio (si se ejecuta en Azure)
        credential = DefaultAzureCredential()
        # credential.get_token("https://management.azure.com//.default") 
        auth_status = "Autenticación de Azure exitosa (simulada)."
    except Exception as e:
        auth_status = f"Fallo en la autenticación de Azure: {e}"

    return jsonify({
        "status": "success",
        "auth_status": auth_status,
        "devices": [
            {"id": "Device-001", "model": "Pixel 6", "last_scan": "2025-10-01"}, 
            {"id": "Device-002", "model": "Galaxy S21", "last_scan": "2025-10-01"}
        ]
    })

if __name__ == '__main__':
    # Solo para desarrollo local; no se usa en GitHub Actions
    app.run(debug=True)
