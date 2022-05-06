CREATE OR ALTER PROCEDURE BookDrop.RetrievePersons
AS

SELECT P.PersonId, P.Name
FROM BookDrop.Person P;
GO
