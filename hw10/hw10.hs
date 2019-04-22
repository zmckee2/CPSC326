data List a = Node a (List a)
            | Nil
            deriving(Show, Eq)

insert :: a -> List a -> List a
insert a Nil = Node a (Nil)
insert a (Node cur rest) = Node cur (insert a rest)

delete :: Eq a => a -> List a -> List a
delete _ Nil = Nil
delete rm (Node cur rest)
    | rm == cur = rest
    | otherwise = Node cur (delete rm rest)

memberOf :: Eq a => a -> List a -> Bool
memberOf _ Nil = False
memberOf elm (Node cur rest)
    | elm == cur = True
    | otherwise = memberOf elm rest

elementAt :: Int -> List a -> a
elementAt _ Nil = error "Index out of bounds"
elementAt i (Node elm rest)
    | i == 0 = elm
    | otherwise = elementAt (i-1) rest

insertAt :: Int -> a -> List a -> List a
insertAt _ _ Nil = error "Index out of bounds"
insertAt i elm (Node cur rest)
    | i == 0 = Node elm (Node cur rest)
    | otherwise = Node cur (insertAt (i-1) elm rest)

deleteAt :: Int -> List a -> List a
deleteAt _ Nil = error "Index out of bounds"
deleteAt i (Node cur rest)
    | i == 0 = rest
    | otherwise = Node cur (deleteAt (i-1) rest)

concatenate :: List a -> List a -> List a
concatenate Nil l2 = l2
concatenate (Node cur rest) l2 = Node cur (concatenate rest l2)

-- This function runs selection sort
sortList :: Ord a => List a -> List a
sortList Nil = Nil
sortList (Node elm Nil) = Node elm Nil
sortList (Node elm rest) = let minVal = findMin elm rest
                               restNoMin = delete minVal (Node elm rest)
                               in Node minVal (sortList restNoMin)

-- This is a helper function for performing selection sort
-- in sort list
findMin :: Ord a => a -> List a -> a
findMin curMin Nil = curMin
findMin curMin (Node elm rest)
    | elm < curMin = findMin elm rest
    | otherwise = findMin curMin rest

mapList :: (a -> b) -> List a -> List b
mapList _ Nil = Nil
mapList f (Node elm rest) = Node (f elm) (mapList f rest)

zipWithList :: (a -> b -> c) -> List a -> List b -> List c
zipWithList _ Nil _ = Nil
zipWithList _ _ Nil = Nil
zipWithList f (Node xelm xrest) (Node yelm yrest) 
                            = Node (f xelm yelm) (zipWithList f xrest yrest)