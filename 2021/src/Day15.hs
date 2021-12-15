import Data.List ( sort )
import Data.Functor.Contravariant.Compat.Repl (Comparison(getComparison))
part1 :: IO ()
part1 = do
    contents <- readFile "input/day15.txt"
    let points = mapToPoints 1 1 (map (map (\c -> rInt [c])) $ words contents)
    let connections = map (\p -> (p, getNeighbours p (filter (/=p) points))) points
    print $ calcPath [head points] 0 connections (last points)

type Point = (Int,Int,Int)
type Connection = (Point, [Point])

maxRisk :: Int
maxRisk = maxBound :: Int


calcPath :: [Point] -> Int -> [Connection] -> Point -> Int
calcPath path cost connections end =
    let current = last path
        neighbours = filter (`notElem` path) (getConnection current connections)
    in if current == end
    then
        cost
    else
        if null neighbours
        then
            maxRisk
        else
            minimum $ map (\p@(_,_,c) -> calcPath (path ++ [p]) (cost + c) connections end) neighbours

getRisk :: [Point] -> Int
getRisk [] = 0
getRisk ((_,_,r):ps) = r + getRisk ps

getConnection :: Point -> [Connection] -> [Point]
getConnection p [] = []
getConnection p (c:cs)
    | p == fst c = snd c
    | otherwise = getConnection p cs

getNeighbours :: Point -> [Point] -> [Point]
getNeighbours _ [] = []
getNeighbours p1@(a,b,_) (p2@(x,y,_):ps)
    | abs (a-x) + abs (a-y) < 2 = p2 : getNeighbours p1 ps
    | otherwise = getNeighbours p1 ps

getPoint :: Int -> Int -> [Point] -> Point
getPoint r c (p@(a,b,_):xss)
    | r == a && c == b = p
    | otherwise = getPoint r c xss

mapToPoints :: Int -> Int -> [[Int]] -> [Point]
mapToPoints r c xs
    | r > length xs = []
    | otherwise = (r,c,risk) : mapToPoints newR newC xs
        where risk = last $ take c (last $ take r xs)
              (newR, newC) = if c == length (head xs) then (r+1,1) else (r,c+1)

rInt :: String -> Int
rInt = read