part1 :: IO ()
part1 = do
    contents <- readFile "input/day16.txt"
    print (sum (fst (decode . mapHexToBin $ contents)))

part2 :: IO ()
part2 = do
    contents <- readFile "input/day16.txt"
    print (fst (calc . mapHexToBin $ contents))

calc :: String -> (Int, String)
calc ps = do
    let r1 = drop 3 ps
    let t = binToDec (take 3 r1)
    let r2 = drop 3 r1
    if t == 4 then
        let (v, rs) = literal r2
        in (binToDec v, rs)
    else do
        let i = binToDec (take 1 r2)
        let r3 = drop 1 r2
        if i == 0 then do
            let l = binToDec (take 15 r3)
            let r4 = drop 15 r3
            let vs = calcRest (take l r4)
            (calcVal vs t, drop l r4)
        else do
            let l = binToDec (take 11 r3)
            let (vs, rs) = calcWhile (drop 11 r3) l
            (calcVal vs t, rs)

calcVal :: [Int] -> Int -> Int
calcVal ps t
    | t == 0 = sum ps
    | t == 1 = product ps
    | t == 2 = minimum ps
    | t == 3 = maximum ps
    | t == 5 = fromEnum (head ps > last ps)
    | t == 6 = fromEnum (head ps < last ps)
    | t == 7 = fromEnum (head ps == last ps)
    | otherwise = 0


calcWhile :: String -> Int -> ([Int], String)
calcWhile ps 0 = ([], ps)
calcWhile ps x = do
    let (vs, rs) = calc ps
    let (vs', rs') = calcWhile rs (x-1)
    ([vs] ++ vs', rs')

calcRest :: String -> [Int]
calcRest [] = []
calcRest ps = let (vs, rs) = calc ps
            in vs:calcRest rs

decode :: String -> ([Int], String)
decode ps = do
    let v = binToDec (take 3 ps)
    let r1 = drop 3 ps
    let t = binToDec (take 3 r1)
    let r2 = drop 3 r1
    if t == 4 then
        ([v], snd . literal $ r2)
    else do
        let i = binToDec (take 1 r2)
        let r3 = drop 1 r2
        if i == 0 then do
            let l = binToDec (take 15 r3)
            let r4 = drop 15 r3
            let vs = decodeRest (take l r4)
            (v : vs, drop l r4)
        else do
            let l = binToDec (take 11 r3)
            let (vs, rs) = decodeWhile (drop 11 r3) l
            (v : vs, rs)

decodeWhile :: String -> Int -> ([Int], String)
decodeWhile ps 0 = ([], ps)
decodeWhile ps x = do
    let (vs, rs) = decode ps
    let (vs', rs') = decodeWhile rs (x-1)
    (vs ++ vs', rs')

decodeRest :: String -> [Int]
decodeRest [] = []
decodeRest ps = let (vs, rs) = decode ps
            in vs ++ decodeRest rs

literal :: String -> (String, String)
literal xs =  if head (take 5 xs) == '1' then
    let (g, r) = literal (drop 5 xs)
    in (drop 1 (take 5 xs) ++ g, r)
    else (drop 1 (take 5 xs), drop 5 xs)

binToDec :: String -> Int
binToDec [] = 0
binToDec xs = read [last xs] + 2 * binToDec (init xs)

mapHexToBin :: String -> String
mapHexToBin = concatMap hexToBin

hexToBin :: Char -> String
hexToBin x = case x of
    '0' -> "0000"
    '1' -> "0001"
    '2' -> "0010"
    '3' -> "0011"
    '4' -> "0100"
    '5' -> "0101"
    '6' -> "0110"
    '7' -> "0111"
    '8' -> "1000"
    '9' -> "1001"
    'A' -> "1010"
    'B' -> "1011"
    'C' -> "1100"
    'D' -> "1101"
    'E' -> "1110"
    'F' -> "1111"
    _ -> "ERROR"

