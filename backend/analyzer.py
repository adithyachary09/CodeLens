import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Initialize the model with JSON output configuration
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "response_mime_type": "application/json",
    }
)

def analyze_code_complexity(code: str, language: str) -> dict:
    """
    Sends the code to Gemini API and returns a structured JSON analysis.
    """
    if not code.strip():
        return {"error": "Code input is empty."}

    prompt = f"""
    You are an expert software engineer and algorithm analyst.
    Analyze the following {language} code. 
    
    CRITICAL INSTRUCTION: If the input is plain text, an essay, a recipe, or clearly NOT valid programming code, you MUST reject it by returning EXACTLY this JSON and nothing else:
    {{"error": "Invalid input. Please provide valid source code."}}
    
    Otherwise, you MUST return a valid JSON object with EXACTLY this structure:
    {{
        "functions": ["function_name_1", "function_name_2"],
        "time_complexity": {{"function_name_1": "O(...) - explanation"}},
        "space_complexity": {{"function_name_1": "O(...) - explanation"}},
        "inefficient_patterns": ["List of bad patterns detected"],
        "optimized_code": "The fully rewritten optimized version of the code",
        "optimization_explanation": "Detailed explanation of what changed and why"
    }}

    Code to analyze:
    ```{language}
    {code}
    ```
    """

    try:
        response = model.generate_content(prompt)
        
        # Safely extract text in case of safety blocks
        try:
            raw_text = response.text.strip()
        except ValueError:
            return {"error": "API Error: The response was blocked by safety filters."}
        
        # Strip markdown formatting if present
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        elif raw_text.startswith("```"):
            raw_text = raw_text[3:]
            
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        # Parse the JSON response
        analysis_result = json.loads(raw_text.strip())
        return analysis_result

    except json.JSONDecodeError:
        return {"error": "Failed to parse API response. The model did not return valid JSON."}
    except Exception as e:
        return {"error": f"API Error: {str(e)}"}