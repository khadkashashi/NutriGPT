import requests
import json


nuti = json.dumps(
    {
      "model": "gemma2:2b",
      "prompt": 'You are generating ingredient data for a nutrition database.\n\nI will provide a list of ingredient names that were generated during the previous 7 days.\n\nYour task is to generate NEW ingredients only. provide nepali foods only \n\nRules:\n- Never generate an ingredient whose name appears in the previous 7 days list.\n- Treat ingredient names as case-insensitive when checking for duplicates.\n- If a previous ingredient is \'Apple\', do not generate \'apple\', \'APPLE\', or any exact name variant.\n- Generate exactly 2 new ingredients.\n- Every generated ingredient name must be unique.\n- None of the generated ingredients may duplicate another generated ingredient.\n- Include a diverse mix of food categories such as grains, vegetables, fruits, dairy, meat, poultry, seafood, legumes, nuts, seeds, spices, herbs, oils, mushrooms, beverages, and sweeteners.\n- Return ONLY valid JSON.\n- Do NOT include explanations, markdown, code fences, comments, or any extra text.\n- The response must begin with \'[\' and end with \']\'.\n- Use "g" as the default unit unless another unit is clearly more appropriate.\n- All nutritional values are per 100 grams.\n- All numeric values must be numbers (not strings).\n- Use realistic nutritional values.\n- Do not generate fictional ingredients.\n- Ensure the JSON is syntactically valid with no trailing commas.\n\nPreviously generated ingredient names (last 7 days):\n\n\n\nIf the list above is empty, there are no restrictions.\n\nReturn exactly this JSON structure:\n[\n  {\n    "name": "string",\n    "unit": "g",\n    "calories_per_100g": 0.0,\n    "protein_per_100g": 0.0,\n    "carbs_per_100g": 0.0,\n    "fat_per_100g": 0.0\n  }\n]\n\nBefore returning the response, verify that none of the generated ingredient names exist in the provided previous 7-day list. Return only the JSON array.',
      "stream": False,
    }
)




def generate_json_data():
    headersList = {"Accept": "*/*", "Content-Type": "application/json"}
    r = requests.post(
        url="http://localhost:11434/api/generate", headers=headersList, data=nuti
    )
    return r.json()["response"]