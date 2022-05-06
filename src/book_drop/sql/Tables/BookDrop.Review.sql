IF OBJECT_ID(N'BookDrop.Review') IS NULL
BEGIN
   CREATE TABLE BookDrop.Review
   (
      ReviewID INT NOT NULL IDENTITY(1, 1),
      BookID INT NOT NULL,
      PersonID INT NOT NULL,
      StarRating INT NOT NULL,
      Location INT NOT NULL, -- In the form of an area code
      Date DATETIMEOFFSET NOT NULL DEFAULT(SYSDATETIMEOFFSET()),

      CONSTRAINT [PK_BookDrop_Review_ReviewID] PRIMARY KEY CLUSTERED
      (
         ReviewID ASC
      )
   );
END;
