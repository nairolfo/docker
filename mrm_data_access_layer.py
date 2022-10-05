import mysql.connector 
from mysql.connector import Error
from contextlib import closing
import csv

class mrm_data_access_layer():
    """ rudimentary class that contains methods to retrieve data and communicate with database  """
    
    host_name = "localhost"
    user_name = "florian"
    user_password = "*mLyreco100l*"

    def create_server_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(host=self.host_name,
                user=self.user_name,
                passwd=self.user_password)
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def execute_query_on_mrm(self, connection, query, params=()):
        with closing(connection.cursor()) as cursor:
            try:
                cursor.execute("USE MRM;")
                connection.commit()
                cursor.execute(query, params)
                connection.commit()
            except Error as err:
                print(f"Error: '{err}'")

    def reset_mrm_db(self, connection):      
        self.execute_query_on_mrm(connection, "DELETE FROM `mrm`.`match` WHERE `mrm`.`match`.`rowId` > 0")
        self.execute_query_on_mrm(connection, "DELETE FROM `mrm`.`menu` WHERE `mrm`.`menu`.`rowId` > 0")
        self.execute_query_on_mrm(connection, "DELETE FROM `mrm`.`term` WHERE `mrm`.`term`.`termId` > 0")

    def insert_term(self, connection, termId, term):
        insert_term_sql_query = "INSERT INTO `mrm`.`term` (`termId`, `term`) VALUES (%s, %s);"
        self.execute_query_on_mrm(connection, insert_term_sql_query, (termId, term))

    def get_terms(self, connection):
        termsdict = {}
        with open('terms.csv', encoding='utf-8') as terms_file:
            csv_reader = csv.reader(terms_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    termsdict.update({row[0]:row[1]})
                    self.insert_term(connection, int(row[0]), row[1])
                line_count += 1
            print(f'Processed {line_count} lines.')
            return termsdict

    def insert_menu(self, connection, rowId, menuId, productName, ProductDescription):
        insert_menu_sql_query = "INSERT INTO `mrm`.`menu` (`rowId`,`menuId`, `ProductName`, `ProductDescription`) VALUES (%s, %s, %s, %s);"
        self.execute_query_on_mrm(connection, insert_menu_sql_query, (rowId, menuId, productName, ProductDescription))

    def insert_match(self, connection, rowId, termId):
        insert_match_query = "INSERT INTO `mrm`.`match` (`rowId`, `termId`) VALUES (%s, %s);"
        self.execute_query_on_mrm(connection, insert_match_query, (rowId, termId))


