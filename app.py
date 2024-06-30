import streamlit as st
from llm import analyze_case_description


st.title("Case Analyzer App")

# Sidebar for OpenAI API key input and case management
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    st.subheader("All Cases")
    for case_id, case_data in list(st.session_state.get('cases', {}).items()):
        with st.expander(f"Case {case_id}: {case_data['category']}"):
            st.write(f"**Summary:** {case_data['summary']}")
            st.write("**Entities:**")
            for entity in case_data['entities']:
                st.write(f"- {entity['entity']} ({entity['type']})")
            st.write("**Sentiments:**")
            for sentiment in case_data['sentiments']:
                st.write(f"- {sentiment['entity']} ({sentiment['sentiment']})")
            if st.button(f"Delete Case {case_id}", key=f"delete_{case_id}"):
                del st.session_state.cases[case_id]
                st.rerun()

# In-memory data structure to store cases
if 'cases' not in st.session_state:
    st.session_state.cases = {}



def display_results(result):
    category = result.get("category", "")
    summary = result.get("summary", "")
    entities = result.get("entities", [])
    sentiments = result.get("sentiments", [])

    st.subheader("Category")
    st.info(category)

    st.subheader("Summary")
    st.info(summary)

    st.subheader("Entities")
    for entity in entities:
        st.write(f"Entity: {entity['entity']}, Type: {entity['type']}")

    st.subheader("Sentiments")
    for sentiment in sentiments:
        st.write(f"Entity: {sentiment['entity']}, Sentiment: {sentiment['sentiment']}")

with st.form("case_form"):
    text = st.text_area("Enter case description:", "Enter Case Description here")
    submitted = st.form_submit_button("Submit")
    
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        try:
            response = analyze_case_description(text, openai_api_key)
            if st.session_state.cases:
                case_id = max(st.session_state.cases.keys()) + 1
            else:
                case_id = 1
            st.session_state.cases[case_id] = response
            # Store the current case separately
            st.session_state.current_case = response  
            st.success("Case added successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error analyzing case description: {e}")

# Display the current case
if 'current_case' in st.session_state:
    st.header("Current Case Analysis")
    display_results(st.session_state.current_case)
