import re
import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure the Flask app
app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# This is the heart of your tool!
# It's the instruction you send to the AI to get it to analyze the user's prompt.
def create_optimizer_prompt(user_prompt, style):
    # This new meta-prompt asks for a score and incorporates the selected style.
    return f"""
    You are a professional AI Prompt Engineering consultant. Your task is to provide a clear, professional, and actionable analysis of a user's prompt. Your analysis must be professional, direct, and helpful.

    **Objective:** Rewrite the user's prompt to be significantly more effective for a large language model. The rewritten prompt must adhere to the user's selected style.

    **User's Prompt to Analyze:**
    ---
    {user_prompt}
    ---
    
    **User's Desired Style for Rewritten Prompt:** {style}

    **Required Output Format (Strict JSON):**
    You must return a single, valid JSON object with THREE keys: "score", "analysis", and "optimized_prompt".

    1.  **score**: An integer between 1 and 10, representing the quality of the *original* user's prompt (1=very poor, 10=excellent).
    2.  **analysis**: A string containing a structured markdown analysis. Start with a one-sentence summary, then a bulleted list evaluating the prompt on Clarity, Context, and Goal.
    3.  **optimized_prompt**: A string containing the rewritten, professional-grade prompt, tailored to the user's desired style.
    """

# Define the API endpoint
@app.route('/optimize', methods=['POST'])
def optimize_prompt():
    user_prompt = request.json.get('prompt')
    # Get the new 'style' value from the request, defaulting to 'professional'
    selected_style = request.json.get('style', 'professional') 
    
    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Pass the selected style to the prompt creation function
        optimizer_prompt = create_optimizer_prompt(user_prompt, selected_style)
        ai_response = model.generate_content(optimizer_prompt)

        json_match = re.search(r'\{.*\}', ai_response.text, re.DOTALL)
        
        if json_match:
            clean_json_string = json_match.group(0)
            return clean_json_string, 200, {'ContentType':'application/json'}
        else:
            print(f"AI response did not contain valid JSON: {ai_response.text}")
            return jsonify({"error": "Failed to parse AI response."}), 500

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500
    
# Add this new route to serve the main page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)