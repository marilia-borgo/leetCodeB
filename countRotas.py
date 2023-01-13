# https://leetcode.com/problems/count-all-possible-routes/


def rotas_possiveis(caminho,start,finish,fuel):
    partida = caminho[start]
    destino = caminho[finish]
    rotas_possiveis=0
    if abs(partida-destino) < fuel:
        rotas_possiveis+=1
    meio=caminho[caminho.index(partida):caminho.index(destino)+1]
    for element in meio:
        if not element is 0 and meio[-1]:
            gas=abs(meio[0] - meio[element])
            if gas > fuel:
                rotas_possíveis+=1
    return rotas_possiveis


