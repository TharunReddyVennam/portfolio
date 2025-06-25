from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def profile_page():
    html_code = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Profile Page</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f0f8ff;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #004080;
                color: white;
                text-align: center;
                padding: 20px;
            }
            main {
                padding: 20px;
                max-width: 800px;
                margin: auto;
            }
            .profile-photo {
                width: 150px;
                border-radius: 50%;
                border: 2px solid #004080;
                margin-bottom: 10px;
            }
            .contact {
                background: #ffffff;
                padding: 15px;
                border-radius: 8px;
                margin-top: 20px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            input, textarea, button {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                background-color: #004080;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #0059b3;
            }
        </style>
        <script>
            function showMessageAlert(event) {
                event.preventDefault();
                var message = document.getElementById("contact-message").value;
                if (message.trim() === "") {
                    alert("Please enter a message.");
                } else {
                    alert("Message Submitted:\\n" + message);
		    event.target.reset();
                }
            }
        </script>
    </head>
    <body>
        <header>
            <h1>Welcome to My Profile Page</h1>
        </header>
        <main>
            <section>
                <img src="/static/passportsize.jpg" alt="Profile Photo" class="profile-photo">
                <p>Hello! I’m <strong>Tharun Reddy Vennam</strong>, a student passionate about technology and development.</p>
            </section>

            <section class="contact">
                <h2>Contact Me</h2>
                <form onsubmit="showMessageAlert(event)">
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Your Email" required>
                    <textarea id="contact-message" placeholder="Your Message" required></textarea>
                    <button type="submit">Submit</button>
                </form>
            </section>
        </main>
    </body>
    </html>
    '''
    return render_template_string(html_code)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=5007)
