part1 :: IO ()
part1 = do
    contents <- readFile "input/day8.txt"
    let numbers = map words $ filter' (map (drop 61) (wordsWhen (=='\n') contents))
    print . sum . map countDistinct $ numbers

part2 :: IO ()
part2 = do
    contents <- readFile "input/day8.txt"
    let lines = map words $ wordsWhen (\c -> c=='|' || c == '\n') contents
    let codes = getCodes lines 1
    let numbers = getNums lines 1
    let patterns = map (getPattern . (\n -> prepare n [] [])) codes
    print . sum $ mapDecode numbers patterns

type Code = (String, Int)

mapDecode :: [[String]] -> [[Code]] -> [Int]
mapDecode [] _ = []
mapDecode _ [] = []
mapDecode (xs:xss) (cs:css) = decode xs cs : mapDecode xss css

decode :: [String] -> [Code] -> Int
decode [] _ = 0
decode (x:xs) cs = n * p + decode xs cs
    where n = findCode x cs
          p = 10 ^ length xs

findCode :: String -> [Code] -> Int
findCode _ [] = -1000
findCode s ((c,i):cs)
    | isAnagram s c = i
    | otherwise = findCode s cs

getCodes :: [[String]] -> Int -> [[String]]
getCodes [] _ = []
getCodes (x:xs) n
    | odd n = x : getCodes xs (n+1)
    | otherwise = getCodes xs (n+1)

getNums :: [[String]] -> Int -> [[String]]
getNums [] _ = []
getNums (x:xs) n
    | even n = x : getNums xs (n+1)
    | otherwise = getNums xs (n+1)

countDistinct :: [String] -> Int
countDistinct [] = 0
countDistinct (x:xs)
    | l == 2 || l == 3 || l == 4 || l == 7 = 1 + countDistinct xs
    | otherwise = countDistinct xs
        where l = length x

prepare :: [String] -> [Code] -> [String] -> ([Code], [String])
prepare [] cs rs = (cs, rs)
prepare (x:xs) cs rs
    | l == 2 = prepare xs ((x,1):cs) rs
    | l == 3 = prepare xs ((x,7):cs) rs
    | l == 4 = prepare xs ((x,4):cs) rs
    | l == 7 = prepare xs ((x,8):cs) rs
    | otherwise = prepare xs cs (x:rs)
        where l = length x

-- b 4, c 4, d 5, f 5

getPattern :: ([Code],[String]) -> [Code]
getPattern (cs,rs) =
    let seven = getNum 7 cs
        eight = getNum 8 cs
        one = getNum 1 cs
        four = getNum 4 cs
        a = diff seven one
        charMap = mapToCount (diff "abcdefg" a) rs
        g = getCharCount charMap 6
        e = getCharCount charMap 3
        b = diff (diff four one) (getCharCount charMap 5)
        d = diff four (one++b)
        f = diff one (getCharCount charMap 4)
        c = diff one f

    in [(a++b++c++e++f++g,0),(a++c++d++e++g,2),(a++c++d++f++g,3),(a++b++d++f++g,5),(a++b++d++e++f++g,6),(a++b++c++d++f++g,9)] ++ cs

mapToCount :: String -> [String] -> [(Char, Int)]
mapToCount [] _ = []
mapToCount (x:xs) rs = (x, countPos rs x) : mapToCount xs rs

countPos :: [String] -> Char -> Int
countPos [] _ = 0
countPos (x:xs) c
    | c `elem` x = 1 + countPos xs c
    | otherwise = countPos xs c

getCharCount :: [(Char,Int)] -> Int -> String
getCharCount [] _ = []
getCharCount ((c,i):xs) n
    | i == n = c : getCharCount xs n
    | otherwise = getCharCount xs n

diff :: String -> String -> String
diff [] _ = []
diff (x:xs) ys
    | x `elem` ys = diff xs ys
    | otherwise = x : diff xs ys

getNum :: Int -> [Code] -> String
getNum _ [] = ""
getNum n ((s,i):cs)
    | i == n = s
    | otherwise = getNum n cs


isAnagram :: String -> String -> Bool
isAnagram x s = all (`elem` s) x && length x == length s

filter' :: [String] -> [String]
filter' [] = []
filter' (x:xs)
    | '|' `elem` x = filter' xs
    | otherwise = x : filter' xs

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'