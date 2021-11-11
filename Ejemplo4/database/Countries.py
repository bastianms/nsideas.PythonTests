from common.MySQLDataBase import MySQLDataBase
from decouple import config

class Countries:
    def __init__(self) -> None:
        self.__connMySQL = MySQLDataBase(
            config('SERVIDOR_BD'), 
            config('USERNAME_BD'), 
            config('PASSWORD_BD'), 
            config('NOMBRE_BD')
            )
    
    def create(self, country_id: str, country_name: str, region_id: str):
        self.__connMySQL.Open()
        self.__connMySQL.excuteQuery(f"INSERT INTO countries (country_id, country_name, region_id) VALUES ('{country_id}', '{country_name}', '{region_id}')")
        self.__connMySQL.Close()
    
    def find(self, filter: str):
        self.__connMySQL.Open()
        result = self.__connMySQL.fetchAll(f"SELECT country_id, country_name, region_id FROM countries WHERE {filter}")
        self.__connMySQL.Close()
        return result
    
    def findOne(self, country_id: str):
        self.__connMySQL.Open()
        result = self.__connMySQL.fetchOne(f"SELECT country_id, country_name, region_id FROM countries WHERE country_id = '{country_id}'")
        self.__connMySQL.Close()
        return result

    def update(self, country_id: str, country_name: str, region_id: str):
        pass

    def delete(self, country_id: str):
        pass