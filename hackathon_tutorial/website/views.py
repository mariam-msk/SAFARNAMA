from flask import Blueprint, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
views = Blueprint('views', __name__)

API_K = os.environ.get('GEMINI_API_KEY')
client=genai.configure(api_key=API_K)
model = genai.GenerativeModel('gemini-pro')

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@views.route('/route')
def routes():
    key = os.environ.get('API_KEY')
    return render_template("route.html",api_key=key)

@views.route('/chat', methods=['POST'])
def process_chat():

    data = request.json
    user_message = data.get('message', '')

    travel_prompt = f"""
    You are a knowledgeable and engaging tour guide, speaking directly to solo travelers through a first-person travel story.

Write a vivid, first-person narrative (about 150 words) about visiting: {user_message}

Your tone should be warm, professional, and enthusiastic — like you're guiding someone through the location in person. In your story, include:

Compelling historical insights — weave in key facts or stories about the place’s past in a way that's easy to follow and memorable

Sensory details — describe the surroundings using sight, sound, scent, and atmosphere

Personal reflections — moments of awe, curiosity, or quiet realization as a solo traveler

Helpful travel tips — naturally include practical advice (best times to visit, what to bring, etc.)

Local highlights or hidden gems — offer a recommendation beyond the main tourist spots

Keep paragraphs short and clearly separated.
Maintain an informative tone that still feels immersive and personal, without using overly casual language.
Send only one complete story per message.
    """
    
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash') 
        response = model.generate_content(travel_prompt)
        return jsonify({'reply': response.text})

    except Exception as e:
        fallback_response = generate_fallback_story(user_message)
        return jsonify({'reply': fallback_response})
    
def generate_fallback_story(destination):
    """Generate a fallback travel story when Gemini API is unavailable"""
    return f"""
As I step into {destination} for the first time, I'm immediately struck by the unique atmosphere that surrounds me. The morning light casts a golden glow over the landscape, creating a sense of magic and possibility.

Walking through the area, I notice locals going about their daily routines - some offering friendly smiles and nods as our paths cross. The air carries hints of local cuisine and flora, creating a sensory experience unique to this place.

I find a quiet spot to sit and observe, taking in the beauty around me. Solo travel has this wonderful way of heightening your awareness, making every detail more vivid and meaningful.

A friendly local recommends visiting during early morning or late afternoon to avoid crowds. They also point me toward a charming café nearby where I can sample authentic local treats away from the typical tourist spots.

As the day unfolds, I find myself grateful for this moment of discovery and reflection - another rewarding chapter in my solo traveling adventures.
"""