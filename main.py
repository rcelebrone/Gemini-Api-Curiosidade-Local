import functions_framework
import os
import google.generativeai as genai

@functions_framework.http
def curiosidade(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    genai.configure(api_key="API_KEY_AQUI")

    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }
    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
    ]

    model = genai.GenerativeModel(
      model_name="gemini-1.5-pro-latest",
      safety_settings=safety_settings,
      generation_config=generation_config,
      system_instruction="Aja como uma API, retorne sempre uma curiosidade a respeito do local ou endereço que lhe for informado. Se Você receber algo diferente de um local ou endereço, deverá retornar bad request. Abaixo vou apresentar exemplo de sucesso (quando lhe enviarem um endereço ou local valido) e um exemplo onde vc deve retornar o erro.\n\nExemplo de sucesso:\ninput: R Silva Jardim 51 Santo André\noutput: {\n \"endereco\": \"Rua Silva Jardim, 51 - Santo André / SP\",\n \"curiosidade\": \"O bairro Santa Terezinha em Santo André é conhecido por abrigar o tradicional Colégio Santa Terezinha, fundado em 1939, um marco educacional na região\",\n \"statusCode\": 200\n}\n\nExemplo de insucesso:\ninput: bala de uva\noutput: {\n \"statusCode\": 400,\n \"mensagem\": \"bala de uva não é um local ou endereço, é um doce muito bom\"\n}",
    )

    chat_session = model.start_chat(
      history=[
        {
          "role": "user",
          "parts": [
            "sorvete de licor",
          ],
        },
        {
          "role": "model",
          "parts": [
            "{\n \"statusCode\": 400,\n \"mensagem\": \"sorvete de licor não é um local ou endereço, é uma sobremesa\" \n}\n",
          ],
        },
      ]
    )

    if request_json and 'name' in request_json:
        response = chat_session.send_message(request_json['name'])
    elif request_args and 'name' in request_args:
        response = chat_session.send_message(request_args['name'])
    else:
        name = 'fail'
    return response.text
