import assets.web_driver as Driver
import pandas as pd
from bs4 import BeautifulSoup


class TableData:
    _table = None
    _headings = None
    _original_html_table = None

    def __init__(self):
        self.driver = Driver.run_web_driver()
        self._original_html_table = None
        self._table = None
        self._headings = None

    def locate_table(self) -> list:
        main_page = BeautifulSoup(self.driver.page_source, "html.parser")
        self._original_html_table = main_page.find("table")
        self._table = (pd.read_html(str(self._original_html_table)))
        return self._table

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

    # def get_column_names(self) -> list:
    #     for column_name in self._original_html_table.find_all("th"):
    #         self._headings.append(column_name)
    #     return self._headings

    # @property
    # def headings(self):
    #     """Get our table attribute"""
    #     return self._original_html_table

    # @headings.setter
    # def headings(self, headings: list):
    #     """Set our headings attribute"""
    #     if not isinstance(headings, list):
    #         raise ValueError("Headings have not been located.")
    #     self._original_html_table = headings

    def close_driver(self):
        self.driver.close()
