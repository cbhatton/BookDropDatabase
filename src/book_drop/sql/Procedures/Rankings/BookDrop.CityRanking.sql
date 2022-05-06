CREATE OR ALTER PROCEDURE BookDrop.CityRanking AS

SELECT R.Location, A.Name as AuthorName, (SUM(CAST(R.StarRating as float)) / COUNT(CAST(R.ReviewID as float))) as AvgScore
FROM BookDrop.BookCopy BC
    INNER JOIN BookDrop.Author A ON A.AuthorID = BC.AuthorID
    INNER JOIN BookDrop.Review R ON BC.BookID = R.BookID
GROUP BY A.Name, R.Location
ORDER BY A.Name DESC
GO
