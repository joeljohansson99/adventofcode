import Data.List

part1 :: IO ()
part1 = do
    contents <- readFile "input/day9.txt"
    let numbers = map (map (\ x -> read [x])) (words contents)
    print . sum $ calcLowest 1 1 numbers

part2 :: IO ()
part2 = do
    contents <- readFile "input/day9.txt"
    let numbers = map (map (\ x -> read [x])) (words contents)
    let pits = getLowPoints 1 1 numbers
    let largestBasins = take 3 (reverse . sort $ map length (allBasins pits numbers))
    print . product $ largestBasins

allBasins :: [(Int,Int,Int)] -> [[Int]] -> [[(Int,Int,Int)]]
allBasins [] _ = []
allBasins (p:ps) xs = rmDuplicate (basin p xs) : allBasins ps xs

basin :: (Int,Int,Int) -> [[Int]] -> [(Int,Int,Int)]
basin (r,c,n) xs =
        let neighbors = getRowPoints r c xs ++ getColPoints r c xs
        in
            (r,c,n) : mapBasin (filter (\(a,b,c) -> c > n && c /= 9) neighbors) xs

mapBasin :: [(Int,Int,Int)] -> [[Int]] -> [(Int,Int,Int)]
mapBasin [] _ = []
mapBasin (p:ps) xs = basin p xs ++ mapBasin ps xs

getLowPoints :: Int -> Int -> [[Int]] -> [(Int,Int,Int)]
getLowPoints r c xs
    | r > length xs = []
    | isPit = (r,c,num) : getLowPoints newR newC xs
    | otherwise = getLowPoints newR newC xs
        where isPit = check r c xs
              num = get c (get r xs)
              newC = if c == length (get 1 xs) then 1 else c+1
              newR = if newC == 1 then r+1 else r

rmDuplicate :: [(Int,Int,Int)] -> [(Int,Int,Int)]
rmDuplicate [] = []
rmDuplicate (x:xs) = x : rmDuplicate (filter (/= x) xs)

calcLowest :: Int -> Int -> [[Int]] -> [Int]
calcLowest r c xs
    | r > length xs = []
    | isPit = 1 + num : calcLowest newR newC xs
    | otherwise = calcLowest newR newC xs
        where isPit = check r c xs
              num = get c (get r xs)
              newC = if c == length (get 1 xs) then 1 else c+1
              newR = if newC == 1 then r+1 else r

check :: Int -> Int -> [[Int]] -> Bool
check r c xs
    | num < minimum adj = True
    | otherwise = False
        where num = get c (get r xs)
              adj = getRow r c xs ++ getCol r c xs

count :: Int -> [Int] -> Int
count _ [] = 0
count n (x:xs)
    | n == x = 1 + count n xs
    | otherwise = count n xs

getRow :: Int -> Int -> [[Int]] -> [Int]
getRow r c xs
    | c == 1 = [get (c+1) (get r xs)]
    | c == length (get r xs) = [get (c-1) (get r xs)]
    | otherwise = [get (c-1) (get r xs), get (c+1) (get r xs)]

getCol :: Int -> Int -> [[Int]] -> [Int]
getCol r c xs
    | r == 1 = [get c (get (r+1) xs)]
    | r == length xs = [get c (get (r-1) xs)]
    | otherwise = [get c (get (r-1) xs), get c (get (r+1) xs)]

getRowPoints :: Int -> Int -> [[Int]] -> [(Int,Int,Int)]
getRowPoints r c xs
    | c == 1 = [(r,c+1,get (c+1) (get r xs))]
    | c == length (get r xs) = [(r,c-1,get (c-1) (get r xs))]
    | otherwise = [(r,c-1,get (c-1) (get r xs)), (r,c+1,get (c+1) (get r xs))]

getColPoints :: Int -> Int -> [[Int]] -> [(Int,Int,Int)]
getColPoints r c xs
    | r == 1 = [(r+1,c,get c (get (r+1) xs))]
    | r == length xs = [(r-1,c,get c (get (r-1) xs))]
    | otherwise = [(r-1,c,get c (get (r-1) xs)), (r+1,c,get c (get (r+1) xs))]

get :: Int -> [a] -> a
get i xs = last (take i xs)
