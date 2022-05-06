CREATE OR ALTER PROCEDURE BookDrop.CreateBookName
   @Name NVARCHAR(32)
AS

INSERT BookDrop.BookName([Name])
VALUES(@Name);

GO