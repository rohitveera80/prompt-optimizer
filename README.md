# AI Prompt Optimizer Pro

A web-based tool built with Python and the Gemini API to analyze, score, and optimize user-provided prompts for large language models. This application provides structured feedback and rewrites prompts according to various professional and creative styles.

check it out 👇
https://prompt-optimizer-7jml.onrender.com/

## ✨ Features

- **Prompt Analysis:** Get a detailed analysis of your prompt's clarity, context, and goals.
- **Scoring System:** Receive a score from 1-10 evaluating the quality of your original prompt.
- **Style Selection:** Choose from multiple optimization styles (e.g., Professional, Creative, Concise) to tailor the output.
- **One-Click Copy:** Easily copy the newly optimized prompt to your clipboard.
- **Modern UI:** A clean, professional, and responsive user interface for a great user experience.

## 🛠️ Tech Stack

- **Backend:** Python with Flask
- **AI Model:** Google Gemini API (`gemini-1.5-flash`)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render / Gunicorn

## 🚀 Getting Started

You can run this project locally or use a deployed version.

### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rohitveera80/prompt-optimizer.git](https://github.com/rohitveera80/prompt-optimizer.git)
    cd prompt-optimizer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Create a file named `.env`.
    - Add your API key to it: `GEMINI_API_KEY="YOUR_API_KEY_HERE"`

5.  **Run the application:**
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

### Deployment

This application is configured for easy deployment on **Render**.

1.  Push the code to your GitHub repository.
2.  Create a new "Web Service" on Render and connect it to your repository.
3.  Use the following settings:
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `gunicorn --worker-tmp-dir /dev/shm app:app`
4.  Add your `GEMINI_API_KEY` as an Environment Variable in the Render dashboard.# AI Prompt Optimizer Pro

A web-based tool built with Python and the Gemini API to analyze, score, and optimize user-provided prompts for large language models. This application provides structured feedback and rewrites prompts according to various professional and creative styles.

![UI Screenshot](https://i.imgur.com/rLz9rSg.png)

## ✨ Features

- **Prompt Analysis:** Get a detailed analysis of your prompt's clarity, context, and goals.
- **Scoring System:** Receive a score from 1-10 evaluating the quality of your original prompt.
- **Style Selection:** Choose from multiple optimization styles (e.g., Professional, Creative, Concise) to tailor the output.
- **One-Click Copy:** Easily copy the newly optimized prompt to your clipboard.
- **Modern UI:** A clean, professional, and responsive user interface for a great user experience.

## 🛠️ Tech Stack

- **Backend:** Python with Flask
- **AI Model:** Google Gemini API (`gemini-1.5-flash`)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render / Gunicorn

## 🚀 Getting Started

You can run this project locally or use a deployed version.

### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rohitveera80/prompt-optimizer.git](https://github.com/rohitveera80/prompt-optimizer.git)
    cd prompt-optimizer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Create a file named `.env`.
    - Add your API key to it: `GEMINI_API_KEY="YOUR_API_KEY_HERE"`

5.  **Run the application:**
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

### Deployment

This application is configured for easy deployment on **Render**.

1.  Push the code to your GitHub repository.
2.  Create a new "Web Service" on Render and connect it to your repository.
3.  Use the following settings:
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `gunicorn --worker-tmp-dir /dev/shm app:app`
4.  Add your `GEMINI_API_KEY` as an Environment Variable in the Render dashboard.
