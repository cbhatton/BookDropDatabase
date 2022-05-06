CREATE OR ALTER PROCEDURE BookDrop.FetchBookName
   @Name NVARCHAR(32)
AS

SELECT COUNT(B.Name)
FROM BookDrop.BookName B
WHERE B.Name = @Name;
GO
