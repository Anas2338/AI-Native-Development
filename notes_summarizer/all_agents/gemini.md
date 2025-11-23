# Gemini Model Configuration for Agents

This document outlines the configuration of the Gemini model used by the agents in this project. The `agents/model.py` file is responsible for setting up the `OpenAIChatCompletionsModel` to interact with the Gemini API.

## Configuration Details

- **Environment Variables**: The `GEMINI_API_KEY` is loaded from the `.env` file to authenticate with the Gemini API.
- **API Client**: An `AsyncOpenAI` client is configured with the Gemini API's base URL (`https://generativelanguage.googleapis.com/v1beta/openai/`).
- **Model Instance**: The `OpenAIChatCompletionsModel` is initialized with the `gemini-2.5-flash` model and the custom `AsyncOpenAI` client. This setup allows the summarizer and quiz generator agents to leverage the Gemini model for their operations.

## Agent Integration

The `summarize_agent.py` and `quiz_agent.py` modules within the `agents/` directory leverage this configured Gemini model. They import the `model` instance from `agents.model` to perform their respective natural language processing tasks, ensuring that all summarization and quiz generation operations are powered by the Gemini 2.5 Flash model.