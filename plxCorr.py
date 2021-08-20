
import os
from zero_point import zpt
from pathlib import Path
from astropy.io import ascii
from astropy.table import Table
import matplotlib.pyplot as plt


def main():
    """
    """
    # Initialize table of coefficients
    zpt.load_tables()

    # Load file with the estimated true members and the Gaia EDR3 added columns
    files = readFiles()

    for file in files:
        print(file.name)
        data = Table.read(file, format='ascii')

        # The names of the column change because this is data retrieved
        # from Vizier, not from https://gaia.aip.de/query/

        # phot_g_mean_mag --> Gmag
        gmag = data['Gmag'].data
        # nu_eff_used_in_astrometry --> nueff
        nueffused = data['nueff'].data
        # pseudocolour --> pscol
        psc = data['pscol'].data
        # ecl_lat --> ELAT
        ecl_lat = data['ELAT'].data
        # astrometric_params_solved --> Solved
        soltype = data['Solved'].data

        # 'get_zpt()' will fail if there are sources with 2-p solutions
        valid = soltype > 3
        print("Stars with soltype=3: {}".format((~valid).sum()))

        # Apply the Parallax correction. The values here are to be *subtracted*
        # from the observed parallaxes
        zpvals = zpt.get_zpt(gmag[valid], nueffused[valid], psc[valid],
                             ecl_lat[valid], soltype[valid])

        # New column with the corrected parallax values
        data = data[valid]
        data['Plx_corr'] = data['Plx'] - zpvals

        # Save output file with the corrected parallax values
        out_path = Path(Path.cwd(), 'output', file.name)
        ascii.write(data, out_path, overwrite=True)

        out_path = Path(
            Path.cwd(), 'output', file.name.replace('dat', 'png'))
        fig = plt.figure(figsize=(15, 5))
        plt.subplot(131)
        plt.scatter(data['Gmag'], zpvals, alpha=.5)
        plt.ylabel("zpvals")
        plt.xlabel("Gmag")

        plt.subplot(132)
        msk = (data['Plx_corr'] > -.5) & (data['Plx_corr'] < 5)
        plt.hist(data['Plx_corr'][msk], 50)
        plt.xlabel("Plx (corrected)")

        plt.subplot(133)
        plt.scatter(data['Gmag'], data['e_Plx'], alpha=.5)
        plt.ylabel("e_Plx")
        plt.xlabel("Gmag")

        fig.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches='tight')
        plt.clf()
        plt.close("all")


def readFiles():
    """
    Read files from the input folder
    """
    files = []

    for pp in Path(Path.cwd(), 'input/').iterdir():
        if not pp.name.endswith(".md"):
            if pp.is_file():
                files += [pp]
            else:
                files += [arch for arch in pp.iterdir()]

    return files


if __name__ == '__main__':
    if not os.path.exists('output'):
        os.makedirs('output')
    main()
