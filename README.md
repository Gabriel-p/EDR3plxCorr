# Gaia EDR3 parallax correction

Based on the functions described in [Lindegren et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/05/aa39653-20/aa39653-20.html), the code returns the estimated parallax zero-point given the ecliptic latitude, magnitude and colour of any Gaia (E)DR3 source.

The code automatically deals with a mix of 5-p and 6-p solutions

As explained in Lindegren et al. (2021), the interpolations are only calibrated
within the following intervals:

```
1. $G$ magnitude: 6 < phot_g_mean_mag < 21
2. Colour:
  1. 1.1 < nu_eff_used_in_astrometry < 1.9 (5-p sources)
  2. 1.24 < pseudocolour < 1.72 (6-p sources)
```

Outside these ranges, the zero-point obtained is an extrapolation.

The code assumes that the data in the input file comes from Vizier, hence the required column names in the input data file are: `Plx, e_Plx, Gmag, nueff, pscol, ELAT, Solved`.


TODO: other corrections

* [An estimation of the Gaia EDR3 parallax bias from stellar clusters and Magellanic Clouds data, Apellaniz (2021)][https://api.semanticscholar.org/CorpusID:238259369]
* [The parallax zero-point offset from Gaia EDR3 data, Groenewegen (2021)](https://ui.adsabs.harvard.edu/abs/2021A%26A...654A..20G/abstract)
* [A Spatially Dependent Correction of Gaia EDR3 Parallax Zero-point Offset based on 0.3 million LAMOST DR8 Giant Stars, Wang et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022AJ....163..149W/abstract)



--------------------------------------------------------------
Source: https://gitlab.com/icc-ub/public/gaiadr3_zeropoint
