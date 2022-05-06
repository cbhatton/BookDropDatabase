CREATE OR ALTER PROCEDURE BookDrop.CreateReview
   @BookID INT,
   @PersonID INT,
   @StarRating INT,
   @Location INT,
   @ReviewID INT OUTPUT
AS

INSERT BookDrop.Review(BookID, PersonID, StarRating, Location)
VALUES(@BookID, @PersonID, @StarRating, @Location);

SET @ReviewID = SCOPE_IDENTITY();
GO
