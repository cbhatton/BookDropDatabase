CREATE OR ALTER PROCEDURE BookDrop.CreateBookCopy
    @BookName NVARCHAR(32),
    @AuthorName NVARCHAR(32),
    @BookID INT OUTPUT
AS

DECLARE @NameID INT = (
                       SELECT B.BookNameID
                       FROM BookDrop.BookName B
                       WHERE B.Name = @BookName
                      )

DECLARE @AuthorID INT = (
                       SELECT A.AuthorID
                       FROM BookDrop.Author A
                       WHERE A.Name = @AuthorName
                       )

INSERT BookDrop.BookCopy(AuthorID, NameID)
VALUES(@AuthorID, @NameID);


SET @BookID = SCOPE_IDENTITY();
GO
