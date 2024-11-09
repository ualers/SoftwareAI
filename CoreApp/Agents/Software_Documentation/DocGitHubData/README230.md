
# Documentação para o GitHub

## Introdução
O **Conversor de Moedas** é uma aplicação Python que permite converter valores entre diferentes moedas utilizando taxas de câmbio obtidas de uma API. É uma ferramenta útil para viajantes, comerciantes e qualquer pessoa que precise realizar transações em múltiplas moedas.

## Instalação
Para instalar e usar o Conversor de Moedas, siga estas etapas:

1. **Pré-requisitos**:
   - Você deve ter o Python instalado em sua máquina. Caso ainda não tenha, faça o download em [python.org](https://www.python.org/downloads/).

2. **Instalação de bibliotecas**:
   - Você precisará instalar a biblioteca `requests`. Execute o seguinte comando no terminal:
   
   ```bash
   pip install requests
   ```

3. **Download do Script**:
   - Salve o código acima em um arquivo chamado `currency_converter.py`.

## Uso
Para usar o Conversor de Moedas, siga estes passos:

1. Execute o script no terminal:
   
   ```bash
   python currency_converter.py
   ```

2. Quando solicitado, insira a moeda base para a conversão (ex: USD, EUR).

3. O programa exibirá as taxas de câmbio disponíveis. 

4. Digite a moeda de origem, a moeda de destino e o valor que deseja converter.

5. O resultado da conversão será exibido em formato monetário.

## Referência de API
- **CurrencyConverter**: Classe principal responsável pela conversão de moedas.
    - `__init__()`: Inicializa a classe definindo a URL da API de taxas de câmbio.
    - `get_exchange_rates(base_currency)`: Obtém as taxas de câmbio para a moeda base especificada. Retorna um dicionário de taxas.
    - `convert_currency(amount, from_currency, to_currency, rates)`: Converte um valor de uma moeda para outra, com base nas taxas fornecidas.

## Contribuição
Contribuições são bem-vindas! Para contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas modificações:
   
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Realize suas alterações e faça um commit:
   
   ```bash
   git commit -m "Descrição das suas alterações"
   ```
4. Envie sua branch:
   
   ```bash
   git push origin minha-contribuicao
   ```
5. Abra um pull request no GitHub.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE). Para mais detalhes, consulte o arquivo LICENSE no repositório.