def limpar_vagas(vagas_raw):
    vagas_limpa = []
    for vaga in vagas_raw:
        vaga["titulo"] = vaga["titulo"].strip()
        vaga["empresa"] = vaga["empresa"].strip()
        vaga["localizacao"] = vaga["localizacao"].strip()
        vaga["salario"] = None
        vaga["data_postagem"] = None
        vaga["dias_atras_postagem"] = None
        vaga["tipo_contrato"] = None
        vagas_limpa.append(vaga)
    return vagas_limpa
