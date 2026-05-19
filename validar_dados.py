import pandas as pd # type: ignore

def validar_dados():
    print("Iniciando validação dos dados...")
    
    # Ler dados
    df = pd.read_csv('dados.csv')
    
    # Testes de qualidade 
    erros = []
    
    # Teste 1: Não pode ter valores negativos
    valores_negativos = df[df['valor'] < 0]
    if not valores_negativos.empty:
        erros.append(f" Valores negativos encontrados: {valores_negativos.to_dict('records')}")
    
    # Teste 2: IDs devem ser únicos
    if df['id'].duplicated().any():
        erros.append(f" IDs duplicados encontrados")
    
    # Teste 3: Nome não pode ser vazio
    if df['nome'].isna().any():
        erros.append(f" Nomes vazios encontrados")
    
    # Teste 4: Valor total deve ser positivo
    if df['valor'].sum() < 0:
        erros.append(f" Soma total negativa: {df['valor'].sum()}")
    
    # Resultado
    if erros:
        print("\n".join(erros))
        print("\n PIPELINE FALHOU - Dados com problemas!")
        return False
    else:
        print(f" Todos os testes foram validados.")
        print(f" Total de registros: {len(df)}")
        print(f" Soma total: R$ {df['valor'].sum()}")
        print(f" Média: R$ {df['valor'].mean():.2f}")
        print("\n PIPELINE SUCESSO - Dados prontos para uso!")
        return True

# Se o script retornar True (Sucesso), ele encerra o programa com o código 0.
# Se retornar False (Falha), ele encerra com o código 1.
if __name__ == "__main__":
    exit(0 if validar_dados() else 1)