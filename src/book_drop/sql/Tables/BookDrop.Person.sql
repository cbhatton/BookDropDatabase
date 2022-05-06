IF OBJECT_ID(N'BookDrop.Person') IS NULL
BEGIN
   CREATE TABLE BookDrop.Person
   (
      PersonID INT NOT NULL IDENTITY(1, 1),
      Name NVARCHAR(32) NOT NULL,
      UserName NVARCHAR(32) NOT NULL,

      UNIQUE(UserName),

      CONSTRAINT [PK_Person_Person_PersonID] PRIMARY KEY CLUSTERED
      (
         PersonID ASC
      )
   );
END;
