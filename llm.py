import openai
import json

"""
Analyzes a given case description using a legal expert AI model. 
Parameters:
    case_description (str): The description of the case to be analyzed.
    api_key (str): The API key for accessing the OpenAI services.
Returns:
    dict: A JSON object containing categorized case, summary, entities, and sentiments.
"""
def analyze_case_description(case_description, api_key):
    openai.api_key = api_key
    
    system_text = '''
    You are a legal expert AI model. When provided with a case description, give accurate responses to all of the user's instructions using the case description. If you cannot find the field asked for by the user, give an empty string instead in json format.
    '''
    user_1 = f"Here is the case description: {case_description}. Give accurate responses to all the below instructions using the case description and provide the final response in a single json object"
    user_2 = "1. Categorize the case into one of the following categories: Employment Discrimination, Harassment, Unfair Dismissal. Format it in json like {category:''}"
    user_3 = "2. Generate a concise summary of the case. Format it in json like {summary:''}"
    user_4 = "3. Extract relevant key entities and types (such as persons, organizations, dates, locations) from the case description. Format it in json like {entities:[{'entity':'','type':''}]}"
    user_5 = "4. Analyze the case description and give sentiments on entities from the case description. Format it in json like {sentiments:[{'entity':'','sentiment':''}]}"
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_text},
            {"role": "user", "content": user_1},
            {"role": "user", "content": user_2},
            {"role": "user", "content": user_3},
            {"role": "user", "content": user_4},
            {"role": "user", "content": user_5}
        ],
        max_tokens=2000,
        temperature=0.7
    )
    
    result = response.choices[0].message.content
    return json.loads(result)


