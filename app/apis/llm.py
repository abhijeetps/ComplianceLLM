import os
from openai import OpenAI
from app.consts import SYSTEM_MESSAGE
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def generate_prompt(compliance_policy, to_test_content):
    prompt = f"""
    Here's the complicance policy within three asterisk:
    ***
    #{compliance_policy}`
    ***

    Here's the website content within three backticks:
    ```
    #{to_test_content}
    ```

    Generate a report with the following headings:
    ---
    Compliance Conclusion:
    Scope of Compliance Report:
    Review of Compliance Process:
    Summary of Outcomes:
    ---
    """
    return prompt

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system","content": SYSTEM_MESSAGE},
        {"role": "system","content": prompt},
    ]
    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model,
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error occured while communicating with LLM: ")

def use_llm(compliance_policy, to_test_content):
    prompt = generate_prompt(compliance_policy, to_test_content)
    compliance_report = get_completion(prompt)
    return compliance_report
