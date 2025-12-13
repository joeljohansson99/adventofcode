part1 = do
    contents <- readFile "input/day4.txt"
    let lines = wordsWhen (=='\n') contents
    let choices = splitToInt (==',') (head lines)
    let boards = splitInto 5 (getRows . tail $ lines)
    print (findWinner choices boards)

part2 = do
    contents <- readFile "input/day4.txt"
    let lines = wordsWhen (=='\n') contents
    let choices = splitToInt (==',') (head lines)
    let boards = splitInto 5 (getRows . tail $ lines)
    print (findLastWinner choices boards)

findLastWinner :: [Int] -> [[[Int]]] -> Int
findLastWinner [] _ = 0
findLastWinner (c:cs) xs = 
    let newBoard = mark c xs
        (win, sum) = isWin newBoard
        filtered = filterWin newBoard
    in if (win && (length xs == 1))
        then sum * c
        else findLastWinner cs filtered

filterWin :: [[[Int]]] -> [[[Int]]]
filterWin [] = []
filterWin (x:xs) = 
    let (win, _) = checkBoard x
    in if win
        then filterWin xs
        else x : filterWin xs

findWinner :: [Int] -> [[[Int]]] -> Int 
findWinner [] _ = 0
findWinner (c:cs) xs = 
    let newBoard = mark c xs 
        (win, sum) = isWin newBoard
    in if win
        then sum * c
        else findWinner cs newBoard

isWin :: [[[Int]]] -> (Bool, Int)
isWin [] = (False, 0)
isWin (x:xs) = 
    let (win, sum) = checkBoard x
    in if win
        then (True, sum)
        else isWin xs

checkBoard :: [[Int]] -> (Bool, Int)
checkBoard xs = 
    let rows = checkRows xs
        cols = checkCols 5 xs
    in if (rows || cols)
        then (True, calcSum xs)
        else (False, 0)

calcSum :: [[Int]] -> Int
calcSum xs = sum (map sumRow xs)

sumRow :: [Int] -> Int
sumRow [] = 0
sumRow (x:xs)
    | x == -1 = sumRow xs
    | otherwise = x + sumRow xs

checkCols :: Int -> [[Int]] -> Bool
checkCols 0 _ = False
checkCols n xs
    | sumRow (getCol n xs) == 0 = True
    | otherwise = checkCols (n-1) xs

checkRows :: [[Int]] -> Bool
checkRows [] = False
checkRows (x:xs)
    | sumRow x == 0 = True
    | otherwise = checkRows xs

mark :: Int -> [[[Int]]] -> [[[Int]]]
mark _ [] = []
mark c (x:xs) = mark2 c x : mark c xs

mark2 :: Int -> [[Int]] -> [[Int]]
mark2 _ [] = []
mark2 c (x:xs) = mark3 c x : mark2 c xs

mark3 :: Int -> [Int] -> [Int]
mark3 _ [] = []
mark3 c (x:xs)
    | c == x = -1 : mark3 c xs
    | otherwise = x : mark3 c xs

splitInto :: Int -> [a] -> [[a]]
splitInto _ [] = []
splitInto n xs = (take n xs) : (splitInto n (drop n xs))

splitToInt :: (Char -> Bool) -> String -> [Int]
splitToInt b s = map read (wordsWhen b s)

getCol :: Int -> [[Int]] -> [Int]
getCol _ [] = []
getCol n (x:xs) = (last (take n x)) : getCol n xs

getRows :: [String] -> [[Int]]
getRows [] = []
getRows (x:xs) = splitToInt (==' ') x : getRows xs

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'