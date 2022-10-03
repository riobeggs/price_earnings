import assets.web_driver as Driver
import pandas as pd
from bs4 import BeautifulSoup

class TableData:
    def __init__(self, driver=None, table=None): 
        self.driver = Driver.run_web_driver()
        self.table = table

    def locate_table(self):
        main_page = BeautifulSoup(self.driver.page_source, "html.parser")
        find_table = main_page.find("table")
        self.table = pd.read_html(str(find_table))
        self.driver.close()