CREATE OR ALTER PROCEDURE BookDrop.FetchPerson
   @UserName NVARCHAR(32)
AS

SELECT P.PersonId
FROM BookDrop.Person P
WHERE P.UserName = @UserName;
GO
