from google import genai

client = genai.Client(api_key="AIzaSyCPBYCXqAsEjEeqrE1-PHhG8YQPYyGyU9M")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Write a short story about a dragon"
)

print(response.text)