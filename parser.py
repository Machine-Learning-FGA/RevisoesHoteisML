import os
from sklearn.preprocessing import MultiLabelBinarizer


class Parser:

    WEEKDAY = 17
    MONTH = 16
    PERIOD = 4
    CATEGORIES = ['Casais', 'Família', 'Amigos', 'Negócios', 'Sozinho']

    def __init__(self, path, separator=','):

        self._multi_label = MultiLabelBinarizer()
        self._multi_label.fit([set([x]) for x in self.CATEGORIES])
        if os.path.exists(path):
            self.path = path
            self.header = next(self._read_lines_()).split(',')
            self._number_columns = len(self.header)
            self.separator = separator

        else:
            raise OSError('file not found')

    def _read_lines_(self):
        """ Read each line from file and return when
        called by a iterator
        """
        with open(self.path, 'r') as data_file:
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

    def get_multi_label(self):
        return self._multi_label

    def _process_data_(self, columns):
        """Transform brute data into a useful data"""
        if self._number_columns == len(columns):
            self._convert_yesno_(columns)
            self._convert_weekday_(columns)
            self._convert_month_(columns)
            self._split_period_(columns)
            self._switch_categories_(columns)
            self._transform_in_int_(columns)
        else:
            print(self.number_columns, len(columns))
            # raise Exception()

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
        """Tranform a columns in format ShortMonth - ShortMonth into
        int month, int month
        """
        periods = columns[4].split('-')
        columns[4] = DateConvert.shortmonth_to_int(periods[0])
        columns.insert(4, DateConvert.shortmonth_to_int(periods[1]))
        return columns

    def _switch_categories_(self, columns):
        """Switch the categories from CATEGORIES constant to a Binary array
        in format [ 0, 0, 0, 0, 0 ]
        """
        idx = -1
        for category in self.CATEGORIES:
        return line.split(',')
            if category in columns:
                idx = columns.index(category)
                break

        binary = self._multi_label.transform([{columns[idx]}]).flatten()
        columns.pop(idx)
        for i, value in enumerate(binary):
            columns.insert(idx + i, value)

        return columns

    def _separate_coluns_(self, line):
        """Separate a line with any separator and remove the \\n from end
        of line
        The default separator is ','
        """

        return line.replace('\n', '').split(self.separator)

    def _transform_in_int_(self, columns):
        for i, field in enumerate(columns):
            if isinstance(field, str) and field.isdigit():
                columns[i] = int(field)
        return columns


class DateConvert:

    @classmethod
    def shortmonth_to_int(cls, month):
        month = month.lower()
        return ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set',
                'out', 'nov', 'dez'].index(month)

    @classmethod
    def month_to_int(cls, month):
        month = month.lower()
        return ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro',
                'dezembro'].index(month)

    @classmethod
    def weekday_to_int(cls, weekday):
        weekday = weekday.lower()
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


if __name__ == '__main__':
    print(Parser('AM_RevisoesHoteisCaldas.csv').get_data())

# with open('AM_RevisoesHoteisCaldas.csv', 'r') as f:
#     reader = f.readline()
#     campos_tabela = reader.split(',')
#     reader = f.readline()
#     lista_registros = []
#     colunas = len(campos_tabela)
#     for reader in f:
#         registro = reader.split(',')
#         if(len(registro) == colunas):
#             lista_registros.append(registro)


# import pandas as pd
# def le_arquivo():
#     dataset = pd.read_csv('AM_RevisoesHoteisCaldas.csv')
#     x = dataset.iloc[:, :-1].values
#     y = dataset.iloc[:, -1].values
#
#     print(x)
