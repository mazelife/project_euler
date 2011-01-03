------------------------------------------------------------------------------
-- | Project Euler No. 9
--
-- A Pythagorean triplet is a set of three natural numbers, a < b < c, 
-- for which, a^(2) + b^(2) = c^(2)
-- 
-- For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
--
--There exists exactly one Pythagorean triplet for which a + b + c = 1000.
--Find the product abc.

import Data.List (find)
import Data.Maybe (isJust, fromJust)

get_triple :: (Int, Int) -> [Int]
get_triple (m, n) = [a,b,c]
    where
        msqr = m ^ 2
        nsqr = n ^ 2
        a = msqr - nsqr
        b = 2 * m * n
        c = msqr + nsqr

generate_pairs :: Int -> [(Int, Int)]
generate_pairs seed = zip left right
    where
        left = take (seed-1) (repeat seed)
        right = reverse [1..(seed-1)]

test_values :: Int -> [Int]
test_values seed
    | isJust y      = fromJust y
    | otherwise     = test_values (seed + 1)
    where
        y = find (\x -> sum x == 1000) [get_triple x | x <- (generate_pairs seed)]

main :: IO ()
main = do 
    putStrLn (show (product (test_values 2)))