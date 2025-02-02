from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os


class MeetingNotesGenerator:

    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key="Enter you Key",
            model_name="llama-3.2-90b-vision-preview"
        )

    def load_transcript(self, file_path: str) -> str:
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"File not found: {file_path}")

    def generate_notes(self, transcript: str) -> str:
        prompt = PromptTemplate.from_template(
            """
            You are an assistant skilled at summarizing meetings. Here's the transcript of a meeting:
            {full_transcript}

            Please generate clear and concise meeting notes. Include:
            - Key discussion points.
            - Decisions made.
            - Action items with assignees.
            - Any unresolved questions or follow-ups.

            Return the notes in a well-structured, professional format.
            """
        )
        chain = prompt | self.llm
        result = chain.invoke(input={"full_transcript": transcript})
        return result.content
