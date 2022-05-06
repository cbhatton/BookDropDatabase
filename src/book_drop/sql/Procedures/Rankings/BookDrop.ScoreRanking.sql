CREATE OR ALTER PROCEDURE BookDrop.ScoreRanking AS

SELECT BN.Name as BookName, A.Name as AuthorName, (SUM(CAST(R.StarRating as float)) / COUNT(CAST(R.ReviewID as float))) as AvgScore
FROM BookDrop.BookCopy BC
    INNER JOIN BookDrop.BookName BN ON BC.NameID = BN.BookNameId
    INNER JOIN BookDrop.Author A ON BC.AuthorID = A.AuthorID
    INNER JOIN BookDrop.Review R ON BC.BookID = R.BookID

GROUP BY BC.BookID, BN.Name, A.Name
ORDER BY AvgScore DESC
GO
