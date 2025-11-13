# app.py
# Um toolkit de matemática com várias funcionalidades.
# Código original de Kauan e Pedro, refatorado e expandido por Kauan (e ChatGPT 😄).

import math
import random

# ==============================================================================
# 1. FUNÇÕES DO CONVERSOR NUMÉRICO
# ==============================================================================

def converter_real_para_inteiro():
    """
    Inicia um programa interativo para converter números reais para inteiros.
    Permite até 10 conversões por sessão.
    """
    print("\n--- Conversor de Número Real para Inteiro ---")
    print("Você tem 10 tentativas. Digite 'sair' para voltar ao menu.")

    metodos = {
        "1": ("math.trunc", math.trunc),
        "2": ("int", int),
        "3": ("round", round)
    }

    contagem = 0
    while contagem < 10:
        valor_str = input(f"\n[Tentativa {contagem + 1}/10] Digite um número real: ")

        if valor_str.lower() == 'sair':
            print("Voltando ao menu principal...")
            break

        try:
            num = float(valor_str)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido.")
            continue

        print(f"\nNúmero digitado: {num}")
        print("Escolha o método de conversão:")
        print("1. math.trunc (corta a parte decimal)")
        print("2. int (conversão padrão para inteiro)")
        print("3. round (arredondamento)")
        print("4. Mostrar todos")

        escolha = input(">> Método: ")

        if escolha == "4":
            print(f"Número inteiro (math.trunc): {math.trunc(num)}")
            print(f"Número inteiro (int):        {int(num)}")
            print(f"Arredondado (round):         {round(num)}")
        elif escolha in metodos:
            nome, func = metodos[escolha]
            print(f"Resultado com {nome}: {func(num)}")
        else:
            print("Opção de método inválida. Mostrando todos por padrão:")
            print(f"Número inteiro (math.trunc): {math.trunc(num)}")
            print(f"Número inteiro (int):        {int(num)}")
            print(f"Arredondado (round):         {round(num)}")

        contagem += 1

# ==============================================================================
# 2. FUNÇÕES DE MÉDIA PONDERADA E ESTATÍSTICA
# ==============================================================================

def calcular_media_ponderada(valores, pesos):
    """
    Calcula a média ponderada de uma lista de valores com seus respectivos pesos.
    
    Args:
        valores (list[float]): Uma lista de números (ex: notas).
        pesos (list[float]): Uma lista de pesos correspondentes a cada valor.
        
    Returns:
        float: O valor da média ponderada.
        
    Raises:
        ValueError: Se as listas de valores e pesos não tiverem o mesmo tamanho
                    ou se a soma dos pesos for zero.
    """
    if len(valores) != len(pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")

    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    numerador = sum(valor * peso for valor, peso in zip(valores, pesos))
    return numerador / soma_pesos

def exemplo_media_ponderada():
    """Demonstra o cálculo da média ponderada com um exemplo de notas."""
    print("\n--- Exemplo: Média Ponderada de Notas ---")
    notas = [8.0, 7.5, 9.5]
    pesos_notas = [2, 3, 5]
    
    try:
        media_final = calcular_media_ponderada(notas, pesos_notas)
        print(f"Notas: {notas}")
        print(f"Pesos: {pesos_notas}")
        print(f"A média ponderada final é: {media_final:.2f}")
    except ValueError as e:
        print(f"Erro no cálculo: {e}")

def menu_media_ponderada_interativa():
    """Permite ao usuário digitar valores e pesos para calcular uma média ponderada."""
    print("\n--- Calculadora de Média Ponderada ---")
    print("Digite os valores separados por espaço (ex: 7 8.5 10):")
    valores_str = input(">> ")
    print("Digite os pesos correspondentes, também separados por espaço:")
    pesos_str = input(">> ")

    try:
        valores = [float(x) for x in valores_str.split()]
        pesos = [float(x) for x in pesos_str.split()]
        media = calcular_media_ponderada(valores, pesos)
        print(f"\nValores: {valores}")
        print(f"Pesos:   {pesos}")
        print(f"Média ponderada: {media:.2f}")
    except ValueError as e:
        print(f"Erro no cálculo: {e}")

def estatisticas_basicas(valores):
    """
    Calcula estatísticas básicas de uma lista de valores.
    
    Returns:
        dict: média, mediana, mínimo, máximo, desvio padrão populacional.
    """
    if not valores:
        raise ValueError("A lista de valores não pode ser vazia.")

    n = len(valores)
    ordenados = sorted(valores)
    media = sum(valores) / n

    if n % 2 == 1:
        mediana = ordenados[n // 2]
    else:
        mediana = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2

    minimo = ordenados[0]
    maximo = ordenados[-1]
    variancia = sum((x - media) ** 2 for x in valores) / n
    desvio_padrao = math.sqrt(variancia)

    return {
        "media": media,
        "mediana": mediana,
        "minimo": minimo,
        "maximo": maximo,
        "desvio_padrao": desvio_padrao,
    }

def menu_estatistica_basica():
    """Interação para o usuário digitar uma lista de números e ver estatísticas básicas."""
    print("\n--- Estatísticas Básicas ---")
    print("Digite uma lista de números separados por espaço:")
    entrada = input(">> ")

    try:
        valores = [float(x) for x in entrada.split()]
        stats = estatisticas_basicas(valores)
        print("\nResultados:")
        print(f"Média:           {stats['media']:.4f}")
        print(f"Mediana:         {stats['mediana']:.4f}")
        print(f"Mínimo:          {stats['minimo']:.4f}")
        print(f"Máximo:          {stats['maximo']:.4f}")
        print(f"Desvio padrão:   {stats['desvio_padrao']:.4f}")
    except ValueError as e:
        print(f"Erro: {e}")

# ==============================================================================
# 3. FUNÇÕES DE PROBABILIDADE
# ==============================================================================

def calcular_probabilidade_simples(favoraveis, total):
    """Calcula a probabilidade de um evento simples."""
    if total == 0:
        raise ValueError("O número total de resultados não pode ser zero.")
    return favoraveis / total

def exemplo_probabilidade_simples():
    """Demonstra o cálculo da probabilidade de tirar um número par em um dado."""
    print("\n--- Exemplo: Probabilidade de Tirar um Número Par em um Dado ---")
    total_resultados = 6
    resultados_favoraveis = 3
    
    probabilidade = calcular_probabilidade_simples(resultados_favoraveis, total_resultados)
    
    print(f"A probabilidade é de {probabilidade:.2f} ou {probabilidade:.2%}")

def exemplo_probabilidade_combinatoria():
    """Demonstra o cálculo de probabilidade usando combinatória (cartas de baralho)."""
    print("\n--- Exemplo: Probabilidade de Tirar 2 Reis de um Baralho ---")
    
    total_combinacoes = math.comb(52, 2)       # Total de maneiras de pegar 2 cartas de 52
    combinacoes_favoraveis = math.comb(4, 2)   # Total de maneiras de pegar 2 Reis de 4
    
    probabilidade = combinacoes_favoraveis / total_combinacoes
    
    print(f"Total de combinações de 2 cartas: {total_combinacoes}")
    print(f"Combinações favoráveis (2 Reis): {combinacoes_favoraveis}")
    print(f"A probabilidade é de {probabilidade:.4f} ou {probabilidade:.4%}")

def simular_soma_dados(numero_de_simulacoes=100_000):
    """Estima a probabilidade da soma de dois dados ser 7 através da simulação."""
    sucessos = 0
    for _ in range(numero_de_simulacoes):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        if dado1 + dado2 == 7:
            sucessos += 1
    return sucessos / numero_de_simulacoes

def exemplo_probabilidade_simulacao():
    """Demonstra a estimativa de probabilidade por simulação (soma de dados)."""
    print("\n--- Exemplo: Simulação da Soma de Dois Dados ser 7 ---")
    num_simulacoes = 200_000  # um pouco mais leve que 1 milhão
    probabilidade_estimada = simular_soma_dados(num_simulacoes)
    
    print(f"Após {num_simulacoes:,} simulações...")
    print(f"A probabilidade estimada é de {probabilidade_estimada:.4f} ou aproximadamente {probabilidade_estimada:.2%}")

def menu_probabilidade_customizada():
    """Usuário escolhe casos favoráveis e total para calcular probabilidade simples."""
    print("\n--- Calculadora de Probabilidade Simples ---")
    try:
        favoraveis = int(input("Número de casos favoráveis: "))
        total = int(input("Número total de casos possíveis: "))
        prob = calcular_probabilidade_simples(favoraveis, total)
        print(f"\nProbabilidade: {prob:.4f} ou {prob:.2%}")
    except ValueError as e:
        print(f"Erro: {e}")

# ==============================================================================
# 4. FUNÇÕES DE COMBINATÓRIA
# ==============================================================================

def fatorial(n):
    """Calcula o fatorial de n com validação básica."""
    if n < 0:
        raise ValueError("n deve ser não negativo.")
    return math.factorial(n)

def permutacao(n, k):
    """Calcula P(n, k) = n! / (n-k)!"""
    if k < 0 or n < 0 or k > n:
        raise ValueError("É necessário que 0 <= k <= n e n >= 0.")
    return math.factorial(n) // math.factorial(n - k)

def combinacao(n, k):
    """Calcula C(n, k) usando math.comb."""
    if k < 0 or n < 0 or k > n:
        raise ValueError("É necessário que 0 <= k <= n e n >= 0.")
    return math.comb(n, k)

def menu_combinatoria():
    """Interação para o usuário calcular fatorial, permutação e combinação."""
    print("\n--- Combinatória: fatorial, permutação e combinação ---")
    print("1. Calcular fatorial (n!)")
    print("2. Calcular permutação P(n, k)")
    print("3. Calcular combinação C(n, k)")
    escolha = input(">> Escolha uma opção: ")

    try:
        if escolha == "1":
            n = int(input("Digite n (inteiro não negativo): "))
            print(f"{n}! = {fatorial(n)}")
        elif escolha == "2":
            n = int(input("Digite n (inteiro não negativo): "))
            k = int(input("Digite k (inteiro, 0 <= k <= n): "))
            print(f"P({n}, {k}) = {permutacao(n, k)}")
        elif escolha == "3":
            n = int(input("Digite n (inteiro não negativo): "))
            k = int(input("Digite k (inteiro, 0 <= k <= n): "))
            print(f"C({n}, {k}) = {combinacao(n, k)}")
        else:
            print("Opção inválida.")
    except ValueError as e:
        print(f"Erro: {e}")

# ==============================================================================
# 5. MENU PRINCIPAL E EXECUÇÃO
# ==============================================================================

def mostrar_menu():
    print("\n===== TOOLKIT DE MATEMÁTICA =====")
    print("1. Conversor de Número Real para Inteiro")
    print("2. Exemplo: Média Ponderada (fixa)")
    print("3. Média Ponderada (interativa)")
    print("4. Estatísticas Básicas (lista de números)")
    print("5. Exemplo: Probabilidade Simples (Dado)")
    print("6. Exemplo: Probabilidade com Combinatória (Cartas)")
    print("7. Probabilidade Simples (interativa)")
    print("8. Probabilidade por Simulação (Soma de Dados = 7)")
    print("9. Combinatória (fatorial, P(n, k), C(n, k))")
    print("0. Sair do Programa")

def main():
    """Função principal que exibe o menu e gerencia o programa."""
    opcoes = {
        "1": converter_real_para_inteiro,
        "2": exemplo_media_ponderada,
        "3": menu_media_ponderada_interativa,
        "4": menu_estatistica_basica,
        "5": exemplo_probabilidade_simples,
        "6": exemplo_probabilidade_combinatoria,
        "7": menu_probabilidade_customizada,
        "8": exemplo_probabilidade_simulacao,
        "9": menu_combinatoria,
    }

    while True:
        mostrar_menu()
        escolha = input(">> Escolha uma opção: ")

        if escolha == '0':
            print("Encerrando o programa. Até logo!")
            break

        funcao_escolhida = opcoes.get(escolha)
        if funcao_escolhida:
            funcao_escolhida()
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()