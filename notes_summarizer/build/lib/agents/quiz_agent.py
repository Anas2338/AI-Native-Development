from typing import List
from model import model
from all_agents import OpenAIChatCompletionsModel, SystemMessage, UserMessage
import json

class QuizAgent:
    """
    Agent responsible for generating quiz questions from text using the Gemini model.
    """

    def __init__(self, model_client: OpenAIChatCompletionsModel = model):
        """
        Initializes the QuizAgent with a model client.
        Args:
            model_client: The OpenAI Chat Completions model to use for quiz generation.
        """
        self.model_client = model_client

    async def generate_quiz(self, text: str) -> str:
        """
        Generates multiple-choice quiz questions with explanations from the given text.

        Args:
            text: The input text to generate quiz questions from.

        Returns:
            A JSON string representing the quiz questions, answers, and explanations.
        """
        system_prompt = """You are a helpful assistant specialized in generating high-quality multiple-choice quiz questions.
        Your task is to create a quiz based on the provided text.
        Each question should have 4 options, with one correct answer and an explanation.
        Ensure the quiz is 100% grounded in the original text and avoids any hallucinations.
        The output should be a JSON array of objects, where each object has 'question', 'options' (an array of strings), 'answer', and 'explanation' fields.

        Example JSON format:
        [
            {{
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "answer": "Paris",
                "explanation": "Paris is the capital and most populous city of France."
            }}
        ]
        """

        user_prompt = f"Generate a multiple-choice quiz from the following text:\n\n{text}"

        messages: List[SystemMessage | UserMessage] = [
            SystemMessage(content=system_prompt),
            UserMessage(content=user_prompt)
        ]

        response = await self.model_client.create(messages=messages, response_format={ "type": "json_object" })
        assert isinstance(response.content, str)
        return response.content
