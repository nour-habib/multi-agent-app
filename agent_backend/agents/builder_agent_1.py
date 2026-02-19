from openai import OpenAI


class BuilderAgent1:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.name = "BuilderAgent1"
