import Data.Char

part1 :: IO ()
part1 = do
    contents <- readFile "input/day2.txt"
    let lines = wordsWhen (=='\n') contents
    print . sumPossibleIds $ map getGame lines

part2 :: IO ()
part2 = do
    contents <- readFile "input/day2.txt"
    let lines = wordsWhen (=='\n') contents
    print . sumPowers $ map getGame lines

sumPowers :: [(Int, [[(Int, String)]])] -> Int
sumPowers [] = 0
sumPowers ((_, sets):xs) = getPower sets + sumPowers xs

getPower :: [[(Int, String)]] -> Int
getPower xs = do
    let (red, green, blue) = getFewestForSet xs
    red * green * blue

getFewestForSet :: [[(Int, String)]] -> (Int, Int, Int)
getFewestForSet [] = (0,0,0)
getFewestForSet (x:xs) = do
    let (red, blue, green) = getFewest x
    let (red', blue', green') = getFewestForSet xs
    (max red red', max blue blue', max green green')

getFewest :: [(Int, String)] -> (Int, Int, Int)
getFewest [] = (0,0,0)
getFewest ((count, color):xs) = do
    let (red, blue, green) = getNeeded count color
    let (red', blue', green') = getFewest xs
    (max red red', max blue blue', max green green')

getNeeded :: Int -> String -> (Int, Int, Int)
getNeeded count color
    | color == "red" = (count, 0, 0)
    | color == "green" = (0, count, 0)
    | otherwise = (0, 0, count)


sumPossibleIds :: [(Int, [[(Int, String)]])] -> Int
sumPossibleIds [(id, sets)]
    | isPossible sets = id
    | otherwise = 0
sumPossibleIds ((id, sets):xs)
    | isPossible sets = id + sumPossibleIds xs
    | otherwise = sumPossibleIds xs

isPossible :: [[(Int, String)]] -> Bool
isPossible [set] = checkSet set
isPossible (set:sets) = checkSet set && isPossible sets

checkSet :: [(Int, String)] -> Bool
checkSet [(count, color)] = checkLimits count color
checkSet ((count, color):xs) = checkLimits count color && checkSet xs

checkLimits :: Int -> String -> Bool
checkLimits count color
    | color == "red" = count <= 12
    | color == "green" = count <= 13
    | otherwise = count <= 14

getGame :: String -> (Int, [[(Int, String)]])
getGame xs = do
    let game = wordsWhen (== ':') xs
    let id = read . getNum $ head game
    let sets = wordsWhen (== ';') (last game)
    let cubes = map getCubes sets
    (id, cubes)

getCubes :: String -> [(Int, String)]
getCubes xs = formatCubes (wordsWhen (==' ') (filter (/=',') xs))

formatCubes :: [String] -> [(Int, String)]
formatCubes [x,y] = [(read x, y)]
formatCubes (x:y:xs) = (read x, y) : formatCubes xs

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'

getNum :: String -> String
getNum [] = []
getNum (x:xs)
    | isDigit x = x:getNum xs
    | otherwise = getNum xs
