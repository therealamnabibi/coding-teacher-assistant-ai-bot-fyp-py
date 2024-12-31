import os
from flask import Flask, request, render_template
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
print("Loaded API Key:", openai.api_key)

# Initialize Flask app
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
@app.route("/intro")
def intro():
    return render_template("intro.html")
@app.route("/")
def home():
    return render_template("index.html", response=None)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    print("Received question:", question)

    if not question:
        return render_template("index.html", response="Please enter a question.")

    try:
        print("Sending request to OpenAI API...")
        # Correct OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=50,
            temperature=0.7
        )
        # Extract the correct response
        answer = response['choices'][0]['message']['content'].strip()
        print("OpenAI API response:", answer)
        return render_template("index.html", response=answer)

    except openai.error.AuthenticationError:
        print("Invalid API Key. Please check your key.")
        return render_template("index.html", response="Invalid API Key. Please check your setup.")

    except Exception as e:
        print(f"Error occurred: {e}")
        return render_template("index.html", response=f"Error occurred: {e}")


if __name__ == "__main__":
    app.run(debug=True)

