# Legal Case Analyzer

## Introduction
This project involves creating a Streamlit app that leverages a Large Language Model (LLM) to process, categorize, and analyze case descriptions. The system includes functionalities for inputting new case descriptions, categorizing them, generating summaries, extracting key entities and sentiments, and managing the cases.

## Installations

### Prerequisites
- Python 3.7 or higher
- Virtual environment tool (e.g., `venv` or `virtualenv`)

## Installation

### 1. Clone the repository
   ```bash
   git clone https://github.com/parthparmar0816/Legal-Case-Analyzer.git
   ```
### 2. Create Environment
Create a virtual environment for the project using Terminal:
```bash
python -m venv venv
source venv/bin/activate   
# On Windows use `venv\Scripts\activate`
```

### 3. Install Libraries
Install the necessary libraries using Terminal:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Activate Virtual Environment
Activate your virtual environment in the Terminal:
```bash
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
### 2. Launch the Streamlit App
Run the application using Terminal:
```bash
streamlit run app.py
```

### 3. Using the app
- **OpenAI API Key**: Provide your OpenAI API key in the form available in the sidebar.
- **Input Case Description**: Enter a new case description in the provided form.
- **Case Categorization**: The app will categorize the case into predefined categories (e.g., "Employment Discrimination", "Harassment", "Unfair Dismissal").
- **Case Summarization**: The app generates a concise summary of the case description using the LLM.
- **Case Analysis**: The app extracts key entities and sentiments from the case description.
- **Case Management**: View the list of all cases with their categories, summaries, and analyses. You can also delete cases from the list.

## Future Optimizations
- **Enhanced Case Categorization**: Improve the accuracy of case categorization by fine-tuning the LLM on a larger dataset of case descriptions.
- **Advanced Analysis Features**: Implement additional analysis features such as trend analysis and case similarity detection.
- **User Authentication**: Add user authentication and authorization to restrict access to the app.
- **Database Integration**: Integrate a database to persist case data instead of using in-memory data structures.

   

