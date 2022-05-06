CREATE OR ALTER PROCEDURE BookDrop.CreateAuthor
   @Name NVARCHAR(32)
AS

INSERT BookDrop.Author([Name])
VALUES(@Name);

GO
