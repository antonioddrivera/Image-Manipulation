import System.Environment

-- Find difference between max pixel value and current pixel value
subtractBy1 :: [Int] -> [Int]
subtractBy1 [] = []
subtractBy1 (x:xs) = (255 - x) : subtractBy1 xs

main :: IO ()


main = do
    -- Command line args are collected as a string
    args <- getArgs

    -- read is an inbuilt function to convert string to int. ::[Int] is the type signatuure
    let numbers = map read args :: [Int]

        -- call the function
        result = subtractBy1 numbers

        -- conver the result back into string
        resultStrings = map show result
        outputString = unwords resultStrings
    -- print the string
    putStrLn outputString