from all_agents.model import model
from agents import OpenAIChatCompletionsModel
from agents.model_settings import ModelSettings
from agents.models.interface import ModelTracing
from agents.items import ItemHelpers # Import ItemHelpers

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

        response = await self.model_client.get_response(
            system_instructions=system_prompt,
            input=user_prompt, # Pass user_prompt as input
            model_settings=ModelSettings(), # Default ModelSettings
            tools=[], # Empty list for tools
            output_schema=None, # No specific output schema for summarization
            handoffs=[], # Empty list for handoffs
            tracing=ModelTracing.DISABLED, # Tracing disabled by default
            previous_response_id=None, # No previous response
        )
        
        full_response_content = ""
        for item in response.output:
            text_content = ItemHelpers.extract_last_text(item)
            if text_content:
                full_response_content += text_content
        
        return full_response_content


