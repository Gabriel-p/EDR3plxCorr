# Gaia EDR3 parallax correction

Based on the functions described in [Lindegren et al. (2020)](https://www.aanda.org/articles/aa/full_html/2021/05/aa39653-20/aa39653-20.html), the code returns the estimated parallax zero-point given the ecliptic latitude, magnitude and colour of any Gaia (E)DR3 source.

The code automatically deals with a mix of 5-p and 6-p solutions

As explained in Lindegren et al. (2020), the interpolations are only calibrated
within the following intervals:

```
1. $G$ magnitude: 6 < phot_g_mean_mag < 21
2. Colour:
  1. 1.1 < nu_eff_used_in_astrometry < 1.9 (5-p sources)
  2. 1.24 < pseudocolour < 1.72 (6-p sources)
```

Outside these ranges, the zero-point obtained is an extrapolation.

The code assumes that the data in the input file comes from Vizier, hence the required column names in the input data file are: `Plx, e_Plx, Gmag, nueff, pscol, ELAT, Solved`.



--------------------------------------------------------------
Source: https://gitlab.com/icc-ub/public/gaiadr3_zeropoint
