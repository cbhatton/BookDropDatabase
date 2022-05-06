CREATE OR ALTER PROCEDURE BookDrop.CreatePerson
   @Name NVARCHAR(32),
   @UserName NVARCHAR(32),
   @PersonID INT OUTPUT
AS

INSERT BookDrop.Person([Name], UserName)
VALUES(@Name, @UserName);

SET @PersonID = SCOPE_IDENTITY();
GO
