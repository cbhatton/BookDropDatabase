IF NOT EXISTS
   (
      SELECT *
      FROM sys.schemas s
      WHERE s.[name] = N'BookDrop'
   )
BEGIN
   EXEC(N'CREATE SCHEMA [BookDrop] AUTHORIZATION [dbo]');
END