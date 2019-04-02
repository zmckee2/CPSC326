-- This function takes in 3 numbers and returns the middle number if applicable
median3 :: Ord a => a -> a -> a -> a
median3 a b c = if (a==b || b == c || a==c) then if (a==b) then a else c
                else if ((a>b && a<c) || (a>c && a<b)) then a 
                else if ((b>a && b<c) || (b>c && b<a)) then b else c

-- This function takes in two tuples of fractional numbers and
-- returns the midpoint between them
midpoint :: (Fractional t1, Fractional t) => (t1,t) -> (t1,t) -> (t1,t)
midpoint (x1,y1) (x2,y2) = ((x1+x2)/2,(y1+y2)/2)

-- This function takes in a list and returns all elements besides the last
allButLast :: [a] -> [a]
allButLast xs = if null xs then error "Empty list" else
                take ((length xs) - 1) xs

-- This function takes in a list and returns the last element without tail
lastElem :: [a] -> a
lastElem xs = if null xs then error "Empty list" else
                head (drop ((length xs) - 1) xs)

-- This function takes in a list and index and returns the element
-- at the given index
elemAt :: Int -> [t] -> t
elemAt i xs = if i >= length xs || i < 0 then error "Invalid index" else
                head (drop i xs)

-- This function takes in a list, an index, and a value and replaces
-- the element at the given index with the new value
replaceInList :: [a] -> Int -> a -> [a]
replaceInList xs i new = if i >= length xs || i < 0 then error "Invalid index" else
                            (take i xs) ++ (new : (drop (i+1) xs))

-- This function takes a list and replaces every element with
-- the largest element
replaceMax :: Ord a => [a] -> [a]
replaceMax xs = replicate (length xs) (maximum xs)

-- This function takes two lists and returns each pair
-- between the lists where the element in the first index
-- is larger than the element in the second list
largeToSmallPairs :: Ord a => [a] -> [a] -> [(a,a)]
largeToSmallPairs xs ys = filter (\(x,y) -> x > y) (zip xs ys)

-- This function filters through a list and returns if the given
-- key is contained in the list
containsElem :: Eq a => a -> [a] -> Bool
containsElem key xs = not (null (filter (\x -> x==key) xs))

-- This function takes two lists and a key and returns a list that
-- contains each pair in the lists where the key appeared in a tuple.
-- The pairs from the first list come before the pairs in the second list
combine :: Eq a => a -> [(a,t)] -> [(a,t)] -> [(a,t)]
combine key xs ys = filter (\(x,y) -> x == key) (xs) ++ filter (\(x,y) -> x == key) (ys)