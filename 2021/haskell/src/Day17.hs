import Data.Char (isDigit)

part1 :: IO ()
part1 = do
    contents <- readFile "input/day17.txt"
    let [x, xe, y, ye] = getNum contents
    let vy = abs y - 1
    print ( findTop 0 vy )


part2 :: IO ()
part2 = do
    contents <- readFile "input/day17.txt"
    let [x, xe, y, ye] = getNum contents
    let xs = findXs 0 x xe
    let ys = findYs (-(abs y)) y ye
    print (countOk ys xs (x,xe) (y, ye))

signedDigit :: Char -> Bool
signedDigit c = isDigit c || (c == '-')

getNum :: String -> [Int]
getNum [] = []
getNum xs = do
    let parsed = dropWhile (not . signedDigit) xs
    let num = takeWhile signedDigit parsed
    let rest = dropWhile signedDigit parsed
    read num : getNum rest

findXs :: Int -> Int -> Int -> [Int]
findXs x s e
    | checkX 0 x s e = x : findXs (x+1) s e
    | x > e = []
    | otherwise = findXs (x+1) s e

checkX :: Int -> Int -> Int -> Int -> Bool
checkX x dx s e
    | x >= s && x <= e = True
    | x > e || dx == 0 = False
    | otherwise = checkX (x+dx) (dx-1) s e

findYs :: Int -> Int -> Int -> [Int]
findYs y s e
    | checkY 0 y s e = y : findYs (y+1) s e
    | y > abs e = []
    | otherwise = findYs (y+1) s e

checkY :: Int -> Int -> Int -> Int -> Bool
checkY y dy s e
    | y >= s && y <= e = True
    | y < s = False
    | otherwise = checkY (y+dy) (dy-1) s e

countOk :: [Int] -> [Int] -> (Int, Int) -> (Int, Int) -> Int
countOk [] _ _ _ = 0
countOk (y:ys) xs (sx, ex) (sy, ey) = countOkX y xs (sx, ex) (sy, ey) + countOk ys xs (sx, ex) (sy, ey) 


countOkX :: Int -> [Int] -> (Int, Int) -> (Int, Int) -> Int
countOkX _ [] _ _ = 0
countOkX y (x:xs) (sx, ex) (sy, ey) 
    | checkOk (0,0) (x, y) (sx, ex) (sy, ey) = 1 + countOkX y xs (sx, ex) (sy, ey)
    | otherwise = countOkX y xs (sx, ex) (sy, ey)

checkOk :: (Int, Int) -> (Int, Int) -> (Int, Int) -> (Int, Int) -> Bool
checkOk (x,y) (dx, dy) (sx, ex) (sy, ey)
    | x > ex || y < sy = False
    | (y >= sy && y <= ey) && (x >= sx && x <= ex) = True
    | otherwise = checkOk (x+dx,y+dy) (max (dx-1) 0, dy-1) (sx, ex) (sy, ey)

findTop :: Int -> Int -> Int
findTop y dy
    | dy > 0 = findTop (y + dy) (dy - 1)
    | otherwise = y