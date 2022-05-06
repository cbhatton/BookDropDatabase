from src.data_access.sql_command_executor import SqlCommandExecutor


class SqlRankingRepository:

    def __init__(self, driver: str = "{SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)

    def fetch_ranking(self, ranking: str):
        if ranking == 'city':
            sp_name = 'BookDrop.CityRanking'
            cols = ['Location', 'Author Name', 'Average Score']
        elif ranking == 'swap':
            sp_name = 'BookDrop.SwapRanking'
            cols = ['Book Name', 'Reviews']
        elif ranking == 'score':
            sp_name = 'BookDrop.ScoreRanking'
            cols = ['Book Name', 'Author Name', 'Average Score']
        elif ranking == 'user':
            sp_name = 'BookDrop.UserRanking'
            cols = ['Name', 'Books Read', 'Average Score']
        else:
            raise ValueError("Invalid Ranking.")

        results = self.executor.execute_stored_procedure(sp_name)

        return results, cols

if __name__ == '__main__':
    rank_repo = SqlRankingRepository(server="(local)\\SQLEXPRESS", database="cc520")
    results = rank_repo.fetch_ranking('score')
    print(results)