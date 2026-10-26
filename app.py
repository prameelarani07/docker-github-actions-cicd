
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps CI/CD Dashboard</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(
                135deg,
                #fff1e6,
                #ffd6ba,
                #f8b89a,
                #f6a57a
            );
            color: #493126;
            min-height: 100vh;
            padding: 35px 20px;
        }

        .container {
            max-width: 1050px;
            margin: auto;
        }

        header {
            text-align: center;
            padding: 35px 15px;
        }

        .badge {
            display: inline-block;
            background: #ffedd5;
            color: #9a3412;
            border: 1px solid #fdba74;
            padding: 8px 15px;
            border-radius: 25px;
            margin-bottom: 20px;
            font-size: 13px;
            font-weight: bold;
        }

        h1 {
            font-size: clamp(34px, 6vw, 60px);
            margin-bottom: 15px;
            line-height: 1.15;
        }

        h1 span {
            background: linear-gradient(
                90deg,
                #c2410c,
                #e11d48,
                #ea580c
            );
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .intro {
            max-width: 650px;
            margin: auto;
            line-height: 1.8;
            color: #795548;
            font-size: 16px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(
                auto-fit,
                minmax(220px, 1fr)
            );
            gap: 20px;
            margin: 25px 0 35px;
        }

        .card {
            background: rgba(255, 255, 255, 0.8);
            border: 1px solid #f5c7a9;
            border-radius: 18px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(120, 53, 15, 0.08);
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card .emoji {
            font-size: 30px;
            margin-bottom: 15px;
        }

        .card h2 {
            font-size: 20px;
            margin-bottom: 10px;
        }

        .card p {
            color: #795548;
            line-height: 1.7;
            font-size: 14px;
        }

        .pipeline {
            background: rgba(255, 250, 245, 0.85);
            border: 1px solid #f5c7a9;
            border-radius: 18px;
            padding: 30px;
            text-align: center;
        }

        .pipeline h2 {
            margin-bottom: 25px;
        }

        .steps {
            display: grid;
            grid-template-columns: repeat(
                auto-fit,
                minmax(130px, 1fr)
            );
            gap: 15px;
        }

        .step {
            background: #fff1e6;
            border: 1px solid #f5c7a9;
            border-radius: 12px;
            padding: 18px 10px;
            font-weight: bold;
            font-size: 14px;
        }

        .step span {
            display: block;
            font-size: 25px;
            margin-bottom: 10px;
        }

        .status {
            display: inline-block;
            margin-top: 25px;
            padding: 10px 18px;
            border-radius: 25px;
            background: #dcfce7;
            color: #166534;
            font-weight: bold;
            font-size: 14px;
        }

        footer {
            text-align: center;
            margin-top: 30px;
            color: #795548;
            font-size: 13px;
            line-height: 1.8;
        }
    </style>
</head>

<body>
    <main class="container">
        <header>
            <div class="badge">⚙️ DEVOPS PROJECT</div>

            <h1>
                Build. Deploy.<br>
                <span>Automate Everything.</span>
            </h1>

            <p class="intro">
                Welcome to my CI/CD dashboard! This project uses
                Docker and GitHub Actions to automate application
                testing, image building, and publishing.
            </p>
        </header>

        <section class="cards">
            <article class="card">
                <div class="emoji">🐳</div>
                <h2>Docker</h2>
                <p>
                    Packages the application and its dependencies
                    into a portable container.
                </p>
            </article>

            <article class="card">
                <div class="emoji">🔄</div>
                <h2>GitHub Actions</h2>
                <p>
                    Automates testing and Docker image publishing
                    whenever code is pushed.
                </p>
            </article>

            <article class="card">
                <div class="emoji">🧪</div>
                <h2>Automated Tests</h2>
                <p>
                    Uses pytest to verify the application's home
                    page and health endpoint.
                </p>
            </article>
        </section>

        <section class="pipeline">
            <h2>🚀 My CI/CD Pipeline</h2>

            <div class="steps">
                <div class="step">
                    <span>📤</span>
                    1. Push Code
                </div>

                <div class="step">
                    <span>🧪</span>
                    2. Run Tests
                </div>

                <div class="step">
                    <span>🐳</span>
                    3. Build Image
                </div>

                <div class="step">
                    <span>📦</span>
                    4. Push Image
                </div>
            </div>

            <div class="status">
                ● Application is running
            </div>
        </section>

        <footer>
            <p>Built with Flask, Docker, pytest and GitHub Actions.</p>
            <p>DevOps CI/CD Internship Project</p>
        </footer>
    </main>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevOps CI/CD Dashboard"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
