def periodo_dia(hora_id):
    if 0 <= hora_id and hora_id <= 5:
        return "madrugada"
    elif 6 <= hora_id and hora_id <= 11:
        return "manhã"
    elif 12 <= hora_id and hora_id <= 17:
        return "tarde"
    elif 18 <= hora_id and hora_id <= 23:
        return "noite"
    else:
        raise ValueError(f"Impossível essa hora utilizada: {hora_id}")


def linhas_dim_hora():
    lista = []
    for hora_id in range(24):
        dic = {}
        dic["hora_id"] = hora_id # hora_id: 0 a 24
        dic["periodo_dia"] = periodo_dia(hora_id) # periodo_dia: manhã, tarde, noite, madrugada
        # { hora_id: 0, periodo_dia: madrugada } 

        lista.append(dic)
    
    return lista