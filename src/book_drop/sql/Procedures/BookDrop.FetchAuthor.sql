CREATE OR ALTER PROCEDURE BookDrop.FetchAuthor
   @Name NVARCHAR(32)
AS

SELECT COUNT(A.Name)
FROM BookDrop.Author A
WHERE A.Name = @Name;
GO
