part1 = do 
    contents <- readFile "input/day2.txt"
    let commands = wordsWhen (=='\n') contents
    let splitted = matchMap commands
    let sum      = (calcHor splitted) * (calcDepth splitted)
    print sum

matchMap :: [String] -> [(String, Int)]
matchMap [] = []
matchMap (x:xs) = [(head ys, read (last ys))] ++ (matchMap xs)
    where ys = wordsWhen (==' ') x

calcHor :: [(String, Int)] -> Int
calcHor [] = 0
calcHor (x:xs)
    | (fst x) == "forward" = snd x + calcHor xs
    | otherwise = calcHor xs

calcDepth :: [(String, Int)] -> Int
calcDepth [] = 0
calcDepth (x:xs)
    | (fst x) == "up" = calcDepth xs - snd x
    | (fst x) == "down" = snd x + calcDepth xs
    | otherwise = calcDepth xs

rInt :: String -> (Int, String)
rInt = read

wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'