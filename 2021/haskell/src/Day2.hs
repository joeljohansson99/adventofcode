part1 = do
    contents <- readFile "input/day2.txt"
    let commands = wordsWhen (=='\n') contents
    let splitted = matchMap commands
    print (calc splitted 0 0)

part2 = do
    contents <- readFile "input/day2.txt"
    let commands = wordsWhen (=='\n') contents
    let splitted = matchMap commands
    print (calcWithAim splitted 0 0 0)

matchMap :: [String] -> [(String, Int)]
matchMap [] = []
matchMap (x:xs) = (head ys, read . last $ ys) : matchMap xs
    where ys = wordsWhen (==' ') x

calc :: [(String, Int)] -> Int -> Int -> Int
calc [] h d = h*d
calc (x:xs) h d
    | fst x == "forward" = calc xs (h + snd x) d
    | fst x == "up" = calc xs h (d - snd x)
    | fst x == "down" = calc xs h (d + snd x)
    | otherwise = calc xs h d

calcWithAim :: [(String, Int)] -> Int -> Int -> Int -> Int
calcWithAim [] h d a = h*d
calcWithAim (x:xs) h d a
    | fst x == "forward" = calcWithAim xs (h + snd x) (d + a * snd x) a
    | fst x == "up" = calcWithAim xs h d (a - snd x)
    | fst x == "down" = calcWithAim xs h d (a + snd x)
    | otherwise = calcWithAim xs h d a

wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'