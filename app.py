from assets.table_data import TableData


def main() -> None:
    td = TableData()
    td.table = td.locate_table()
    print(td.table)



    # # print(td.table)
    # td.table = td.locate_table()
    # print(td.table)
    # # headings = TableData().column_names()
    # # print(headings)

if __name__ == "__main__":
    main()