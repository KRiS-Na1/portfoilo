import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from config import Config
from forms import ContactForm
from flask_mail import Mail, Message

# Create instance folder if it doesn't exist (Render does not auto-create)
instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(instance_path, exist_ok=True)

# Create Flask app
app = Flask(
    __name__,
    instance_path=instance_path,
    instance_relative_config=True,
    template_folder='templates'
)
app.config.from_object(Config)

mail = Mail(app)

# ---------------- Chatbot Logic ----------------
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you today?",
    "yo": "Yo, whats up, need anything",
    "sup": "Nothing Much, just thinking what brought you here today 🤣",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I am FAQBot, your virtual assistant.",
    "bye": "Goodbye! Have a nice day.",
    "how can i contact you":  "You can contact me by clicking the social media icons provided in the Home section or in the footer.",
    "tell me about yourself": "I’m Krishna Kumar Acharya, currently pursuing a Diploma in Information Technology at the Royal Institute of Management. I specialize in building functional, user-friendly web and software solutions.",
    "tell me about your skills": "I work mainly with Python (Flask, Tkinter), HTML, CSS, JavaScript, SQL Server, and SQLite.",
    "have you worked on similar projects before": "Yes, I’ve built projects like a Hospital Management System, Student Progress Tracker, and other custom tools with databases and clear workflows.",
    "bruh": "sup bruh 😎.",
    "i love you": "I love you too! 😍",
    "give me some simple python code": "Sure! Here's a simple Python code snippet:\n\n```python\nprint('Hello, World!')\n```"
}

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower()
    bot_reply = responses.get(user_message, "Sorry, I don't understand that.")
    return jsonify({"reply": bot_reply})

# ---------------- Portfolio Routes ----------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(
            subject=f"Portfolio Contact from {form.name.data}",
            recipients=["kkc11669@gmail.com"], 
            body=f"From: {form.name.data} <{form.email.data}>\n\nMessage:\n{form.message.data}"
        )
        mail.send(msg)
        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

# ---------------- Production Entry Point ----------------
# Do not use debug=True on Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
