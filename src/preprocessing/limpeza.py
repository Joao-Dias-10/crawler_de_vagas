import pandas as pd

def limpar_vagas(vagas_raw):
    df = pd.DataFrame(vagas_raw)
    
    df["titulo"] = df["titulo"].str.strip()
    df["empresa"] = df["empresa"].str.strip()
    df["localizacao"] = df["localizacao"].str.strip()
    
    return df.to_dict(orient='records')
