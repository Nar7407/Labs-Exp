import numpy as np
from scipy import linalg, stats
A = np . array ([[2 , 1] , [1 , 3]])
b = np . array ([8 , 13])
print (" Determinant :", linalg . det ( A ) )
print (" Inverse :\n", linalg . inv ( A ) )
print (" Solution of Ax = b:", linalg . solve (A , b ) )
print (" Eigenvalues :", linalg . eigvals ( A ) )

data = [12 , 15 , 12 , 18 , 20 , 15 , 15 , 22]
desc = stats . describe ( data )
print ( desc )
print (" Skewness :", stats . skew ( data ) )
print (" Kurtosis :", stats . kurtosis ( data ) )
print (" Ranks :", stats . rankdata ( data ) )
stat , p = stats . shapiro ( data )
print (" Shapiro - Wilk statistic :", stat , " p- value :", p )
print (" Normal " if p > 0.05 else "Not normal ")

group1 = [22 , 25 , 28 , 24 , 26]
group2 = [30 , 35 , 28 , 40 , 32]
stat , p = stats . levene ( group1 , group2 )
print (" Levene statistic :", stat , " p- value :", p )

x = [1 , 2 , 3 , 4 , 5]
y = [2 , 4 , 5 , 4 , 5]
pearson_corr , p_val = stats . pearsonr (x , y )
spearman_corr , p_val2 = stats . spearmanr (x , y )
print (" Pearson :", pearson_corr , " Spearman :", spearman_corr )

import pandas as pd
t_stat , p = stats . ttest_1samp ( data , popmean =15)
print ("One - sample t- test p- value :", p )
t_stat2 , p2 = stats . ttest_ind ( group1 , group2 )
print (" Independent t- test p- value :", p2 )
f_stat , p3 = stats . f_oneway ( group1 , group2 , [18 , 20 , 19 , 21 , 17])
print (" ANOVA p- value :", p3 )
u_stat , p = stats . mannwhitneyu ( group1 , group2 )
print ("Mann - Whitney U p- value :", p )
h_stat , p2 = stats . kruskal ( group1 , group2 , [18 , 20 , 19 , 21 , 17])
print (" Kruskal - Wallis p- value :", p2 )

import scipy . ndimage as ndi
from scipy import datasets
import matplotlib . pyplot as plt
img = datasets . ascent ()
flipped = np . fliplr ( img )
rotated = ndi . rotate ( img , angle =45)
blurred = ndi . gaussian_filter ( img , sigma =3)
cropped = img [50:400 , 50:400]
fig , axes = plt . subplots (1 , 4 , figsize =(14 , 4) )
for ax , im , title in zip( axes , [ flipped , rotated , blurred ,cropped ] ,[" Flipped ", " Rotated ", " Blurred ", "Cropped "]) :
    ax . imshow ( im , cmap ="gray")
    ax . set_title ( title )
    ax . axis ("off")