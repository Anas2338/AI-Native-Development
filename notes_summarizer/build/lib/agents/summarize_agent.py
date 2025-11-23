from typing import List
from model import model
from all_agents import OpenAIChatCompletionsModel, SystemMessage, UserMessage

class SummarizeAgent:
    """
    Agent responsible for summarizing text using the Gemini model.
    """

    def __init__(self, model_client: OpenAIChatCompletionsModel = model):
        """
        Initializes the SummarizeAgent with a model client.
        Args:
            model_client: The OpenAI Chat Completions model to use for summarization.
        """
        self.model_client = model_client

    async def summarize(self, text: str, summary_style: str = "Bullet Notes") -> str:
        """
        Generates a summary of the given text based on the specified style.

        Args:
            text: The input text to summarize.
            summary_style: The desired style for the summary (e.g., "Bullet Notes", "Blocks", "Flashcards").

        Returns:
            The generated summary.
        """
        system_prompt = f"""You are a helpful assistant specialized in generating study notes.
        Your task is to summarize the provided text into a '{summary_style}' format.
        Ensure the summary is accurate, concise, and faithful to the original text.
        Avoid hallucinations and only use information present in the input text.
        """

        user_prompt = f"Please summarize the following text in '{summary_style}' format:\n\n{text}"

        messages: List[SystemMessage | UserMessage] = [
            SystemMessage(content=system_prompt),
            UserMessage(content=user_prompt)
        ]

        response = await self.model_client.create(messages=messages)
        assert isinstance(response.content, str)
        return response.content

