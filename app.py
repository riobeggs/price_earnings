from assets.table_data import TableData


def main() -> None:
    td = TableData()
    td.table = td.locate_table()
    # td.headings = td.get_column_names()
    print(td.table)
    # print(td.headings)
    td.close_driver()



    # # print(td.table)
    # td.table = td.locate_table()
    # print(td.table)
    # # headings = TableData().column_names()
    # # print(headings)

if __name__ == "__main__":
    main()