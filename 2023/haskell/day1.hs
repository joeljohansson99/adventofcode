import Data.Char
import Data.Maybe

part1 :: IO ()
part1 = do 
    contents <- readFile "input/day1.txt"
    let lines = words contents
    print . getSum $ lines

part2 :: IO ()
part2 = do
    contents <- readFile "input/day1.txt"
    let lines = words contents
    print . getSum2 $ lines

getSum :: [String] -> Int
getSum [xs] = read ([getFirst xs] ++ [getFirst (reverse xs)])
getSum (xs:xss) = read ([getFirst xs] ++ [getFirst (reverse xs)]) + getSum xss

getFirst :: String -> Char
getFirst [x] = x
getFirst (x:xs)
    | isDigit x = x
    | otherwise = getFirst xs

getSum2 :: [String] -> Int
getSum2 [xs] = read ([getFirst2 [] xs] ++ [getLast2 [] xs])
getSum2 (xs:xss) = read ([getFirst2 [] xs] ++ [getLast2 [] xs]) + getSum2 xss

getFirst2 :: String -> String -> Char
getFirst2 ys xs
    | isDigit . head $ xs = head xs
    | otherwise = case checkFirst [] (ys ++ [head xs]) of
        Just c -> c
        Nothing -> getFirst2 (ys ++ [head xs]) (tail xs)

getLast2 :: String -> String -> Char
getLast2 ys xs
    | isDigit . last $ xs = last xs
    | otherwise = case checkLast [] ([last xs] ++ ys) of
        Just c -> c
        Nothing -> getLast2 ([last xs] ++ ys) (init xs)

checkLast :: String -> String -> Maybe Char
checkLast ys [] = mapToNum ys
checkLast ys xs = case mapToNum ys of 
    Just c -> Just c
    Nothing -> checkLast (ys ++ [head xs]) (tail xs)

checkFirst :: String -> String -> Maybe Char
checkFirst ys [] = mapToNum ys
checkFirst ys xs = case mapToNum ys of 
    Just c -> Just c
    Nothing -> checkFirst ([last xs] ++ ys) (init xs)

mapToNum :: String -> Maybe Char
mapToNum xs
    | xs == "one" = Just '1'
    | xs == "two" = Just '2'
    | xs == "three" = Just '3'
    | xs == "four" = Just '4'
    | xs == "five" = Just '5'
    | xs == "six" = Just '6'
    | xs == "seven" = Just '7'
    | xs == "eight" = Just '8'
    | xs == "nine" = Just '9'
    | otherwise = Nothing