from rh.classes.Departamento import Departamento
from datetime import date, timedelta
import pytest


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento(
            'Departamento XYZ',
            'José da Silva',
            28, 3, 1990
            )
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento(
            'Departamento XYZ',
            None, 28, 3, 1990
            )
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel is None
        assert objeto.aniversario_resp, '1990-03-28'

    def test_str_repr(self):
        objeto = Departamento(
            'Departamento XYZ',
            'José da Silva',
            28, 3, 1990
            )
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'
        assert str(objeto.aniversario_resp) == '1990-03-28'

    def test_setters(self):
        objeto = Departamento(
            'Curadoria',
            'João',
            28, 3, 1990
            )
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento(
            'Departamento XYZ',
            'José da Silva',
            28, 3, 1990
            )
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento(
            'Departamento XYZ',
            None,
            28, 3, 1990
            )
        assert departamento.responsavel is None
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'

    def test_responsavel_substituido(self):
        departamento = Departamento(
            'Departamento XYZ',
            None,
            28, 3, 1990
            )
        assert departamento.responsavel is None
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'
        departamento.informar_responsavel('João Oliveira', 1, 1, 1990)
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento(
            'Departamento XYZ',
            None,
            28, 3, 1990
            )
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        retorno = [
            ('João Oliveira', hoje.strftime('1992-%m-%d'), 'Departamento XYZ'),
            ('Luis Fernando', hoje.strftime('2000-%m-%d'), 'Departamento XYZ')
        ]
        depto = Departamento(
            'Departamento XYZ',
            None,
            27, 3, 1990
            )
        depto.informar_responsavel('José da Silva', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list

    def test_class_declared_fail(self):
        msg_erro = "Informe dia, mês e ano"
        with pytest.raises(TypeError) as error:
            Departamento('John Doe')
        assert str(error.value) == msg_erro

    def test_aniversario_resp(self):
        objeto = Departamento(
            'Departamento XYZ',
            'José da Silva',
            28, 3, 1990
            )
        assert objeto.aniversario_resp == '1990-03-28' 

        
