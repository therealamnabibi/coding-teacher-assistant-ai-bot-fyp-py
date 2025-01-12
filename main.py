import os
from flask import Flask, request, render_template
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI API key a
openai.api_key = os.getenv("OPENAI_API_KEY")
print("Loaded API Key:", openai.api_key)

# Initialize Flask app
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# Route for introduction page
@app.route("/index")
def intro():
    return render_template("index.html")

# Route for chatbot page
@app.route("/")
def home():
    return render_template("chatbot.html", response=None)

# Route for video page
@app.route("/vedio")
def vedio():
    return render_template("vedio.html")

@app.route("/notes")
def notes():
    return render_template("Course/notes.html")

@app.route("/notes/csharp")
def csharp_notes():
    return render_template("Course/csharp.html")
@app.route("/notes/Cpp")
def Cpp_notes():
    return render_template("Course/Cpp.html")

@app.route("/notes/html")
def html_notes():
    return render_template("Course/html.html")

@app.route("/notes/css")
def css_notes():
    return render_template("Course/css.html")
@app.route("/notes/python")
def python_notes():
    return render_template("Course/python.html")

@app.route("/notes/javaScript")
def javaScript_notes():
    return render_template("Course/javaScript.html")
@app.route("/notes/sql")
def sql_notes():
    return render_template("Course/sql.html")
@app.route("/notes/php")
def php_notes():
    return render_template("Course/php.html")

# Chatbot endpoint
@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    print("Received question:", question)

    if not question:
        return render_template("chatbot.html", response="Please enter a question.")

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
        return render_template("chatbot.html", response=answer)



    except Exception as e:
        print(f"Error occurred: {e}")
        return render_template("chatbot.html", response=f"Error occurred: {e}")

if __name__ == "__main__":
    app.run(debug=True)
