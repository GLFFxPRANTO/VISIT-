from flask import Flask, request
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/visit/<uid>/<sl>', methods=['GET'])
def get_visit_data(uid, sl):
    url = f"https://freefire-virusteam.vercel.app/visit?key=7day@apivirusteam&uid={uid}&sl={sl}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "message" in data and all(key in data["message"] for key in ["Name", "UID", "Successful", "Failed", "Time", "Speed"]):
            return f"""NAME : {data["message"]["Name"]}
UID : {data["message"]["UID"]}
SUCCESSFUL : {data["message"]["Successful"]}
FAILED : {data["message"]["Failed"]}
TIME : {data["message"]["Time"]}
SPEED : {data["message"]["Speed"]}""", 200, {'Content-Type': 'text/plain; charset=utf-8'}
        
        else:
            return "Error: Required data not found!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("Visit API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment
