class Matrix:
    def __init__(self, matrix_string):
        self.formated_matrix_list = []
        self.formated_matrix = matrix_string.split("\n")
        self.format_matrix()

    def format_matrix(self):
        for row in self.formated_matrix:
            self.formated_matrix_list.append([int(value) for value in row.split(" ")])

    def row(self, index):
        try:
            return self.formated_matrix_list[index - 1]
        except Exception as e:
            return

    def column(self, index):
        try:
            col = []
            for x in self.formated_matrix_list:
                col.append(x[index - 1])

            return col
        except Exception as e:
            return



