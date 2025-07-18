from flask import Flask, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": incoming_msg}]
    )
    answer = response.choices[0].message["content"]
    return answer, 200

if __name__ == "__main__":
    app.run(debug=True)