
decrypt :: Int -> Int -> Int -> Int 
decrypt x e n = (x ^ e) `mod` n