part1 :: IO ()
part1 = do
    contents <- readFile "input/day13.txt"
    let dots = map toDot $ takeWhile (\s -> head s /= 'f') $ words contents
    let folds = map (toFold . dropWhile (\ c -> c /= 'x' && c /= 'y')) (dropWhile (\ s -> head s /= 'f') $ wordsWhen (== '\n') contents)
    print $ foldOnce (head folds) dots

part2 :: IO ()
part2 = do
    contents <- readFile "input/day13.txt"
    let dots = map toDot $ takeWhile (\s -> head s /= 'f') $ words contents
    let folds = map (toFold . dropWhile (\ c -> c /= 'x' && c /= 'y')) (dropWhile (\ s -> head s /= 'f') $ wordsWhen (== '\n') contents)
    let codes = filterDuplicate $ folding folds dots
    putStr $ unlines $ generateGrid $ map (\d -> ('#',snd d, fst d)) codes

setVal :: Int -> a -> [a] -> [a]
setVal idx val lst = h ++ (val : tail t)
    where (h, t) = splitAt idx lst

setCell :: (Char, Int, Int) -> [[Char]] -> [[Char]]
setCell (c, x, y) grid = setVal x xl grid
    where xl = setVal y c $ grid !! x

generateGrid :: [(Char, Int, Int)] -> [[Char]]
generateGrid cs = take (mx+1) $ map (take (my+1)) grid
    where (mx, my, grid) = foldr step (0, 0, g) cs
          g = repeat $ repeat ' '
          step co@(c, x, y) (mx, my, g) =
            let g' = setCell co g
                mx' = max x mx
                my' = max y my
            in
                (mx', my', g')

type Dot = (Int,Int)
type Fold = (String, Int)

foldOnce :: Fold -> [Dot] -> [Dot]
foldOnce f ds
    | pos == "x" = filterDuplicate $ map (\d -> if fst d > line then (2*line - fst d, snd d) else d) ds
    | pos == "y" = filterDuplicate $ map (\d -> if snd d > line then (fst d, 2*line - snd d) else d) ds
        where (pos, line) = f

folding :: [Fold] -> [Dot] -> [Dot]
folding [] ds = ds
folding (f:fs) ds
    | pos == "x" = folding fs (map (\d -> if fst d > line then (2*line - fst d, snd d) else d) ds)
    | pos == "y" = folding fs (map (\d -> if snd d > line then (fst d, 2*line - snd d) else d) ds)
        where (pos, line) = f

filterDuplicate :: [Dot] -> [Dot]
filterDuplicate [] = []
filterDuplicate (d:ds)
    | d `elem` ds = filterDuplicate ds
    | otherwise = d : filterDuplicate ds

toDot :: String -> Dot
toDot s = let w = wordsWhen (==',') s in (rInt $ head w, rInt $ last w)

toFold :: String -> Fold
toFold s = let w = wordsWhen (=='=') s in (head w, rInt $ last w)
rInt :: String -> Int
rInt = read

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'
