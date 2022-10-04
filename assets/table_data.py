import assets.web_driver as Driver
import pandas as pd
from bs4 import BeautifulSoup


class TableData:
    _table = None

    def __init__(self):
        self.driver = Driver.run_web_driver()
        self._table = []
        # self.headings = []

    @property
    def table(self):
        """Get our table attribute"""
        return self._table

    @table.setter
    def table(self, table: list):
        """Set our table attribute"""
        if not isinstance(table, list):
            raise ValueError("Table has not been located.")
        self._table = table

    def locate_table(self) -> list:
        main_page = BeautifulSoup(self.driver.page_source, "html.parser")
        find_table = main_page.find("table")
        self.table.append(pd.read_html(str(find_table)))
        self.driver.close()
        return self.table

    # def column_names(self) -> list:
    #     for column_name in self.table.find_all("thead"):
    #         self.headings.append(column_name)
    #     return self.column_names
