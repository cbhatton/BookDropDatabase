IF OBJECT_ID(N'BookDrop.BookName') IS NULL
BEGIN
   CREATE TABLE BookDrop.BookName
   (
      BookNameId INT NOT NULL IDENTITY(1, 1),
      Name NVARCHAR(32) NOT NULL,

      UNIQUE(Name),

      CONSTRAINT [PK_Person_BookName_BookNameID] PRIMARY KEY CLUSTERED
      (
         BookNameID ASC
      )
   );
END;
