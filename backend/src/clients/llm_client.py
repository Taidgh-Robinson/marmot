from litellm import acompletion
from src.config.llm_config import LLMConfig


class LLMClient():
    def __init__(self):
        self.config: LLMConfig = LLMConfig() 

    async def query_llm(self, query: str):
        if self.config.local_base:
            response = await acompletion(
                model=self.config.model,
                messages=[{"role": "user", "content": query}],
                api_base=self.config.local_base
            )
        else: 
            response = await acompletion(
                model=self.config.model,
                messages=[{"role": "user", "content": query}],
            )

        return response

         

