import os
import uvicorn
import traceback
from pydantic import BaseModel
from fastapi import FastAPI, Response, HTTPException
from transformers import T5Tokenizer, T5ForConditionalGeneration
from googletrans import Translator

# Path to the T5 model
MODEL_PATH = "t5_english" 

# Initialize the translator
translator = Translator()

# Load the model and tokenizer
try:
    tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    raise e

# Initialize FastAPI
app = FastAPI()

class CopywritingRequest(BaseModel):
    product_description: str  # Input description text for the product

@app.get("/")
def index():
    return {"message": "Welcome to the T5 Copywriting API. Visit /docs for API documentation."}

@app.post("/generate_copywriting")
def generate_copywriting(req: CopywritingRequest, response: Response):
    """
    Generate copywriting based on the input product description.
    """
    try:
        # Input text from the request
        product_description = req.product_description.strip()

        # Validate input
        if not product_description:
            raise HTTPException(status_code=400, detail="Product description cannot be empty")

        # Detect language
        detected_lang = translator.detect(product_description).lang

        # Translate to English if not already in English
        if detected_lang != 'en':
            product_description = translator.translate(product_description, src=detected_lang, dest='en').text

        # Prepare input for the model
        input_ids = tokenizer.encode(
            product_description,
            return_tensors="pt",  # Convert to PyTorch tensor
            max_length=512,       # Optional: Limit input length
            truncation=True
        )
        
        # Generate text with customizable hyperparameters
        outputs = model.generate(
            input_ids=input_ids,
            max_length=150,
            num_beams=5,
            repetition_penalty=1.2,
            length_penalty=1.2,
            temperature=0.8,
            early_stopping=True
        )
        
        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return {
            "input_language": detected_lang,
            "translated_input": product_description,
            "generated_copywriting": generated_text
        }
    
    except HTTPException as http_err:
        raise http_err  # Re-raise HTTP exceptions
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return {"error": f"Internal Server Error: {str(e)}"}

# Starting the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Listening on http://0.0.0.0:{port}")
    uvicorn.run(app, host='0.0.0.0', port=port)
