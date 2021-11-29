module advent where

main = do 
    contents <- readFile "../input/test.txt"
    print . mapToWords $ contents

mapToInt :: String -> [Int]
mapToInt = map rInt . words

mapToWords :: String -> [String]
mapToWords = words

rInt :: String -> Int
rInt = read