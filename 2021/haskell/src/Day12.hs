import Data.Char ( isLower )

part1 :: IO ()
part1 = do
    contents <- readFile "input/day12.txt"
    let caves = readCaveLinks $ words contents
    print . length $ paths caves ["start"]

part2 :: IO ()
part2 = do
    contents <- readFile "input/day12.txt"
    let caves = readCaveLinks $ words contents
    print . length $ weightedPaths caves ["start"] False

type Cave = String
type CaveLink = (Cave, Cave)
type Path = [Cave]

weightedPaths :: [CaveLink] -> Path -> Bool -> [Path]
weightedPaths cs p b 
    | current == "end" = [p]
    | otherwise = concatMap (\c -> weightedPaths newCaves (p++[c]) visited ) connections
        where current = last p
              visited = if b then b else visitedSmallCave current (init p)
              newCaves
                | isLowerCase current && b = filter (\(s,e) -> e /= current) cs
                | isLowerCase current && visited = filter (\(s,e) -> not (isLowerCase e && e `elem` p)) cs
                | otherwise = cs
              connections = getConnections current newCaves

visitedSmallCave :: Cave -> [Cave] -> Bool
visitedSmallCave c cs = isLowerCase c && c `elem` cs


paths :: [CaveLink] -> Path -> [Path]
paths cs p
    | current == "end" = [p]
    | otherwise = concatMap (\c -> paths newCaves (p++[c])) connections
        where current = last p
              newCaves = if isLowerCase current then filter (\(s,e) -> e /= current) cs else cs
              connections = getConnections current newCaves

isLowerCase :: Cave -> Bool
isLowerCase = all isLower

getConnections :: Cave -> [CaveLink] -> [Cave]
getConnections _ [] = []
getConnections s ((a,b):cs)
    | s == a = b : getConnections s cs
    | otherwise = getConnections s cs

readCaveLinks :: [String] -> [CaveLink]
readCaveLinks [] = []
readCaveLinks (c:cs) = if s == "start" then (s,e) : readCaveLinks cs else [(s,e),(e,s)] ++ readCaveLinks cs
    where [s,e] = wordsWhen (=='-') c

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'