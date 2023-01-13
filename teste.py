from . import countRotas

def test_chega_inicio_fim():
    assert countRotas.solution_1([2,3,6,8,4],1,3,5) == 4

def test_segundo_caso_leetcode():
    assert countRotas.solution_1([4,3,1],1,0,6) == 5

def test_nenhuma_rota_e_possivel():
    assert countRotas.solution_1([5,2,1],0,2,3) == 0
