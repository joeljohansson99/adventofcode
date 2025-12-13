import Data.List.Split

part1 = do
    contents <- readFile "input/day5.txt"
    let lines = splitOn "\n" contents
    let points = betweenPoints . filterDiagonal . format . (map (splitOn " -> ")) $ lines
    print . intersections $ points

part2 = do
    contents <- readFile "input/day5.txt"
    let lines = splitOn "\n" contents
    let points = betweenPoints . filterUnusable . format . (map (splitOn " -> ")) $ lines
    print . intersections $ points

intersections :: [(Int,Int)] -> Int
intersections [] = 0
intersections (p:ps) 
    | p `elem` ps = 1 + intersections (filter (/=p) ps)
    | otherwise = intersections ps

betweenPoints :: [((Int,Int),(Int,Int))] -> [(Int,Int)]
betweenPoints [] = []
betweenPoints (((x1,y1),(x2,y2)):xs) 
    | x1 == x2 = makeYPoints x1 (y1,y2) ++ betweenPoints xs
    | y1 == y2 = makeXPoints (x1,x2) y1 ++ betweenPoints xs
    | otherwise = makeDiaPoints (x1,x2) (y1,y2) ++ betweenPoints xs

makeYPoints :: Int -> (Int,Int) -> [(Int,Int)]
makeYPoints x (y1,y2)
    | y1 == y2 = [(x,y1)]
    | y1 > y2 = (x,y1) : makeYPoints x (y1-1,y2)
    | y1 < y2 = (x,y1) : makeYPoints x (y1+1,y2)

makeXPoints :: (Int,Int) -> Int -> [(Int,Int)]
makeXPoints (x1,x2) y
    | x1 == x2 = [(x1,y)]
    | x1 > x2 = (x1,y) : makeXPoints (x1-1,x2) y
    | x1 < x2 = (x1,y) : makeXPoints (x1+1,x2) y

makeDiaPoints :: (Int,Int) -> (Int,Int) -> [(Int,Int)]
makeDiaPoints (x1,x2) (y1,y2)
    | x1 == x2 && y1 == y2 = [(x1,y1)]
    | x1 > x2 && y1 > y2 = (x1,y1) : makeDiaPoints (x1-1, x2) (y1-1,y2)
    | x1 > x2 && y1 < y2 = (x1,y1) : makeDiaPoints (x1-1, x2) (y1+1,y2)
    | x1 < x2 && y1 > y2 = (x1,y1) : makeDiaPoints (x1+1, x2) (y1-1,y2)
    | x1 < x2 && y1 < y2 = (x1,y1) : makeDiaPoints (x1+1, x2) (y1+1,y2)

format :: [[String]] -> [((Int,Int), (Int,Int))]
format [] = []
format (a:as) =
    let [x1,y1] = splitOn "," (head a)
        [x2,y2] = splitOn "," (last a)
    in 
    ((read x1, read y1), (read x2, read y2)) : format as

filterDiagonal :: [((Int,Int), (Int,Int))] -> [((Int,Int), (Int,Int))]
filterDiagonal [] = []
filterDiagonal (p@((x1,y1),(x2,y2)):xs)
    | x1 == x2 || y1 == y2 = p:filterDiagonal xs
    | otherwise = filterDiagonal xs

filterUnusable :: [((Int,Int), (Int,Int))] -> [((Int,Int), (Int,Int))]
filterUnusable [] = []
filterUnusable (p@((x1,y1),(x2,y2)):xs)
    | x1 == x2 || y1 == y2 || (abs (x1-x2) == abs (y1-y2)) = p:filterUnusable xs
    | otherwise = filterUnusable xs