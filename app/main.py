from meeting_notes_generator import MeetingNotesGenerator
import streamlit as st

def main():
    st.title("Meeting Notes Generator")

    # Input for the transcript (text box)
    transcript = st.text_area("Enter the meeting transcript here:", height=300)

    # Configuration
    #file_path = "resource/sample_transcript.txt"

    if st.button("Generate Notes"):
        if transcript:
            # Step 1: Initialize the MeetingNotesGenerator
            generator = MeetingNotesGenerator()

            # Step 2: Load the transcript
            #transcript = generator.load_transcript(file_path)

            # Step 3: Generate meeting notes
            notes = generator.generate_notes(transcript)

            # Step 4: Display the generated notes
            st.subheader("Generated Meeting Notes:")
            st.write(notes)
        else:
            st.warning("Please enter a transcript before submitting.")


# Run the script
if __name__ == "__main__":
    main()
