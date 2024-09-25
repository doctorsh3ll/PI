def classificar_tarefa(complexidade, tempo_estimado, recursos_necessários):
    """
    Classifica a tarefa em 'Baixo', 'Médio' ou 'Alto' com base em critérios.
    
    Args:
        complexidade (int): 1 a 5 (1 - Muito simples, 5 - Muito complexo)
        tempo_estimado (int): Tempo estimado em horas
        recursos_necessários (int): Número de recursos necessários (pessoas, ferramentas, etc.)

    Returns:
        str: Categoria da tarefa ('Baixo', 'Médio', 'Alto')
    """
    
    # Cálculo da classificação
    if complexidade <= 2 and tempo_estimado <= 2 and recursos_necessários <= 2:
        return "Baixo"
    elif (3 <= complexidade <= 4) or (3 <= tempo_estimado <= 4) or (3 <= recursos_necessários <= 4):
        return "Médio"
    else:
        return "Alto"


def main():
    print("Classificação de Tarefas")
    
    # Coletando dados do usuário
    complexidade = int(input("Insira a complexidade da tarefa (1-5): "))
    tempo_estimado = int(input("Insira o tempo estimado em horas: "))
    recursos_necessários = int(input("Insira o número de recursos necessários: "))

    # Classificando a tarefa
    categoria = classificar_tarefa(complexidade, tempo_estimado, recursos_necessários)

    print(f"A tarefa é classificada como: {categoria}")


# Executando a função principal
if __name__ == "__main__":
    main()
