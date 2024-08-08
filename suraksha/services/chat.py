from openai import OpenAI
from suraksha.config import config
from suraksha.services.firebase import db
import datetime
import time

openai = OpenAI(
    api_key=config.KRUTRIM_SECRET_KEY,
    base_url="https://cloud.olakrutrim.com/v1",
)

def get_firebase_data(user_id, query_time=None):
    if query_time is None:
        query_time = datetime.datetime.now()
    
    query_time_millis = int(time.mktime(query_time.timetuple()) * 1000)
    
    analytics_data = db.child("analytics").child(user_id).order_by_key().end_at(str(query_time_millis)).limit_to_last(1).get().val()
    
    if analytics_data:
        return list(analytics_data.values())[0]
    return None

def format_analytics_data(data):
    if not data:
        return "No data available for the specified time."
    
    formatted_data = "Data recorded:\n"
    for obj, details in data.items():
        formatted_data += f"- {obj.capitalize()}: detected {details['freq']} times, "
        formatted_data += f"max confidence: {details['maxConfidence']:.2f}, "
        formatted_data += f"min confidence: {details['minConfidence']:.2f}, "
        formatted_data += f"at {details['time']}\n"
    
    return formatted_data

def get_chat_response(text, conversation_history, user_id):
    query_time = None
    if "at" in text.lower():
        try:
            time_str = text.split("at")[-1].strip()
            query_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass
    
    firebase_data = get_firebase_data(user_id, query_time)
    formatted_data = format_analytics_data(firebase_data)
    
    system_message = """
    You are an AI assistant for a security system called SuRक्षा AI. Your primary function is to help users 
    understand and interpret security data captured by cameras and sensors. You have access to analytics 
    data that includes information about detected objects, their frequency, and confidence levels.
    
    When answering questions:
    1. Always prioritize user safety and privacy.
    2. If asked about specific times, refer to the provided analytics data.
    3. If no specific time is mentioned, use the most recent data available.
    4. Be concise but informative in your responses.
    5. If you're unsure about something, say so rather than making assumptions.
    6. Recommend contacting human security personnel for any serious concerns.
    """
    
    conversation_history.append({"role": "user", "content": text})
    conversation_history.append({"role": "system", "content": f"Recent analytics data: {formatted_data}"})
    
    messages = [{"role": "system", "content": system_message}] + conversation_history
    
    chat_completion = openai.chat.completions.create(
        model="Krutrim-spectre-v2",
        messages=messages,
        frequency_penalty=0,
        logit_bias={2435: -100, 640: -100},
        logprobs=True,
        top_logprobs=2,
        max_tokens=256,
        n=1,
        presence_penalty=0,
        response_format={"type": "text"},
        stop=None,
        stream=False,
        temperature=0,
        top_p=1
    )
    
    assistant_response = chat_completion.choices[0].message.content
    
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
    if len(conversation_history) > 10:
        conversation_history = conversation_history[-10:]
    
    return assistant_response, conversation_history