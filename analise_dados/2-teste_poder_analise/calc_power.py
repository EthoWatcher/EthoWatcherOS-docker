
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calc_tshn as ct
from scipy import stats

class Calc_poder():
    def __init__(self, controle, tratamento, TSHN= stats.mannwhitneyu,  qntd_animais =5, **kwargs):
        self.controle = controle
        self.tratamento = tratamento
        self.kwargs = kwargs
        
        self.lis_qnt = [qntd_animais, qntd_animais*2, qntd_animais*3, qntd_animais*4, qntd_animais*5, qntd_animais*6]
        self._create_list_powa(self.lis_qnt, TSHN)

    def get_list_qnt_powa(self):
        return self.lis_qnt, self.lis_powa 


    def _create_list_powa(self, lis_qnt, TSHN):
        self.lis_powa = []
        for qnt in lis_qnt:
            ls_reamostra_controle = _get_novas_observacoes(self.controle, qnt, 1000)
            ls_reamostra_tratamen = _get_novas_observacoes(self.tratamento, qnt, 1000)
            self.lis_powa.append(self._get_powa(ls_reamostra_controle,ls_reamostra_tratamen, TSHN))


    def _get_powa(self, ls_reamostra_controle, ls_reamostra_tratamen, TSHN):
        b=0
        qnt_dados = len(ls_reamostra_controle)
        for rea_controle, rea_tratamen in zip(ls_reamostra_controle, ls_reamostra_tratamen):
            t_1 = ct.test_hipotese_scipy(rea_controle, rea_tratamen, TSHN, **self.kwargs)
            r_rejeitou = t_1.get_p()
        #     print(r_rejeitou)
            if r_rejeitou:
                b+=1

        return b/qnt_dados * 100
    

class Calc_poder_one(Calc_poder):
    def __init__(self, controle, TSHN= stats.mannwhitneyu,  qntd_animais =5):
        super().__init__(controle, [], TSHN, qntd_animais )


    def _get_powa(self, ls_reamostra_controle, ls_reamostra_tratamen, TSHN):
        b=0
        qnt_dados = len(ls_reamostra_controle)
        for rea_controle in ls_reamostra_controle:
            t_1 = ct.test_hipotese_scipy_one(rea_controle, TSHN)
            r_rejeitou = t_1.get_p()
        #     print(r_rejeitou)
            if r_rejeitou:
                b+=1

        return b/qnt_dados * 100

    def _create_list_powa(self, lis_qnt, TSHN):
        self.lis_powa = []
        self.list_data = []
        for qnt in lis_qnt:
            ls_reamostra_controle = _get_novas_observacoes(self.controle, qnt, 1000)
            # ls_reamostra_tratamen = _get_novas_observacoes(self.tratamento, qnt, 1000)
            self.lis_powa.append(self._get_powa(ls_reamostra_controle, [], TSHN))
            self.list_data.append(ls_reamostra_controle)


def _gera_novas_observacoes(todos_dados, qnt_dados):
    saida = np.random.choice(todos_dados, qnt_dados, replace=True)
    return saida

def _get_novas_observacoes(dados_reamostrar, qnt_dados, qnt_vezes=1000):
    reamostrado_dados_reamostra= [] 
    for a in range(qnt_vezes):
        reamostrado_dados_reamostra.append(_gera_novas_observacoes(dados_reamostrar, qnt_dados))
    return reamostrado_dados_reamostra


def test_Calc_podeR_one():
    data = [ 31.46666667,  34.56666667, 119.9       ,  64.63333333,
        87.96666667,  79.46666667]
    co = Calc_poder_one(data, stats.shapiro, len(data))


    lis_qnt_k, lis_powa_k= co.get_list_qnt_powa()

    print(lis_qnt_k, lis_powa_k)


if __name__ == "__main__":
    test_Calc_podeR_one()