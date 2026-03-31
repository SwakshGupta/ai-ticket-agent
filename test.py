from models.llm import generate_response

response = generate_response(
    "Explain what is a database error in simple terms"
)

print(response)