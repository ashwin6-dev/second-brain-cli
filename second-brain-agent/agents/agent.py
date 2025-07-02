from google import genai

class Agent:
    def __init__(
            self,
            model,
            final_response_schema=None,
            config=None,
    ):
        self.model = model
        self.final_response_schema = final_response_schema
        self.config = config
        self.client = genai.Client()

    def invoke(self, query: str):
        chat = self.client.chats.create(model=self.model, config=self.config)

        response = chat.send_message(query)

        return response