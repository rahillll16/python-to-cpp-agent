from core.prompts import planner_prompt
from core.models import CLIENTS

def plan(model: str, python_code: str, language: str) -> str:
    client = CLIENTS[model]
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": planner_prompt(python_code, language)}]
    )
    return response.choices[0].message.content
