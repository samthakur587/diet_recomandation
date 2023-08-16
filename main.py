import os
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Form
from langchain.llms import OpenAI
from apikey import apikey
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from fastapi.middleware.cors import CORSMiddleware

api_key = os.environ.get('OPENAI_API_KEY')
# Set your OpenAI API key here
os.environ['OPENAI_API_KEY'] = apikey

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific requirements
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prompt templates
breakfast_template = PromptTemplate(
    input_variables=['bmi','vag','diabetes','meditation','gory','nati','regionality','exercise','goal'],
    template="""You are a knowledgeable AI chatbot dedicated to providing personalized food recommendations based on an individual's health and preferences. Given the provided information about the person, including their Body Mass Index (BMI), vegetarian status (VAG), diabetes condition, meditation routine, grocery availability at home (GORY), nationality (NATI), regionality, and exercise activity for the day, goal of user, I need your guidance on crafting nutritious meal suggestions.
Please provide guidance on suitable food options for breakfast, lunch, and dinner, including protein, nutritional content, and fat content. Keep in mind the person's specific dietary needs and health conditions.

Person's Profile:
- Body Mass Index (BMI): {bmi}
- Vegetarian Status: {vag}
- Diabetes Condition: {diabetes}
- Meditation Routine: {meditation}
- Grocery Availability: {gory}
- Nationality: {nati}
- Regionality: {regionality}
- Exercise Activity: {exercise}
- Goal: {goal}

Based on this information, what would you recommend for their breakfast, lunch, and dinner, considering their dietary preferences and health goals? Also provide nutrition statistics for every meal.
"""
)

def calculate_bmi(height: float, weight: float) -> float:
    # Calculate BMI using height (in meters) and weight (in kilograms)
    bmi = weight / (height * height)
    return bmi

class UserInputModel(BaseModel):
    bmi: float
    vag: bool
    diabetes: bool
    meditation: str
    gory: str
    nati: str
    regionality: str
    exercise: str
    goal: str

def get_breakfast_recommendation(user_input_dict):
    try:
        breakfast_memory = ConversationBufferMemory(input_key="bmi", memory_key='chat_history')
        llm = OpenAI(temperature=0.9)
        breakfast_chain = LLMChain(llm=llm, prompt=breakfast_template, verbose=True, output_key='title', memory=breakfast_memory)
        
        if user_input_dict:
            breakfast = breakfast_chain.run(user_input_dict)
            return breakfast
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return None
@app.post("/calculate_bmi", response_model=float, description="Calculate BMI (Body Mass Index). Please provide weight in kilograms and height in meters.")
def calculate_bmi_route(height: float, weight: float):
    try:
        bmi = calculate_bmi(height, weight)
        return bmi
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recommend")
def recommend_meals(user_input: UserInputModel):
    try:
        user_input_dict = user_input.dict()
        breakfast = get_breakfast_recommendation(user_input_dict)
        
        if breakfast is not None:
            return {"breakfast_recommendation": breakfast}
        else:
            return {"message": "Unable to generate recommendation."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)