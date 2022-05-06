IF OBJECT_ID(N'BookDrop.Author') IS NULL
BEGIN
   CREATE TABLE BookDrop.Author
   (
      AuthorID INT NOT NULL IDENTITY(1, 1),
      Name NVARCHAR(32) NOT NULL,

      UNIQUE(Name),

      CONSTRAINT [PK_Person_Author_AuthorID] PRIMARY KEY CLUSTERED
      (
         AuthorID ASC
      )
   );
END;
