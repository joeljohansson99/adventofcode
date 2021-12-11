import Data.List ( sort )
part1 :: IO ()
part1 = do
    contents <- readFile "input/day10.txt"
    let lines = words contents
    print .sum $ map (`parseLine` "") lines

part2 :: IO ()
part2 = do
    contents <- readFile "input/day10.txt"
    let lines = words contents
    let scores = filter (/=0) (sort $ map ((`sumRest` 0) . (`incomplete` "")) lines)
    print . last $ take ((length scores `div` 2) + 1) scores

sumRest :: String -> Int -> Int
sumRest xs n = foldl (\ n x -> n * 5 + findValue2 x) n xs

parseLine :: String -> String -> Int
parseLine [x] ps
    | head ps == x = 0
    | otherwise = findValue x
parseLine (x:xs) ps
    | x `elem` "([{<" = parseLine xs (parseOpening x ps)
    | otherwise =
        let (parsed, expect) = parseClosing x ps
        in if parsed
            then parseLine xs expect
            else findValue x

incomplete :: String -> String -> String
incomplete [] ps = ps
incomplete (x:xs) ps
    | x `elem` "([{<" = incomplete xs (parseOpening x ps)
    | otherwise =
        let (parsed, expect) = parseClosing x ps
        in if parsed
            then incomplete xs expect
            else []

findValue2 :: Char -> Int
findValue2 c = case c of
    ')' -> 1
    ']' -> 2
    '}' -> 3
    '>' -> 4
    _ -> 0

findValue :: Char -> Int
findValue c = case c of
    ')' -> 3
    ']' -> 57
    '}' -> 1197
    '>' -> 25137
    _ -> 0

parseOpening :: Char -> String -> String
parseOpening c xs = case c of
    '(' -> ')':xs
    '[' -> ']':xs
    '{' -> '}':xs
    '<' -> '>':xs
    _ -> ""

parseClosing :: Char -> String -> (Bool, String)
parseClosing c xs =
    if c == head xs
        then (True, tail xs)
        else (False, xs)