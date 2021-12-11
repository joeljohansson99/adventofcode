part1 :: IO ()
part1 = do
    contents <- readFile "input/day11.txt"
    let octos = mapToOctopus 1 1 (map (map (\ x -> rInt [x])) (words contents))
    print $ step octos 0 100

part2 :: IO ()
part2 = do
    contents <- readFile "input/day11.txt"
    let octos = mapToOctopus 1 1 (map (map (\ x -> rInt [x])) (words contents))
    print $ allFlash octos 0

type Octopus = (Int, Int, Int)

step :: [Octopus] -> Int -> Int -> Int
step _ n 0 = n
step os n i =
    let incremented = update os
        (calm, flashed) = flashes incremented []
        newOctos = calm ++ map (\(n,r,c) -> (0,r,c)) flashed
    in step newOctos (n + length flashed) (i-1)

allFlash :: [Octopus] -> Int -> Int
allFlash os n =
    let incremented = update os
        (calm, flashed) = flashes incremented []
        newOctos = calm ++ map (\(n,r,c) -> (0,r,c)) flashed
    in if null calm then n+1 else allFlash newOctos (n+1)

flashes :: [Octopus] -> [Octopus] -> ([Octopus],[Octopus])
flashes os fs =
    let flash = flashing os
        calm = filter (`notElem` flash) os
    in if null flash
        then (os,fs)
        else flashes (foldl (flip incFlashes) calm flash) (fs++flash)

incFlashes :: Octopus -> [Octopus] -> [Octopus]
incFlashes _ [] = []
incFlashes o1@(n1,r1,c1) (o2@(n2,r2,c2):os)
    | abs (r1-r2) < 2 && abs (c1-c2) < 2 = (n2+1,r2,c2) : incFlashes o1 os
    | otherwise = o2 : incFlashes o1 os

flashing :: [Octopus] -> [Octopus]
flashing [] = []
flashing (o@(n,r,c):os)
    | n > 9 = o : flashing os
    | otherwise = flashing os

update :: [Octopus] -> [Octopus]
update [] = []
update ((n,r,c):os) = (n+1,r,c) : update os

mapToOctopus :: Int -> Int -> [[Int]] -> [Octopus]
mapToOctopus r c xs
    | r > length xs = []
    | otherwise = (energy,r,c) : mapToOctopus newR newC xs
        where energy = last $ take c (last $ take r xs)
              (newR, newC) = if c == length (head xs) then (r+1,1) else (r,c+1)

rInt :: String -> Int
rInt = read