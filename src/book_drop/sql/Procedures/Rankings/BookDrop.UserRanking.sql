CREATE OR ALTER PROCEDURE BookDrop.UserRanking AS


SELECT P.Name, COUNT(ReviewID) as BooksRead, (SUM(CAST(R.StarRating as float)) / COUNT(CAST(R.ReviewID as float))) as AvgScore
FROM BookDrop.Person P
    INNER JOIN BookDrop.Review R ON P.PersonID = R.PersonID
GROUP BY P.PersonID, P.Name
GO
