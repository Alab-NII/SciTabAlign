# openai_model.py
from openai import OpenAI
from models.base_model import BaseModel

class OpenAIModel(BaseModel):
    def __init__(self, model_name="gpt-4o"):
        super().__init__(model_name)
        self.model = OpenAI()

    def call(self, prompt, **kwargs):
        response = self.model.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=kwargs.get("temperature", 0),
            max_tokens=kwargs.get("max_tokens", 1024),
        )
        return prompt, response.choices[0].message.content
