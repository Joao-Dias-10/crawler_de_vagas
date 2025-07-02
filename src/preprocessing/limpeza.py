import pandas as pd
from typing import List, Dict

class VagaLimpeza:
    def __init__(self, vagas_raw: List[Dict[str, str]]):

        self.df = pd.DataFrame(vagas_raw)

    def limpar_vagas(self) -> List[Dict[str, str]]:

        self.df["titulo"] = self.df["titulo"].str.strip()
        self.df["empresa"] = self.df["empresa"].str.strip()
        self.df["localizacao"] = self.df["localizacao"].str.strip()

        return self.df.to_dict(orient='records')
