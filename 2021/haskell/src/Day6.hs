part1 :: IO ()
part1 = do
    contents <- readFile "input/day6.txt"
    let fish = addFish (map rInt . wordsWhen (==',') $ contents) []
    print . count $ evolve 80 fish

part2 :: IO ()
part2 = do
    contents <- readFile "input/day6.txt"
    let fish = addFish (map rInt . wordsWhen (==',') $ contents) []
    print . count $ evolve 256 fish

type Fish = (Int, Int)

compress :: Int -> [Fish] -> [Fish]
compress n [] = [(6, n)]
compress n (f:fs)
    | fst f == 6 = compress (n + snd f) fs
    | otherwise = f : compress n fs

count :: [Fish] -> Int
count = foldr ((+) . snd) 0

evolve :: Int -> [Fish] -> [Fish]
evolve 0 xs = xs
evolve t xs =
    let (fish, babies) = nextGen xs
    in evolve (t-1) (compress 0 (fish ++ [(8,babies)]))

nextGen :: [Fish] -> ([Fish], Int)
nextGen [] = ([], 0)
nextGen (x:xs)
    | fst x == 0 = ((6, snd x):fish, babies+snd x)
    | otherwise = ((fst x - 1, snd x):fish, babies)
        where
            (fish, babies) = nextGen xs

addFish :: [Int] -> [Fish] -> [Fish]
addFish xs fs = foldl (flip addFish') fs xs

addFish' :: Int -> [Fish] -> [Fish]
addFish' x [] = [(x,1)]
addFish' x (f:fs)
    | x == fst f = (x, snd f + 1) : fs
    | otherwise = f : addFish' x fs

rInt :: String -> Int
rInt = read

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'