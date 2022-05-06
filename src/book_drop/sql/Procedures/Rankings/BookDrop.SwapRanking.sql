CREATE OR ALTER PROCEDURE BookDrop.SwapRanking AS

SELECT BN.Name as BookName, COUNT(R.ReviewID) as Reviews
FROM BookDrop.BookCopy BC
    INNER JOIN BookDrop.BookName BN ON BC.NameID = BN.BookNameID
    INNER JOIN BookDrop.Review R ON BC.BookID = R.BookID
GROUP BY BC.BookID, BN.Name
ORDER BY Reviews DESC
GO
