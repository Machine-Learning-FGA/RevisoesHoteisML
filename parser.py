import os
from sklearn.preprocessing import MultiLabelBinarizer


def _flatten(array):
    res = []

    def loop(sub_array):
        for i in sub_array:
            if isinstance(i, list):
                loop(i)
            else:
                res.append(i)
    loop(array)
    return res


class Parser:

    WEEKDAY_COLUMN = 17
    MONTH_COLUMN = 16
    PERIOD_COLUMN = 4
    STAR_COLUMN = 13
    CATEGORIES = ['Casais', 'Família', 'Amigos', 'Negócios', 'Sozinho']

    SHORT_MONTHS = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul',
                    'ago', 'set', 'out', 'nov', 'dez']
    MONTHS = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
              'julho', 'agosto', 'setembro', 'outubro', 'novembro',
              'dezembro']
    WEEKDAY = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira',
               'quinta-feira', 'sexta-feira', 'sábado']

    def __init__(self, path, separator=';'):

        self._multi_label = MultiLabelBinarizer()
        self._short_month = MultiLabelBinarizer()
        self._months = MultiLabelBinarizer()
        self._weekday = MultiLabelBinarizer()

        self._multi_label.fit(self._get_categories_(self.CATEGORIES))
        self._short_month.fit(self._get_categories_(self.SHORT_MONTHS))
        self._months.fit(self._get_categories_(self.MONTHS))
        self._weekday.fit(self._get_categories_(self.WEEKDAY))

        if os.path.exists(path):
            self.path = path
            self.header = next(self._read_lines_()).split(separator)
            self._number_columns = len(self.header)
            self.separator = separator

        else:
            raise OSError('file not found')

    def _get_categories_(self, categories):
        return [set([x]) for x in categories]

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
        label = []
        lines = self._read_lines_()
        next(lines)
        for line in lines:
            columns = self._separate_coluns_(line)
            data_array, data_label = self._process_data_(columns)
            flatten_data = _flatten(data_array)
            data.append(flatten_data)
            label.append(data_label)

        return data, label

    def get_multi_label(self):
        return self._multi_label

    def _process_data_(self, columns):
        """Transform brute data into a useful data"""
        if self._number_columns == len(columns):
            self._convert_yesno_(columns)
            self._floor_star_hotel_(columns)
            self._convert_weekday_(columns)
            self._convert_month_(columns)
            self._split_period_(columns)
            self._switch_categories_(columns)
            columns = self._transform_in_int_(columns)
        else:
            print(self._number_columns, len(columns))
            # raise Exception()
        label = columns.pop()

        return columns, label

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

    def _floor_star_hotel_(self, columns):
        columns[self.STAR_COLUMN] = int(columns[self.STAR_COLUMN][0])
        return columns

    def _convert_weekday_(self, columns):
        weekday = columns[self.WEEKDAY_COLUMN].lower()
        columns[self.WEEKDAY_COLUMN] = self._transform_table_(self._weekday, weekday)
        return columns

    def _transform_table_(self, multi_label, value):
        label = multi_label.transform([{value}])
        label_list = list(label.flatten())
        return label_list

    def _convert_month_(self, columns):
        month = columns[self.MONTH_COLUMN].lower()
        columns[self.MONTH_COLUMN] = self._transform_table_(self._months, month)
        return columns

    def _split_period_(self, columns):
        """Tranform a columns in format ShortMonth - ShortMonth into
        int month, int month
        """
        periods = columns[self.PERIOD_COLUMN].split('-')
        columns[self.PERIOD_COLUMN] = self._transform_table_(self._short_month, periods[0].lower())
        columns.insert(self.PERIOD_COLUMN, self._transform_table_(self._short_month, periods[1].lower()))
        return columns

    def _switch_categories_(self, columns):
        """Switch the categories from CATEGORIES constant to a Binary array
        in format [ 0, 0, 0, 0, 0 ]
        """
        idx = -1
        for category in self.CATEGORIES:
            if category in columns:
                idx = columns.index(category)
                break

        binary = self._multi_label.transform([{columns[idx]}]).flatten()
        columns[idx] = list(binary)

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
        columns = list(filter(lambda x: not isinstance(x, str), columns))
        return columns



if __name__ == '__main__':
    print(Parser('AM_RevisoesHoteisCaldas.csv').get_data()[0][0])

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
