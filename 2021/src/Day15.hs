import qualified Data.PSQueue as Q
import qualified Data.Array as A
import Data.Maybe ( fromJust )
import Data.IntMap (minView)

part1 :: IO ()
part1 = do
    contents <- readFile "input/day15.txt"
    let risks = map (map (\c -> rInt [c])) $ words contents
    let (h,w) = (length risks, length $ head risks)
    let costs = A.listArray ((1,1),(h, w)) (concat risks) A.// [((1,1), 0)]
    let visited = A.listArray ((1,1),(h, w)) $ True : replicate (w*h-1) False
    let queue = Q.insert (1,1) 0 Q.empty
    print $ calcPath queue costs visited (h,w)

part2 :: IO ()
part2 = do
    contents <- readFile "input/day15.txt"
    let risks = extend 0 $ map (map (\c -> rInt [c])) $ words contents
    let (h,w) = (length risks, length $ head risks)
    let costs = A.listArray ((1,1),(h, w)) (concat risks) A.// [((1,1), 0)]
    let visited = A.listArray ((1,1),(h, w)) $ True : replicate (w*h-1) False
    let queue = Q.insert (1,1) 0 Q.empty
    print $ calcPath queue costs visited (h,w)

type Pos = (Int,Int)
type Cost = A.Array Pos Int
type Visited = A.Array Pos Bool
type PrioQueue = Q.PSQ Pos Int

extend :: Int -> [[Int]] -> [[Int]]
extend 5 xs = []
extend n xs = map (extendRow 0 . map (+n)) xs ++ extend (n+1) xs

extendRow :: Int -> [Int] -> [Int]
extendRow 5 _ = []
extendRow n xs = map (\x -> if x+n > 9 then x+n-9 else x+n) xs ++ extendRow (n+1) xs

calcPath :: PrioQueue -> Cost -> Visited -> Pos -> PrioQueue
calcPath qs cs vs end =
    let ((c Q.:-> d), qs') = fromJust $ Q.minView qs
        next = filter (\n -> not $ vs A.! n) $ diggable cs c
        vs' = vs A.// map (\n -> (n,True)) next
        dist = map (\n -> (n,cs A.! n)) next
        qs'' = insertAll qs' dist d
    in if c == end then qs else calcPath qs'' cs vs' end

insertAll :: PrioQueue -> [(Pos,Int)] -> Int -> PrioQueue
insertAll qs [] _ = qs
insertAll qs ((p,i):ps) d = insertAll (Q.insert p (i+d) qs) ps d

addVisited :: Visited -> [Pos] -> Visited
addVisited = foldl (\ vs p -> vs A.// [(p, True)])

diggable :: Cost -> Pos -> [Pos]
diggable costs (x,y) = filter (A.inRange $ A.bounds costs) [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

rInt :: String -> Int
rInt = read