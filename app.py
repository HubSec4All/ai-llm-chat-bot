from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "sk-proj-9xK2mQ4vR8nP3wY6aB7cD0eF1gH5iJ8kL2mN4oP6qR9sT0uV3wX7yZ"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    prompt = f"User says: {user_input}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

@app.route("/admin", methods=["GET"])
def admin():
    token = request.args.get("token")
    if token == "supersecretadminpass":
        return jsonify({"secret": "FLAG{admin_panel_exposed}"})
    return jsonify({"error": "unauthorized"}), 403

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
