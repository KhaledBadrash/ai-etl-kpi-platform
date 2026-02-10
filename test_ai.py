import ollama

print("⏳ Sende Anfrage an Llama 3.1...")
response = ollama.chat(model='llama3.1', messages=[
  {'role': 'user', 'content': 'Erkläre einem Laien, was ETL bedeutet.'},
])
print("\n🤖 Antwort:")
print(response['message']['content'])