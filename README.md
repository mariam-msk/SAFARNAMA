# safarnama
This is a simple AI chatbot web application built using Flask and Google Gemini (Generative AI). Users can interact with the Gemini LLM through a web interface styled with HTML and JavaScript.
1. Clone the Repository

git clone https://github.com/your-username/safarnama.git
cd safarnama

2. Create and Activate a Virtual Environment

python -m venv .venv
# On Windows:
.venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the root folder and add your Google Gemini API key, also add your geoapify key, set your secret key too:

GOOGLE_API_KEY=your_google_api_key_here

5. Run the Application

python main.py


You should see output like:

 * Running on http://127.0.0.1:5000/ 
