def vacina_ja(idade, profissao=''):
    profissao_com_prioridade = ['medico', 'enfermeiro', 'medica', 'enfermeira', 'auxiliar de enfermagem', 'profissionais da saude']
    if profissao in profissao_com_prioridade:
        return 'Autorizado Vacinação'
    if idade >= 69:
        return 'Autorizado Vacinação'
    if profissao == 'professor' and idade > 47:
        return 'Autorizado Vacinação'
    return 'Não autorizado por enquanto'


assert vacina_ja(29, "medico") == 'Autorizado Vacinação'
assert vacina_ja(69) == 'Autorizado Vacinação'
assert vacina_ja(48, 'professor') == 'Autorizado Vacinação'
assert vacina_ja(48) == 'Não autorizado por enquanto'
assert vacina_ja(50) == 'Não autorizado por enquanto'
