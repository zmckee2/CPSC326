-- Zach McKee
-- CPSC 326:01
-- Homework 9b
-- This file contains the functions from homework 9 with pattern matching
-- This function takes in a list and returns the largest element
myMaximum :: Ord a => [a] -> a
myMaximum [] = error "Empty List"
myMaximum [x] = x
myMaximum (x:xs)
    | x > tailMax = x
    | otherwise = tailMax
    where
        tailMax = myMaximum xs

-- This function takes in a list and returns a reversed verison
myReverse :: [a] -> [a]
myReverse [] = []
myReverse xs = (xs !! (length xs - 1)) : myReverse (init xs)

-- This function takes in a list and returns the length
myLength :: Num b => [a] -> b
myLength [] = 0
myLength (_:xs) = 1 + myLength(xs)

-- This function takes in a element and list
-- Evaluates to true if the element is in the list, otherwise false
myElement :: Eq a => a -> [a] -> Bool
myElement _ [] = False
myElement key (x:xs)
    | key == x = True
    | otherwise = myElement key xs

-- This function takes in a pair and a list. The resulting list has all
-- occurances of the first in the pair replaced by the second
myReplace :: Eq a => (a,a) -> [a] -> [a]
myReplace _ [] = []
myReplace pair (x:xs)
    | first == x = second : myReplace pair xs
    | otherwise = x : myReplace pair xs
    where  
        first = fst pair
        second = snd pair

-- This function takes in a list of pairs and a list.
-- It replaces all occurances of the first element of each pair with second
myReplaceAll :: Eq a => [(a,a)] -> [a] -> [a]
myReplaceAll [] xs = xs
myReplaceAll (x:xs) ys = myReplaceAll xs (myReplace x ys)

-- This function takes in an element and list
-- It returns the sum of all occuranes of the element
myElementSum :: (Num a, Eq a) => a -> [a] -> a
myElementSum _ [] = 0
myElementSum elm (x:xs)
    | x == elm = elm + myElementSum elm xs
    | otherwise = myElementSum elm xs

-- This function takes in a list and removes any duplicate elements
removeDuplicates :: Eq a => [a] -> [a]
removeDuplicates [] = []
removeDuplicates (x:xs)
    | myElement x xs = removeDuplicates xs
    | otherwise = x : removeDuplicates xs

-- This function sorts a list using mergesort
mergeSort :: Ord a => [a] -> [a]
mergeSort xs
    | len < 2 = xs
    | otherwise = merge (mergeSort left) (mergeSort right)
    where
        len = length xs
        left = (take (div (len) 2) xs)
        right = (drop (div (len) 2) xs)

-- This function serves as a helper function for merge sort.
-- It performs the merge of the sort by building a list with the
-- smallest elements first.
merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) (ys)