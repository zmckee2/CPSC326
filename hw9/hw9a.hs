-- Zach McKee
-- CPSC 326:01
-- Homework 9a
-- This file contains the functions from homework 9 without pattern matching
-- This function takes in a list and returns the largest element
myMaximum :: Ord a => [a] -> a
myMaximum xs = if null xs then error "Empty List"
               else if length xs == 1 then xs !! 0
               else if (xs !! 0) > myMaximum (tail xs) then xs !! 0
               else myMaximum(tail xs)

-- This function takes in a list and returns a reversed verison
myReverse :: [a] -> [a]
myReverse xs = if null xs then []
               else (xs !! (length xs - 1)) : myReverse (init xs)

-- This function takes in a list and returns the length
myLength :: Num b => [a] -> b
myLength xs = if null xs then 0
              else 1 + myLength(tail xs)

-- This function takes in a element and list
-- Evaluates to true if the element is in the list, otherwise false
myElement :: Eq a => a -> [a] -> Bool
myElement key xs = if null xs then False
                   else if head xs == key then True
                   else myElement key (tail xs)

-- This function takes in a pair and a list. The resulting list has all
-- occurances of the first in the pair replaced by the second
myReplace :: Eq a => (a,a) -> [a] -> [a]
myReplace pair xs = if null xs then []
                    else if (head xs) == (fst pair) then (snd pair) : myReplace pair (tail xs)
                    else (head xs) : myReplace pair (tail xs)

-- This function takes in a list of pairs and a list.
-- It replaces all occurances of the first element of each pair with second
myReplaceAll :: Eq a => [(a,a)] -> [a] -> [a]
myReplaceAll pairList replaceList = if null pairList then replaceList
                                    else myReplaceAll (tail pairList) (myReplace (head pairList) replaceList)

-- This function takes in an element and list
-- It returns the sum of all occuranes of the element
myElementSum :: (Num a, Eq a) => a -> [a] -> a
myElementSum elm xs = if null xs then 0
                      else if head xs == elm then elm + myElementSum elm (tail xs)
                      else myElementSum elm (tail xs)

-- This function takes in a list and removes any duplicate elements
removeDuplicates :: Eq a => [a] -> [a]
removeDuplicates xs = if (null xs) then [] 
                      else if myElement (head xs) (tail xs) then removeDuplicates(tail xs)
                      else (head xs) : removeDuplicates(tail xs)

-- This function sorts a list using mergesort
mergeSort :: Ord a => [a] -> [a]
mergeSort xs = if length xs < 2 then xs else
               merge (mergeSort (take (div (length xs) 2) xs)) (mergeSort (drop (div (length xs) 2) xs))

-- This function serves as a helper function for merge sort.
-- It performs the merge of the sort by building a list with the
-- smallest elements first.
merge :: Ord a => [a] -> [a] -> [a]
merge xs ys = if null xs then ys
              else if null ys then xs
              else if (head xs) < (head ys) then (head xs) : (merge(tail xs) (ys))
              else (head ys) : (merge (xs) (tail ys))
