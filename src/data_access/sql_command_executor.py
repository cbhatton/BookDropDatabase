"""
File: sql_command_executor.py
Author: Josh Weese

This file contains a class that serves as the data access layer for a MS SQL database.
You will need to have the odbc driver for SQL server installed, which can be found here https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

"""
import pyodbc


class SqlCommandExecutor:
    """
    This is a general purpose class designed to interface directly with a MS SQL Server database.
    """

    def __init__(self, driver: str = "{SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        """
        Constructor to initialize information to connect/work with the database.
        Args:
            driver: The driver pyodbc needs to use to connect to the database server. The defualt value here should
                    work for most cases, but you could also use {ODBC Driver 17 for SQL Server} or whichever version
                    you are using.
            server: The server to connect to.
            database: The database on the server to use.
            trusted: Whether or not this is a trusted connection.
        """
        params = []
        if driver != "":
            params.append(f"Driver={driver}")
        if server != "":
            params.append(f"Server={server}")
        if database != "":
            params.append(f"Database={database}")
        if trusted:
            params.append("TrustedConnection=yes")
        self._connection_string = ";".join(params)

    @staticmethod
    def stringify_inp_params(params: list):
        return ", ".join([f"@{val} = ?" for val in params])

    @staticmethod
    def stringify_out_params(params: dict):
        sp_out = ", ".join([f"@{val} = @{params['sp_local'][i]} OUTPUT" for i, val in enumerate(params["sp_out"])])
        sp_local = ", ".join([f"@{val} {params['sp_local_types'][i]}" for i, val in enumerate(params["sp_local"])])
        sp_select = ", ".join([f"@{val} AS {val}_var" for val in params["sp_local"]])
        return sp_out, sp_local, sp_select

    def execute_stored_procedure(self, procedure_name: str,
                                 input_param_names: list = None,
                                 input_param_values: list = None,
                                 output_param: dict = None):
        connection = pyodbc.connect(self._connection_string, autocommit=False)
        cursor = connection.cursor()
        if input_param_names is None and output_param is None:
            sql = f"""
                    EXEC {procedure_name};
                """
            cursor.execute(sql)
        elif input_param_names is not None and output_param is None:
            sql = f"""
                    EXEC {procedure_name} {self.stringify_inp_params(input_param_names)};
                """
            cursor.execute(sql, input_param_values)
        elif input_param_names is None and output_param is not None:
            sp_out, sp_local, sp_select = self.stringify_out_params(output_param)
            sql = f"""
                    DECLARE {sp_local};
                    EXEC {procedure_name} {sp_out};
                    SELECT {sp_select};            
                """
            cursor.execute(sql)
        else:
            sp_out, sp_local, sp_select = self.stringify_out_params(output_param)
            sql = f"""
                    DECLARE {sp_local};
                    EXEC {procedure_name} {self.stringify_inp_params(input_param_names)}, {sp_out};
                    SELECT {sp_select};            
                """
            cursor.execute(sql, input_param_values)
        results = self.get_all_rows(cursor)

        connection.commit()
        connection.close()
        return results

    def execute_query(self, sql):
        connection = pyodbc.connect(self._connection_string, autocommit=False)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_rows(cursor: pyodbc.Cursor):
        more_sets = True
        results = []
        while more_sets:  # NB: This always skips the first resultset
            try:
                results += cursor.fetchall()
            except pyodbc.ProgrammingError:
                pass
            more_sets = cursor.nextset()
        return results
