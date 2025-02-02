**Meeting Notes Generator**

**Overview**
The Meeting Notes Generator is a Streamlit-based application that automatically generates structured meeting notes from a given transcript using a Large Language Model (LLM). It extracts key discussion points, decisions made, action items, and follow-ups from the provided text.

**Features
•	Accepts meeting transcripts as input.
•	Uses an AI-powered model (Llama-3.2-90B) to generate structured meeting notes.
•	Provides a well-formatted summary of key points, decisions, and action items.
•	Simple and intuitive Streamlit-based UI.

**Installation**
**Prerequisites**
•	Python 3.8+
•	Streamlit
•	LangChain
•	LangChain Groq

**Setup Instructions**

1.	Clone the repository:
git clone https://github.com/your-username/meeting-notes-generator.git
cd meeting-notes-generator

2.	Install the required dependencies:
pip install -r requirements.txt
3.	Set up your API key in meeting_notes_generator.py:
self.llm = ChatGroq(
    temperature=0,
    groq_api_key="Enter your Key",
    model_name="llama-3.2-90b-vision-preview"
)

**Usage**
1.	Run the Streamlit app:
streamlit run main.py
2.	Enter the meeting transcript in the text area.
3.	Click the Generate Notes button to extract structured meeting notes.
4.	View the generated summary, including key points, decisions, and action items.

**Project Structure**
meeting-notes-generator/
│-- main.py                  # Streamlit UI for input and output
│-- meeting_notes_generator.py # Core logic for generating meeting notes
│-- requirements.txt         # Required dependencies
│-- README.md                # Project documentation


**Dependencies**
Ensure you have the following dependencies installed:
•	streamlit
•	langchain
•	langchain_groq
•	python-dotenv
Install them using:
pip install -r requirements.txt

**Contributing**
Feel free to fork this repository, open issues, or submit pull requests for enhancements.

**License**
This project is licensed under the MIT License.

**Author**
Developed by Dhivya.
