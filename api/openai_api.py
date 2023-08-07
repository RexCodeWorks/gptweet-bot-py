import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")

def get_tweet(type):
    openai.organization = ORGANIZATION_ID
    openai.api_key = OPENAI_API_KEY

    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": get_prompt(type)}
    #     ]
    # )
    # print(completion.choices)
    # print(completion.choices[0].message)

    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=get_prompt(type),
        max_tokens=1000,
        temperature=0.6,
        presence_penalty =0.6
    )

    return completion.choices[0].text

def get_prompt(type):
    if type == "quote":
        return "Please provide a 'Motivational Quote' tweet for my weight loss and health Twitter account. The tweet must follow this format and the tweet must limited between 50 characters and 270 characters and must add linebreak between sections(title, quote, hashtags): \n 🌟 Motivational Quote 🌟 \n 💬 [Your motivational quote here] \n #[Hashtags related to motivation and inspiration]"
    else:
        return "Please provide a 'Daily Weight Loss Tip' tweet for my weight loss and health Twitter account. The tweet must follow this format and the tweet must limited between 100 characters and 280 characters and must add linebreak between sections(title, tip, why, act, hashtags): \n 🌟 Daily Weight Loss Tip 🌟 \n 💡 Tip: [Your weight loss tip here] \n ❓ Why: [Explain the benefits and reasons for the tip] \n ✅ Act: [Offer actionable advice or steps related to the tip] \n #[Hashtags related to the topic]"

