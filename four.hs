------------------------------------------------------------------------------
-- | Project Euler No. 4
--
-- Find the largest palindrome made from the product of 2 three-digit numbers.

is_palindrome :: Integer -> Bool
is_palindrome x = reverse (show x) == show x

result = show (maximum (filter is_palindrome numbers))
    where
        r = [100..999]
        numbers = concat [[(i * j)  | i <- r, i <= j] | j <- r]

main :: IO ()
main = do 
    putStrLn result