def calfp(frates, fac_rate):
    fun_units = [
        "Entradas Externas",
        "Saídas Externas",
        "Consultas Externas",
        "Arquivos Lógicos Internos",
        "Arquivos de Interface Externos"
    ]

    # Taxas de Peso
    wt_rates = ["Baixo", "Médio", "Alto"]

    # Fatores de Peso
    wt_factors = [
        [3, 4, 6],
        [4, 5, 7],
        [3, 4, 6],
        [7, 10, 15],
        [5, 7, 10],
    ]

    UFP = 0

    # Calculando UFP (Ponto de Função Não Ajustado)
    for i in range(5):
        for j in range(3):
            freq = frates[i][j]
            UFP += freq * wt_factors[i][j]

    # 14 fatores
    aspects = [
        "é necessário backup e recuperação confiáveis?",
        "a comunicação de dados é necessária?",
        "existem funções de processamento distribuído?",
        "o desempenho é crítico?",
        "o sistema funcionará em um ambiente operacional existente e muito utilizado?",
        "é necessária entrada de dados online?",
        "a entrada de dados online requer que a transação de entrada seja construída em várias telas ou operações?",
        "os arquivos mestres são atualizados online?",
        "as entradas, saídas, arquivos ou consultas são complexos?",
        "o processamento interno é complexo?",
        "o código é projetado para ser reutilizável?",
        "as conversões e a instalação estão incluídas no projeto?",
        "o sistema é projetado para várias instalações em diferentes organizações?",
        "a aplicação é projetada para facilitar mudanças e facilidade de uso pelo usuário?"
    ]

    # Escala de Avaliação dos Fatores
    # Avalie os aspectos em uma escala de 0 a 5
    sumF = 0

    # Coletando a Taxa de Fatores
    for i in range(14):
        rate = fac_rate  # Isso pode ser modificado para aceitar entradas individuais
        sumF += rate

    # Calcular CAF
    CAF = 0.65 + 0.01 * sumF

    # Calcular Ponto de Função (FP)
    FP = UFP * CAF

    # Valores de Saída
    print("Análise de Ponto de Função :-")
    print("Pontos de Função Não Ajustados (UFP) : ", UFP)
    print("Fator de Ajuste de Complexidade (CAF) : ", CAF)
    print("Pontos de Função (FP) : ", FP)


# Função principal
if __name__ == "__main__":
    frates = [
        [0, 50, 0],
        [0, 40, 0],
        [0, 35, 0],
        [0, 6, 0],
        [0, 4, 0]
    ]

    fac_rate = 3

    calfp(frates, fac_rate)
