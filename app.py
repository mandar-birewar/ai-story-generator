from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Generate AI text
def generate_story(prompt):

    result = generator(
        prompt,
        max_length=150,
        num_return_sequences=1,
        temperature=0.9
    )

    return result[0]["generated_text"]

@app.route("/", methods=["GET", "POST"])
def home():

    output = ""

    if request.method == "POST":

        prompt = request.form["prompt"]

        output = generate_story(prompt)

    return render_template(
        "index.html",
        output=output
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )