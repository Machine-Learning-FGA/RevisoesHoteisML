import os


class Parser:

    def __init__(self, path):

        if os.path.exists(path):
            self.path = path
            self.header = next(self._read_lines_()).split(';')
            self.number_columns = len(self.header)

        else:
            raise OSError('file not found')

    def _read_lines_(self):
        """ Read each line from file and return when
        called by a iterator
        """
        with open(self.path, 'r', encoding='latin-1') as data_file:
            while True:
                line = data_file.readline()
                if not line:
                    break
                yield line

    def get_data(self):
        """Mount a big array with all data readed from file
        and do some processament in each line"""

        data = []
        for line in self._read_lines_():
            columns = self._separate_coluns_(line)
            data_array = self._process_data_(columns)
            data.append(data_array)

        return data

    def _process_data_(self, columns):
        if self.number_columns == len(columns):
            self._convert_yesno_(columns)
            self._convert_weekday_(columns)
            self._split_period_(columns)
        else:
            raise Exception()

    def _convert_yesno_(self, columns):
        for i, field in enumerate(columns):
            if field == 'SIM':
                columns[i] = 1
            elif field == 'NÃO' or field == 'NAO':
                columns[i] = 0
        return columns

    def _convert_weekday_(self, columns):
        columns[self.WEEKDAY] = DateConvert.weekday_to_int(columns[self.WEEKDAY])
        return columns

    def _separate_coluns_(self, line):
        return line.split(';')


class DateConvert:

    @classmethod
    def shortmonth_to_int(cls, month):
        return ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set',
                'Out', 'Nov', 'Dez'].index(month)

    @classmethod
    def month_to_int(cls, month):
        return ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
                'Dezembro'].index(month)

    @classmethod
    def weekday_to_int(cls, weekday):
        return ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira',
                'Quinta-feira', 'Sexta-feira', 'Sábado'].index(weekday)


def pause():
    raw_input("Press the <ENTER> key to continue...")


def mostra_registro(registro):
    for campo in registro:
        print(campo)


def mostra_campos(lista_campos):
    for campo in lista_campos:
        print(campo)


def mostra_tabela(lista_registros):
    for registro in lista_registros:
        for campo in registro:
            print(campo)


# with open('AM_RevisoesHoteisCaldas.csv', 'r') as f:
#     reader = f.readline()
#     campos_tabela = reader.split(';')
#     reader = f.readline()
#     lista_registros = []
#     colunas = len(campos_tabela)
#     for reader in f:
#         registro = reader.split(';')
#         if(len(registro) == colunas):
#             lista_registros.append(registro)
# Ative os 4 se quiser ver um registro só #################
# i = input("Digite o numero do registro: ")
# assert(i >= 0 and "O numero tem que ser maior que 0")
# mostra_registro(lista_registros[i])
# pause()
# mostra_tabela(lista_registros)
