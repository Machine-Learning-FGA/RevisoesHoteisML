import os


class Parser:

    WEEKDAY = 17
    MONTH = 16

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
        lines = self._read_lines_()
        next(lines)
        for line in lines:
            columns = self._separate_coluns_(line)
            data_array = self._process_data_(columns)
            data.append(data_array)

        return data

    def _process_data_(self, columns):
        """Transform brute data into a useful data"""
        if self.number_columns == len(columns):
            self._convert_yesno_(columns)
            self._convert_weekday_(columns)
            self._convert_month_(columns)
            self._split_period_(columns)
            self._switch_categories_(columns)
        else:
            raise Exception()

        return columns

    def _convert_yesno_(self, columns):
        """Simple parser to
        YES - 1
        NO - 0
        """
        for i, field in enumerate(columns):
            if field == 'SIM':
                columns[i] = 1
            elif field == 'NÃO' or field == 'NAO':
                columns[i] = 0
        return columns

    def _convert_weekday_(self, columns):
        columns[self.WEEKDAY] = DateConvert.weekday_to_int(columns[self.WEEKDAY])
        return columns

    def _convert_month_(self, columns):
        columns[self.MONTH] = DateConvert.month_to_int(columns[self.MONTH])
        return columns

    def _split_period_(self, columns):
        # TODO: split periods from ShortMont-ShortMont to
        # two columns with number of each month 1,0
        pass

    def _switch_categories_(self, columns):
        # TODO: convert the Negócios, Casais... categories into thruth table
        # or numbers
        pass

    def _separate_coluns_(self, line):
        return line.split(';')


class DateConvert:

    @classmethod
    def shortmonth_to_int(cls, month):
        month=month.lower()
        return ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set',
                'out', 'nov', 'dez'].index(month)

    @classmethod
    def month_to_int(cls, month):
        month=month.lower()
        return ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro',
                'dezembro'].index(month)

    @classmethod
    def weekday_to_int(cls, weekday):
        weekday=weekday.lower()
        return ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira',
                'quinta-feira', 'sexta-feira', 'sábado'].index(weekday)


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
