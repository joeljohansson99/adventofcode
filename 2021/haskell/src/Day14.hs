{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
part1 :: IO ()
part1 = do
    contents <- readFile "input/day14.txt"
    let code = head . words $contents
    let tmp = map (\s -> (take 2 s, last s)) $ tail $ wordsWhen (=='\n') contents
    let pairs = map (\(p,c) -> (p, (init p++[c], c : tail p))) tmp
    let codes = getCodes code
    let t = map (\s -> (take 2 s, last s)) $ tail $ wordsWhen (=='\n') contents
    let entries = startEntries codes (map (\(p,_) -> (p,0)) tmp)
    let charCount = map (\c -> (c,0)) $ distinct $ map snd t
    let calculated = step pairs entries 10
    let counted = map snd $ increaseLetters (head code) (last code) (map (\(c,n) -> (c, n `div` 2)) (countChars calculated charCount))
    let (max,min) = (maximum counted,minimum counted)
    print $ max - min

part2 :: IO ()
part2 = do
    contents <- readFile "input/day14.txt"
    let code = head . words $contents
    let tmp = map (\s -> (take 2 s, last s)) $ tail $ wordsWhen (=='\n') contents
    let pairs = map (\(p,c) -> (p, (init p++[c], c : tail p))) tmp
    let codes = getCodes code
    let t = map (\s -> (take 2 s, last s)) $ tail $ wordsWhen (=='\n') contents
    let entries = startEntries codes (map (\(p,_) -> (p,0)) tmp)
    let charCount = map (\c -> (c,0)) $ distinct $ map snd t
    let calculated = step pairs entries 40
    let counted = map snd $ increaseLetters (head code) (last code) (map (\(c,n) -> (c, n `div` 2)) (countChars calculated charCount))
    let (max,min) = (maximum counted,minimum counted)
    print $ max - min

type Entry = (String, Int)
type Pair = (String, (String,String))

increaseLetters :: Char -> Char -> [(Char, Int)] -> [(Char, Int)]
increaseLetters _ _ [] = []
increaseLetters f l ((c,n):cs)
    | f == c || l == c = (c,n+1) : increaseLetters f l cs
    | otherwise = (c,n) : increaseLetters f l cs

countChars :: [Entry] -> [(Char,Int)] -> [(Char, Int)]
countChars [] cs = cs
countChars ((e,n):es) cs = countChars es (addCharCount (head e) (addCharCount (last e) cs n) n)

addCharCount :: Char -> [(Char,Int)] -> Int -> [(Char, Int)]
addCharCount _ [] _ = []
addCharCount c ((x,n):xs) i
    | c == x = (x,n+i) : xs
    | otherwise = (x,n) : addCharCount c xs i

startEntries :: [String] -> [Entry] -> [Entry]
startEntries xs es = foldl (\ es x -> addCount es x 1) es xs

step :: [Pair] -> [Entry] -> Int -> [Entry]
step _ es 0 = es
step ps es n = step ps (decreaseOldEntries (newEntries es es ps) es) (n-1)

findTransform :: String -> [Pair] -> [String]
findTransform s (p:ps)
    | fst p == s = [fst . snd $ p, snd . snd $ p]
    | otherwise = findTransform s ps

newEntries :: [Entry] -> [Entry] -> [Pair] -> [Entry]
newEntries [] ret _ = ret
newEntries ((e,n):es) ret ps
    | n > 0 =
        let [e1,e2] = findTransform e ps
        in newEntries es (addCount (addCount ret e1 n) e2 n) ps
    | otherwise = newEntries es ret ps

decreaseOldEntries :: [Entry] -> [Entry] -> [Entry]
decreaseOldEntries [] [] = []
decreaseOldEntries ((e1,n1):ns) ((e2,n2):os) = (e1,n1-n2) : decreaseOldEntries ns os

getCodes :: String -> [String]
getCodes [x,y] = [[x,y]]
getCodes (x:y:xs) = [x,y] : getCodes (y:xs)

addCount :: [Entry] -> String -> Int -> [Entry]
addCount ((e,n):es) s i
    | e == s = (e,n+i) : es
    | otherwise = (e,n) : addCount es s i

distinct :: String -> String
distinct [] = []
distinct (x:xs) = x : distinct (filter (/=x) xs)

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'