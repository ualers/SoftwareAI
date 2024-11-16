import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

class BitcoinAnalyzer:
    def __init__(self, symbol='BTC-USD'):
        self.symbol = symbol
        self.data = None

    def collect_data(self, start_date='2020-01-01'):
        """Coleta dados históricos de preços e volumes da Bitcoin."""
        try:
            self.data = yf.download(self.symbol, start=start_date)
            if self.data.empty:
                raise ValueError("Nenhum dado encontrado. Verifique o símbolo ou a data.")
            print("Dados coletados com sucesso.")
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")

    def calculate_indicators(self):
        """Calcula indicadores técnicos: MA, RSI, Bandas de Bollinger, MACD e Estocástico."""
        if self.data is None:
            raise Exception("Dados não carregados. Execute collect_data primeiro.")

        # Cálculo da Média Móvel
        self.data['MA20'] = self.data['Close'].rolling(window=20).mean()

        # Cálculo do Índice de Força Relativa (RSI)
        self.data['RSI'] = self.calculate_rsi(self.data['Close'])

        # Cálculo das Bandas de Bollinger
        self.calculate_bollinger_bands()

        # Cálculo do MACD
        self.calculate_macd()

        # Cálculo do Estocástico
        self.data['Stochastic'] = self.calculate_stochastic(self.data['Close'])

        print("Indicadores calculados com sucesso.")

    @staticmethod
    def calculate_rsi(series, window=14):
        """Calcula o Índice de Força Relativa (RSI) para um dado conjunto de preços."""
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_bollinger_bands(self):
        """Calcula as Bandas de Bollinger."""
        self.data['20 Std'] = self.data['Close'].rolling(window=20).std()
        self.data['Upper Band'] = self.data['MA20'] + (self.data['20 Std'] * 2)
        self.data['Lower Band'] = self.data['MA20'] - (self.data['20 Std'] * 2)

    def calculate_macd(self):
        """Calcula o MACD."""
        self.data['EMA12'] = self.data['Close'].ewm(span=12, adjust=False).mean()
        self.data['EMA26'] = self.data['Close'].ewm(span=26, adjust=False).mean()
        self.data['MACD'] = self.data['EMA12'] - self.data['EMA26']
        self.data['Signal Line'] = self.data['MACD'].ewm(span=9, adjust=False).mean()

    @staticmethod
    def calculate_stochastic(series, window=14):
        """Calcula o Estocástico para um dado conjunto de preços."""
        min_low = series.rolling(window=window).min()
        max_high = series.rolling(window=window).max()
        return 100 * (series - min_low) / (max_high - min_low)

    def plot_data(self):
        """Gera gráficos para visualização das tendências e padrões de preços."""
        if self.data is None:
            raise Exception("Dados não carregados. Execute collect_data primeiro.")

        plt.figure(figsize=(14, 12))

        # Gráfico dos preços e Bandas de Bollinger
        plt.subplot(4, 1, 1)
        plt.plot(self.data[['Close', 'MA20', 'Upper Band', 'Lower Band']], 
                 label=['Preço', 'MA20', 'Banda Superior', 'Banda Inferior'])
        plt.title('Preço do Bitcoin e Bandas de Bollinger')
        plt.legend()

        # Gráfico do RSI
        plt.subplot(4, 1, 2)
        plt.plot(self.data['RSI'], label='RSI', color='orange')
        plt.title('Índice de Força Relativa (RSI)')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')
        plt.legend()

        # Gráfico do MACD
        plt.subplot(4, 1, 3)
        plt.plot(self.data['MACD'], label='MACD', color='blue')
        plt.plot(self.data['Signal Line'], label='Signal Line', color='red')
        plt.title('MACD')
        plt.legend()

        # Gráfico do Estocástico
        plt.subplot(4, 1, 4)
        plt.plot(self.data['Stochastic'], label='Estocástico', color='purple')
        plt.axhline(80, linestyle='--', alpha=0.5, color='red')
        plt.axhline(20, linestyle='--', alpha=0.5, color='green')
        plt.title('Estocástico')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def alert_system(self):
        """Configura alertas para condições específicas do mercado."""
        if self.data is None:
            raise Exception("Dados não carregados. Execute collect_data primeiro.")

        last_ma = self.data['MA20'].iloc[-1]
        last_price = self.data['Close'].iloc[-1]
        last_rsi = self.data['RSI'].iloc[-1]
        last_stochastic = self.data['Stochastic'].iloc[-1]

        # Alertas para cruzamento de média
        if last_price > last_ma:
            print(f"Aviso: O preço ({last_price:.2f}) cruzou acima da MA de 20 dias ({last_ma:.2f}). Considere comprar.")
        elif last_price < last_ma:
            print(f"Aviso: O preço ({last_price:.2f}) cruzou abaixo da MA de 20 dias ({last_ma:.2f}). Considere vender.")

        # Alertas para o RSI
        if last_rsi > 70:
            print(f"Aviso: O RSI está alto ({last_rsi:.2f}). Considere realizar vendas.")
        elif last_rsi < 30:
            print(f"Aviso: O RSI está baixo ({last_rsi:.2f}). Considere realizar compras.")

        # Alertas para o Estocástico
        if last_stochastic > 80:
            print(f"Aviso: O Estocástico está alto ({last_stochastic:.2f}). Considere realizar vendas.")
        elif last_stochastic < 20:
            print(f"Aviso: O Estocástico está baixo ({last_stochastic:.2f}). Considere realizar compras.")

if __name__ == '__main__':
    try:
        analyzer = BitcoinAnalyzer()
        analyzer.collect_data()
        analyzer.calculate_indicators()
        analyzer.plot_data()
        analyzer.alert_system()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")