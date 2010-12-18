------------------------------------------------------------------------------
-- | Project Euler No. 7
-- 
-- 10001st prime number.
-- 

import Data.List (find)
import Data.Maybe (isNothing)

isqrt = ceiling . sqrt . fromIntegral

is_prime :: Int -> Bool
is_prime 2 = True
is_prime 3 = True
is_prime n = isNothing result
    where
        test_vals = [2,3] ++ [x | x <- [3,5..isqrt n], x `mod` 3 /= 0]
        result = find (\x -> n `mod` x == 0) test_vals

primes = take 10001 [x | x <- [2..], is_prime x]

main :: IO ()
main = do 
    putStrLn (show (last primes))
