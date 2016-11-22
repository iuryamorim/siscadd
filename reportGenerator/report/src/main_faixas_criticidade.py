###############################################################################
# _*_ coding: utf-8

from reportGenerator.report.src.analisador_desempenho_academico import AnalisadorDesempenhoAcademico
from reportGenerator.report.src.parametros import Parametros

import sys, getopt
import glob, os
from os.path import basename
from reportGenerator.report.src.parametros import Criticidade
from reportGenerator.report.src.periodo_letivo import PeriodoLetivo

def construir_lista_candidatos_jubilacao(planilha):
    
    return AnalisadorDesempenhoAcademico.construir_mapa_alunos(planilha)
#     mapa_alunos = AnalisadorDesempenhoAcademico.construir_mapa_alunos(planilha)
# 
#     outro_mapa_alunos = {}
#     
#     for (matr_aluno, aluno) in mapa_alunos.iteritems():
#         if not aluno.esta_regular():
#             outro_mapa_alunos[matr_aluno] = aluno
# 
#     return outro_mapa_alunos

import xlsxwriter

def main(dic, name, outputdir, ano, periodo):
    inputdir = ''
    
    '''try:
        opts, args = getopt.getopt(argv, "hp:i:o:", ["idir=", "odir="])
    except getopt.GetoptError:
        print 'main.py -i <inputdir> -o <outputdir>'
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print 'main.py -i <inputdir> -o <outputdir>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputdir = arg
        elif opt == "-p":
            componentes = arg.split('.')
            if len(componentes) == 2:
                Parametros.ANO_BASE = int(componentes[0])
                Parametros.PERIODO_BASE = int(componentes[1])
                print PeriodoLetivo.fromstring(arg)
            else:
                sys.exit()
    
    print 'Input dir: ', inputdir
    print 'Output dir:', outputdir
    
    os.chdir(inputdir)'''

    Parametros.ANO_BASE = ano
    Parametros.PERIODO_BASE = periodo

    #for planilha in glob.glob("*.csv"):
    filename = name + '-faixas-criticidade.xlsx'
    filename = outputdir + '/' + basename(filename)

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    format_blue = workbook.add_format()
    format_blue.set_font_color('blue')
    format_blue.set_align('center')

    format_orange = workbook.add_format()
    format_orange.set_font_color('orange')
    format_orange.set_align('center')

    format_red = workbook.add_format()
    format_red.set_font_color('red')
    format_red.set_align('center')

    format_black = workbook.add_format({'bold': True})
    format_black.set_align('center')

    # Write some data headers.
    worksheet.write('A1', 'MATR_ALUNO', bold)
    worksheet.write('B1', 'NOME_ALUNO', bold)
    worksheet.write('C1', 'CPF_ALUNO', bold)
    worksheet.write('D1', 'QTD_MAX_REPROVACOES', bold)
    worksheet.write('E1', 'QTD_PERIODOS_CURSADOS', bold)
    worksheet.write('F1', 'CRITICIDADE', bold)

    # Start from the first cell below the headers.
    row = 1
    col = 0

    width_coluna_nome = 0
    width_coluna_cpf = 0

    alunos = construir_lista_candidatos_jubilacao(dic)
    for (matr_aluno, aluno) in alunos.items():
        worksheet.write_string(row, col, matr_aluno)

        worksheet.write(row, col + 1, aluno.nome)
        width_coluna_nome = max(width_coluna_nome, len(aluno.nome))

        worksheet.write(row, col + 2, aluno.cpf)
        width_coluna_cpf = max(width_coluna_cpf, len(aluno.cpf))

        worksheet.write(row, col + 3, aluno.qtd_maxima_reprovacoes)

        worksheet.write(row, col + 4, aluno.qtd_periodos_cursados)

        criticidade = Criticidade.descritor(aluno.faixa_criticidade())
        if criticidade == "AZUL":
            worksheet.write(row, col + 5, criticidade, format_blue)
        elif criticidade == "LARANJA":
            worksheet.write(row, col + 5, criticidade, format_orange)
        elif criticidade == "VERMELHA":
            worksheet.write(row, col + 5, criticidade, format_red)
        elif criticidade == "PRETA":
            worksheet.write(row, col + 5, criticidade, format_black)

        row += 1

    width_coluna_matricula = 14
    width_coluna_qtd_maxima_reprovacoes = 24
    width_coluna_qtd_periodos_cursados = 25
    width_coluna_faixa_criticidade = 10

    worksheet.set_column(col, col, width_coluna_matricula)
    worksheet.set_column(col + 1, col + 1, width_coluna_nome)
    worksheet.set_column(col + 2, col + 2, width_coluna_cpf)
    worksheet.set_column(col + 3, col + 3, width_coluna_qtd_maxima_reprovacoes)
    worksheet.set_column(col + 4, col + 4, width_coluna_qtd_periodos_cursados)
    worksheet.set_column(col + 5, col + 5, width_coluna_faixa_criticidade)

    workbook.close()

if __name__ == "__main__":
    main(sys.argv[1:])
