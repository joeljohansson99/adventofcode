import Data.Char (digitToInt)
import Data.List (foldl')

part1 = do 
    contents <- readFile "input/day3.txt"
    let nums = words contents
    let mc = mcb_word nums (length . head  $ nums)
    let lc = complement mc
    print (toDec mc * toDec lc)

part2 = do 
    contents <- readFile "input/day3.txt"
    let nums = words contents
    let ogr = find_ogr nums 1
    let csr = find_csr nums 1
    print (toDec ogr * toDec csr)

mcb :: [String] -> Int -> Int -> Int -> Char
mcb [] i o z
    | o >= z = '1'
    | otherwise = '0'
mcb (x:xs) i o z 
    | last (take i x) == '1' = mcb xs i (o+1) z
    | otherwise = mcb xs i o (z+1)

mcb_word :: [String] -> Int -> String
mcb_word xs 0 = ""
mcb_word xs n = mcb_word xs (n-1) ++ [(mcb xs n 0 0)]

complement :: String -> String
complement [] = []
complement (x:xs) 
    | x == '1' = '0' : complement xs
    | otherwise = '1' : complement xs

toDec :: String -> Int
toDec = foldl' (\acc x -> acc * 2 + digitToInt x) 0

find_ogr :: [String] -> Int -> String
find_ogr [s] _ = s
find_ogr xs n = find_ogr (filterBits xs n (mcb xs n 0 0)) (n+1)

find_csr :: [String] -> Int -> String
find_csr [s] _ = s
find_csr xs n = case mcb xs n 0 0 of 
    '1' -> find_csr (filterBits xs n '0') (n+1)
    '0' -> find_csr (filterBits xs n '1') (n+1)

filterBits :: [String] -> Int -> Char -> [String]
filterBits [] _ _ = []
filterBits (x:xs) n c 
    | last (take n x) == c = x : filterBits xs n c
    | otherwise = filterBits xs n c