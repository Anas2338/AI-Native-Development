import streamlit as st
from core.pdf import extract_text_from_pdf
from core.summarize import process_summarization
from core.quiz import process_quiz_generation
from all_agents.model import model as gemini_model_client
import json
from io import BytesIO
import asyncio

def main():
    st.set_page_config(page_title="Study Notes Summarizer & Quiz Generator", layout="wide")
    st.title("📚 Study Notes Summarizer & Quiz Generator")

    # Instantiate GeminiModel once
    gemini_model_client_instance = gemini_model_client

    # File uploader
    pdf_file = st.file_uploader("Upload your PDF document", type=["pdf"])

    if pdf_file:
        st.success("PDF uploaded successfully!")
        
        # Read the file into a BytesIO object
        pdf_bytes = BytesIO(pdf_file.read())

        # Placeholder for summary style selection
        st.subheader("Choose Summary Style:")
        summary_style = st.radio(
            "Select a style",
            ("Bullet Notes", "Blocks", "Flashcards"),
            index=0,
        )

        if st.button("Generate Notes & Quiz"):
            with st.spinner("Extracting text from PDF..."):
                extracted_text = extract_text_from_pdf(pdf_bytes)
            
            if extracted_text:
                st.success("Text extracted successfully!")
                
                with st.expander("Extracted Text"):
                    st.text_area("Full Text", extracted_text, height=300)

                # Generate Summary
                try:
                    with st.spinner(f"Generating {summary_style} summary..."):
                        summary = asyncio.run(process_summarization(extracted_text, summary_style, gemini_model_client_instance)) # Await the coroutine
                    
                    st.subheader(f"{summary_style} Summary:")
                    st.write(summary)
                except Exception as e:
                    st.exception(e)

                # Generate Quiz
                try:
                    with st.spinner("Generating quiz questions..."):
                        quiz_json_string = asyncio.run(process_quiz_generation(extracted_text, gemini_model_client_instance)) # Await the coroutine
                    
                    st.subheader("Generated Quiz:")
                    try:
                        # Strip markdown fences before loading JSON
                        cleaned_quiz_json_string = quiz_json_string.strip()
                        if cleaned_quiz_json_string.startswith("```json"):
                            cleaned_quiz_json_string = cleaned_quiz_json_string[len("```json"):].strip()
                        if cleaned_quiz_json_string.endswith("```"):
                            cleaned_quiz_json_string = cleaned_quiz_json_string[:-len("```")].strip()

                        quiz_data = json.loads(cleaned_quiz_json_string)
                        if isinstance(quiz_data, list):
                            for i, q in enumerate(quiz_data):
                                st.markdown(f"**Question {i+1}:** {q['question']}")
                                for option in q['options']:
                                    st.markdown(f"- {option}")
                                st.markdown(f"**Answer:** {q['answer']}")
                                st.markdown(f"**Explanation:** {q['explanation']}")
                                st.markdown("---")
                        else:
                            st.exception(ValueError("Error: Quiz data is not in expected list format."))
                            st.json(quiz_data)
                    except json.JSONDecodeError:
                        st.error(f"Failed to decode quiz data. Raw response: {quiz_json_string}")
                    except KeyError as ke:
                        st.exception(ke)
                except Exception as e:
                    st.exception(e)
            else:
                st.error("Failed to extract text from PDF. Please try another file.")

if __name__ == "__main__":
    main()