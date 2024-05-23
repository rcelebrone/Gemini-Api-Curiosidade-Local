# Função `curiosidade`

## Descrição
Esta função é um endpoint HTTP que utiliza a API do Google Generative AI para fornecer curiosidades sobre locais ou endereços fornecidos. Se o input não for um local ou endereço válido, a função retornará um erro de solicitação incorreta (Bad Request).

## Configuração
Para configurar esta função, você precisará das seguintes dependências:
- `functions_framework`
- `google.generativeai`

## Variáveis de Ambiente
- `API_KEY_AQUI`: Substitua esta variável pela sua chave de API do Google Generative AI.

## Estrutura do Código
- Importações necessárias
- Configuração da API
- Configuração das opções de geração e segurança
- Configuração do modelo de geração
- Inicialização de uma sessão de chat com um histórico predefinido
- Lógica para processar a solicitação HTTP e retornar a resposta apropriada

## Exemplo de Sucesso
**Input**: `R Silva Jardim 51 Santo André`  
**Output**:
```json
{
  "endereco": "Rua Silva Jardim, 51 - Santo André / SP",
  "curiosidade": "O bairro Santa Terezinha em Santo André é conhecido por abrigar o tradicional Colégio Santa Terezinha, fundado em 1939, um marco educacional na região",
  "statusCode": 200
}
```

## Exemplo de Insucesso
**Input**: `bala de uva`  
**Output**:
```json
{
  "statusCode": 400,
  "mensagem": "bala de uva não é um local ou endereço, é um doce muito bom"
}
```

## Uso
Esta função deve ser implantada em um ambiente compatível com o `functions_framework`, como o Google Cloud Functions.

Para enviar uma solicitação HTTP, use um formato JSON conforme os exemplos de sucesso e insucesso. A função processará a solicitação e retornará a curiosidade sobre o local ou um erro apropriado se o input não for válido.

## Licença
Este projeto está licenciado sob os termos da licença MIT.
