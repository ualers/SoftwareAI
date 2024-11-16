import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

class SolanaAnalyzer:
    def __init__(self, symbol='SOL-USD'):
        """Inicializa o analisador com o símbolo da criptomoeda."""
        self.symbol = symbol
        self.data = None

    def collect_data(self, start_date='2020-01-01'):
        """Coleta dados históricos de preços e volumes da Solana."""
        try:
            self.data = yf.download(self.symbol, start=start_date)
            if self.data.empty:
                raise ValueError("Nenhum dado encontrado. Verifique o símbolo ou a data.")
            print("Dados coletados com sucesso.")
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")

    def calculate_indicators(self):
        """Calcula indicadores técnicos: MA, RSI, MACD, Bandas de Bollinger e Estocástico."""
        if self.data is None:
            raise Exception("Dados não carregados. Execute collect_data primeiro.")

        self.calculate_moving_average()
        self.calculate_rsi()
        self.calculate_bollinger_bands()
        self.calculate_macd()
        self.calculate_stochastic()

        print("Indicadores calculados com sucesso.")

    def calculate_moving_average(self, window=20):
        """Calcula a Média Móvel."""
        self.data['MA20'] = self.data['Close'].rolling(window=window).mean()

    def calculate_rsi(self, window=14):
        """Calcula o Índice de Força Relativa (RSI)."""
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

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

    def calculate_stochastic(self, window=14):
        """Calcula o Estocástico."""
        min_low = self.data['Close'].rolling(window=window).min()
        max_high = self.data['Close'].rolling(window=window).max()
        self.data['Stochastic'] = 100 * (self.data['Close'] - min_low) / (max_high - min_low)

    def plot_data(self):
        """Gera gráficos para visualização das tendências de preço e indicadores."""
        if self.data is None:
            raise Exception("Dados não carregados. Execute collect_data primeiro.")

        plt.figure(figsize=(14, 12))

        # Gráfico dos preços e Bandas de Bollinger
        plt.subplot(4, 1, 1)
        plt.plot(self.data[['Close', 'MA20', 'Upper Band', 'Lower Band']])
        plt.title('Preço da Solana e Bandas de Bollinger')
        plt.legend(['Preço', 'MA20', 'Banda Superior', 'Banda Inferior'])

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

        # Alertas para cruzamentos de média
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

    def save_analysis_report(self, filename='solana_analysis_report.txt'):
        """Salva um relatório da análise em um arquivo texto."""
        if self.data is None:
            raise Exception("Dados não carregados. Execute collect_data primeiro.")

        with open(filename, 'w') as file:
            file.write(f"Análise para {self.symbol} em {self.data.index[-1].date()}
")
            file.write(f"Preço atual: {self.data['Close'].iloc[-1]:.2f}
")
            file.write(f"MA20: {self.data['MA20'].iloc[-1]:.2f}
")
            file.write(f"RSI: {self.data['RSI'].iloc[-1]:.2f}
")
            file.write(f"MACD: {self.data['MACD'].iloc[-1]:.2f}
")
            file.write(f"Estocástico: {self.data['Stochastic'].iloc[-1]:.2f}
")
            file.write(f"Alertas:
")
            last_ma = self.data['MA20'].iloc[-1]
            last_price = self.data['Close'].iloc[-1]
            last_rsi = self.data['RSI'].iloc[-1]
            last_stochastic = self.data['Stochastic'].iloc[-1]
            
            # Alertas para cruzamentos de média
            if last_price > last_ma:
                file.write(f"O preço ({last_price:.2f}) cruzou acima da MA de 20 dias ({last_ma:.2f}).
")
            elif last_price < last_ma:
                file.write(f"O preço ({last_price:.2f}) cruzou abaixo da MA de 20 dias ({last_ma:.2f}).
")

            # Alertas para o RSI
            if last_rsi > 70:
                file.write(f"O RSI está alto ({last_rsi:.2f}).
")
            elif last_rsi < 30:
                file.write(f"O RSI está baixo ({last_rsi:.2f}).
")

            # Alertas para o Estocástico
            if last_stochastic > 80:
                file.write(f"O Estocástico está alto ({last_stochastic:.2f}).
")
            elif last_stochastic < 20:
                file.write(f"O Estocástico está baixo ({last_stochastic:.2f}).
")

        print(f"Relatório salvo em '{filename}'.")

    def set_alert_thresholds(self, rsi_high=70, rsi_low=30, stochastic_high=80, stochastic_low=20):
        """Permite ao usuário configurar limites personalizados para alertas de RSI e Estocástico."""
        self.rsi_high = rsi_high
        self.rsi_low = rsi_low
        self.stochastic_high = stochastic_high
        self.stochastic_low = stochastic_low

if __name__ == '__main__':
    try:
        analyzer = SolanaAnalyzer()
        analyzer.collect_data()
        analyzer.calculate_indicators()
        analyzer.plot_data()
        analyzer.alert_system()
        analyzer.save_analysis_report()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")