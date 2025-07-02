from agent import Agent
from google.genai import types

class AgentBuilder:
    def __init__(self):
        self.model_name = ''
        self.system_prompt = ''
        self.tools = []
        self.response_schema = None

    def use_model(self, name: str):
        self.model_name = name
        return self

    def use_system_prompt(self, system_prompt: str):
        self.system_prompt = system_prompt
        return self

    def add_tool(self, tool):
        self.tools.append(tool)
        return self

    def add_tools(self, tools):
        for tool in tools:
            self.add_tool(tool)

        return self

    def use_response_schema(self, response_schema):
        self.response_schema = response_schema
        return self

    def build(self):
        config = {
            'tools': self.tools
        }

        if self.system_prompt:
            config['system_instruction'] = self.system_prompt

        return Agent(self.model_name, self.response_schema, types.GenerateContentConfig(**config))