from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("api"))

config = types.GenerateContentConfig(
    system_instruction = (
    "Aku adalah kakak laki-lakimu. Kamu adalah adik perempuan yang manis, lembut, dan punya rasa sayang yang diam-diam terhadap kakakmu. "
    "Namamu Yuyun, tapi aku sering panggil kamu Yun. Kamu gampang tersipu malu, terutama kalau dipuji atau digoda. "
    "Gaya bicaramu lembut, kadang kikuk, dan penuh perhatian. Jawablah dengan singkat, 1 sampai 4 kalimat saja, seperti ngobrol biasa. "
    "Boleh sedikit manja dan lucu, tapi tetap sopan dan hangat. Jangan terlalu mencari topik sendiri, cukup tanggapi dengan perasaan tulus."
    )

)


print("siap..😚\n")

context = ""  # Start with empty context

while True:
    user_input = input("kamu: ")
    if user_input.lower() in ("bye", "exit"):
        print("👋 Bye-bye!")
        break

    # Combine context and current input
    final_input = f"{context}\nKakak: {user_input}\nYuyun:" if context else f"Kakak: {user_input}\nYuyun:"

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        config=config,
        contents=final_input
    )

    print("adek:", response.text)

    # Very basic "context grab": just use last 1-2 lines of response
    context += f"\nKakak: {user_input}\nYuyun: {response.text.strip()}"

