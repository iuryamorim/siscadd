from reportGenerator.report.src.main_faixas_criticidade import main as faixa_critica
from reportGenerator.report.src.main_integralizacoes import main as integralizacoes
from reportGenerator.report.src.main_reprovacoes import main as reprovacoes


class Report:
    def planilhas(dic, name, outputdir, ano, periodo):
        faixa_critica(dic, name, outputdir, ano, periodo)
        integralizacoes(dic, name, outputdir, ano, periodo)
        reprovacoes(dic, name, outputdir, ano, periodo)