from all_agents.summarize_agent import SummarizeAgent
from all_agents import OpenAIChatCompletionsModel # Assuming this type hint is needed

async def process_summarization(text: str, summary_style: str, model_client: OpenAIChatCompletionsModel) -> str:
    """
    Orchestrates the summarization process using the SummarizeAgent.

    Args:
        text: The input text to summarize.
        summary_style: The desired style for the summary.
        model_client: The model client to be used by the SummarizeAgent.

    Returns:
        The generated summary.
    """
    summarize_agent = SummarizeAgent(model_client=model_client)
    summary = await summarize_agent.summarize(text=text, summary_style=summary_style)
    return summary