from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_work(
    grade,
    subject,
    task,
    topic
):

    prompt = f"""
Make a {task}

Class: {grade}
Subject: {subject}
Topic: {topic}

Use simple language suitable for students.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
