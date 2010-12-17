------------------------------------------------------------------------------
-- | Project Euler No. 5
--
-- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
--
-- What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
-- Answer: 232792560

import Data.List (find)

-- NOTE: This implementation is terribly slow...needs to improve.

is_match :: Int -> Bool
is_match x = (length result) == 19
    where
        factors = reverse [2..20]
        result = takeWhile (== 0) [x `mod` i | i <- factors]

posibilities = [2521..]
r = find is_match posibilities
result = show (find is_match posibilities)

main :: IO ()
main = do 
    putStrLn result