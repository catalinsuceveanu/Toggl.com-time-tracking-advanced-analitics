import random
import xlsxwriter

def main():
    # tree id
    # of apples
    # profit of tree
    # age of tree
    # type of tree

    workbook = xlsxwriter.Workbook("apples.xlsx")
    worksheet = workbook.add_worksheet('apples')

    worksheet.write('A1','Tree ID')
    worksheet.write('B1','Number of Apples')
    worksheet.write('C1','Tree Height')
    worksheet.write('D1','Tree Profit')
    worksheet.write('E1','Tree Type')

    row_index=2


    for row in range (200):
        tree_id = row +1000
        num_apples = 20 + random.randint(50,100)
        type_of_tree = random.choice(['Macintosh', 'Red Delicious','Granny Smith', 'Fuji'])
        tree_profit = random.random() * 1000
        height_of_tree = 100 + random.randint(25,50)

        worksheet.write('A' + str(row_index), tree_id)
        worksheet.write('B' + str(row_index), num_apples)
        worksheet.write('C' + str(row_index), type_of_tree)
        worksheet.write('D' + str(row_index), tree_profit)
        worksheet.write('E' + str(row_index), height_of_tree)

        row_index+=1

    workbook.close()

#if __name__ == "__main__":
main()