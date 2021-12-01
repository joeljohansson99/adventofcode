part1 = do 
    contents <- readFile "input/day1.txt"
    let depths = mapToInt contents
    print . countInc $ depths

part2 = do
    contents <- readFile "input/day1.txt"
    let depths = mapToInt contents
    print . countSums $ depths

mapToInt :: String -> [Int]
mapToInt = map rInt . words

rInt :: String -> Int
rInt = read

countInc :: [Int] -> Int
countInc [x] = 0;
countInc (x:xs) 
    | x < head xs = 1 + countInc xs
    | otherwise = countInc xs

countSums :: [Int] -> Int
countSums [x,_,_] = 0
countSums (x:xs)
    | (sumOf 3 (x:xs)) < (sumOf 3 xs) = 1 + countSums xs
    | otherwise = countSums xs

sumOf :: Int -> [Int] -> Int
sumOf 0 _ = 0
sumOf n (x:xs) = x + (sumOf (n-1) xs)
