import ast

def calcular_complexidade(codigo):
    """
    Calcula a complexidade de uma tarefa com base no código fornecido.
    
    Args:
        codigo (str): Código-fonte a ser analisado.

    Returns:
        int: Nível de complexidade (1 a 5).
    """
    # Contando linhas, funções, loops e condicionais
    num_linhas = len(codigo.strip().split('\n'))
    num_funcoes = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(ast.parse(codigo)))
    num_loops = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(ast.parse(codigo)))
    num_condicionais = sum(isinstance(node, ast.If) for node in ast.walk(ast.parse(codigo)))
    num_recursao = sum(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) for node in ast.walk(ast.parse(codigo)))

    # Calculando a complexidade
    complexidade = 1  # Inicia com 1 (muito simples)

    if num_linhas > 30:
        complexidade += 1
    if num_funcoes > 4:
        complexidade += 1
    if num_loops > 2:
        complexidade += 1
    if num_condicionais > 3:
        complexidade += 1
    if num_recursao > 0:
        complexidade += 1  # A presença de recursão aumenta a complexidade

    # Limitar a complexidade entre 1 e 5
    return min(complexidade, 5)

def verificar_unidade_funcao(codigo):
    """
    Verifica as unidades de função às quais o código se relaciona.
    
    Args:
        codigo (str): Código-fonte a ser analisado.

    Returns:
        list: Lista de nomes de unidades de função ou ["pedro"] se não se relacionar.
    """
    fun_units = [
        "Entradas Externas",
        "Saídas Externas",
        "Consultas Externas",
        "Arquivos Lógicos Internos",
        "Arquivos de Interface Externos"
    ]

    # Palavras-chave para identificar unidades de função
    keywords = {
        "Entradas Externas": ["input", "entrada", "dados", "formulário", "request", "POST"],
        "Saídas Externas": ["print", "saída", "resultado", "relatório", "GET"],
        "Consultas Externas": ["consulta", "buscar", "pesquisar", "query"],
        "Arquivos Lógicos Internos": ["arquivo", "dados internos", "persistência"],
        "Arquivos de Interface Externos": ["interface", "API", "integração", "externo"]
    }

    unidades_encontradas = []

    for unidade, palavras in keywords.items():
        if any(palavra in codigo for palavra in palavras):
            unidades_encontradas.append(unidade)

    return unidades_encontradas if unidades_encontradas else ["pedro"]

def main():
    print("Análise de Complexidade de Tarefa")
    
    codigo = """\
@app.route('/api/join_room', methods=['POST'])
def join_room_character():
    data = request.json
    room_id = data['room_id']
    player_id = data['player_id']
    username = data['username']
    character = data['character']

    if character not in available_characters:
        return jsonify({'message': 'Invalid character'}), 400

    if room_id in rooms:
        room = rooms[room_id]

        if player_id in room['players']:
            room['players'][player_id]['username'] = username  
            room['last_activity'] = time.time()
            return jsonify({'message': 'Rejoining...', 'token': player_id})

        if len(room['players']) < 8:
            if room['started']:
                return jsonify({'message': 'Cannot join room, game already started'}), 400

            if any(player.get('character') == character for player in room['players'].values()):
                return jsonify({'message': 'Character already taken'}), 400

            if not player_id:
                player_id = generate_token()
            rooms[room_id]['players'][player_id] = {'username': username, 'character': character}
            rooms[room_id]['last_activity'] = time.time()
            return jsonify({'message': 'Player added', 'token': player_id})
        else:
            return jsonify({'message': 'Room is full'}), 400
    else:
        return jsonify({'message': 'Room does not exist'}), 404
""" 

    # Calculando a complexidade
    nivel_complexidade = calcular_complexidade(codigo)
    print(f"Nível de complexidade: {nivel_complexidade} (1 - Muito simples, 5 - Muito complexo)")

    # Verificando unidade de função
    unidades_funcao = verificar_unidade_funcao(codigo)
    print(f"As unidades de função identificadas são: {', '.join(unidades_funcao)}")

# Executando a função principal
if __name__ == "__main__":
    main()
