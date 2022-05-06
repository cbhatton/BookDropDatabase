IF OBJECT_ID(N'BookDrop.BookCopy') IS NULL
BEGIN
   CREATE TABLE BookDrop.BookCopy
   (
      BookID INT NOT NULL IDENTITY(1, 1),
      AuthorID INT NOT NULL,
      NameID INT NOT NULL,

      CONSTRAINT [PK_BookDrop_BookCopy_BookID] PRIMARY KEY CLUSTERED
      (
         BookID ASC
      ),
   );
END;
