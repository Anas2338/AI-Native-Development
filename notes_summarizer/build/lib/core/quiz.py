from all_agents.quiz_agent import QuizAgent
from all_agents import OpenAIChatCompletionsModel # Assuming this type hint is needed

async def process_quiz_generation(text: str, model_client: OpenAIChatCompletionsModel) -> str:
    """
    Orchestrates the quiz generation process using the QuizAgent.

    Args:
        text: The input text to generate quiz questions from.
        model_client: The model client to be used by the QuizAgent.

    Returns:
        A JSON string representing the generated quiz.
    """
    quiz_agent = QuizAgent(model_client=model_client)
    quiz_json_string = await quiz_agent.generate_quiz(text=text)
    return quiz_json_string
