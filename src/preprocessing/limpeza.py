def limpar_vagas(vagas_raw):
    vagas_limpa = []
    for vaga in vagas_raw:
        vaga["titulo"] = vaga["titulo"].strip()
        vaga["empresa"] = vaga["empresa"].strip()
        vaga["localizacao"] = vaga["localizacao"].strip()
        vagas_limpa.append(vaga)
    return vagas_limpa
