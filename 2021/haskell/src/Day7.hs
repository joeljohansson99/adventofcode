part1 :: IO ()
part1 = do
    contents <- readFile "input/day7.txt"
    let positions = map rInt $ wordsWhen (==',') contents
    let mid = shortestDistance 0 positions
    print (calcDiff mid positions)

part2 :: IO ()
part2 = do
    contents <- readFile "input/day7.txt"
    let positions = map rInt $ wordsWhen (==',') contents
    let mid = shortestGrowDistance 0 positions (calcGrowDiff 0 positions)
    print (calcGrowDiff mid positions)

shortestGrowDistance :: Int -> [Int] -> Int -> Int
shortestGrowDistance n xs last
    | last < next = n
    | otherwise = shortestGrowDistance (n+1) xs next
        where next = calcGrowDiff (n+1) xs

calcGrowDiff :: Int -> [Int] -> Int
calcGrowDiff _ [] = 0
calcGrowDiff n (x:xs) = (sum1 . abs $ (x-n)) + calcGrowDiff n xs

sum1 :: Int -> Int
sum1 0 = 0
sum1 n = n + sum1 (n-1)

shortestDistance :: Int -> [Int] -> Int
shortestDistance n xs
    | under n xs > ((length xs) `div` 2) = n
    | otherwise = shortestDistance (n+1) xs 

calcDiff :: Int -> [Int] -> Int
calcDiff _ [] = 0
calcDiff n (x:xs) = abs (x-n) + calcDiff n xs

under :: Int -> [Int] -> Int
under _ [] = 0
under n (x:xs) 
    | n >= x = 1 + under n xs
    | otherwise = under n xs

rInt :: String -> Int
rInt = read

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'