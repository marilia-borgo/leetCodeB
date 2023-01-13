from . import countRotas

def test_chega_inicio_fim():
    assert countRotas.rotas_possiveis([2,3,6,8,4],1,3,5) == 1

def quantidade_rotas_totais():
    assert countRotas.rotas_possiveis([2,3,6,8,4],1,3,5) == 4
