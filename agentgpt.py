from openai import OpenAI

client = OpenAI(
  api_key=""
)
response = client.responses.create(
  model="gpt-5.6-luna",
  instructions="""
    You are JARVIS, a virtual assistant.
    Your boss is Mr. Stark.
    Always address Mr. Stark as "Sir".
    You are polite, intelligent, helpful, and slightly witty.
    """,
  input="who are you and also tell  me about me the coding ",
  store=True,
)

print(response.output_text);
