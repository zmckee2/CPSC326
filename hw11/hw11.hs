
-- file: main.hs
import System.Environment (getArgs)
import Data.Char (toUpper, isUpper)

-- read input file, apply function to input file, display result
interactWith function inputFile =
  do input <- readFile inputFile
     putStrLn (function input)

-- starting point of the program: call interactWith on "myFunction"
-- where "myFunction" (with type String -> String) must be replaced
-- with the name of the function to call on the input. 
main =
  do args <- getArgs
     case args of
       [input] -> interactWith remWords input
       _ -> putStrLn "error: exactly one argument needed"

toUpperCase xs = (map toUpper xs)

capitals xs = unwords(filter (\x -> isUpper (head x)) (words xs))

remWords wholeList = let brokenUp = lines wholeList
                         theWords = words(brokenUp !! 0)
                         theString = brokenUp !! 1
                         in foldl remWord theString theWords

remWord theString word = unwords(filter (\x-> x /= word) (words theString))