title: Analysis Challenge #1
slug: challenge1

Welcome to the first ngEHT analysis challenge. The primary objectives
of this first challenge are to set up a framework for the generation
of synthetic ngEHT data based on theoretical source models, to conduct
the organized submission and cross-comparison of reconstruction
results from multiple people, and to get a first idea of the benefits
and challenges of ngEHT datasets as compared to the current EHT.

We invite participants to submit image reconstructions from a total of
eight synthetic datasets. Additionally, results from any non-imaging
analysis are also welcome, as well as an evaluation on the
challenge. This challenge includes two static total-intensity source
models (SgrA* and M87), and simulated observations a two frequencies
(230 and 345 GHz) using a hypothetical ngEHT array including the
current EHT and 10 additional stations (ngeht_ref1 and
eht_2022). Participants are requested to submit image reconstructions
by July 16th to the ngEHT challenge website -- see below for details
and instructions. Please note that unless otherwise specified, all
source models and data products should be kept proprietary among those
currently invited to participate in the challenge, which includes all
EHT Collaboration members.

The information below is (partly) published in our [Galaxies paper](https://ui.adsabs.harvard.edu/abs/2023Galax..11...12R/abstract).

## Table of Contents

- [Downloads](./#Downloads)
- [Submissions](./#Submissions)
- [Source models](./#SourceModels)

## Communicating with the organizers

The primary way to talk to the challenge organizers is the private
`analysis-challenge-1` channel on the ngEHT-2021 Slack.  If you need an
invite to the Slack or to the channel, please contact Greg at glindahl
ZAT cfa.harvard.edu.  We're also happy to help people with software
installation advice.

## Schedule

- June 18, 2021: General announcement
- July 16, 2021: Submission deadline
- May 1, 2022: Submission deadline for inclusion in Challenge 1+2 paper

## <a name="Downloads">Downloads</a>

Please note that unless otherwise specified, all source models and
data products should be kept proprietary among those currently invited
to participate in the challenge, which includes all EHT Collaboration
members.

Downloads are password protected: the username is `challenge1` and the
secret password is available if you ask on Slack, on the
`analysis-challenge-1` channel on the ngEHT-2021 Slack.

[Challenge 1 Downloads](../c1downloads/)

## Example Scripts

Joseph Farah has provided an example imaging script, [genericImaging.py](../scripts/genericImaging.py) (last updated July 15, 2021)

Running on `M87_eht2022_230_thnoise.uvfits`, it took 90 seconds and used 3 gigabytes of memory.

## <a name="Submissions">Submissions</a>

### Images

Please submit your images as FITS files bundled in a zip file. The
images can be reconstructed with any field of view or pixel
resolution, as long as this is clear from the FITS header. If you can,
submit an image for each of the eight provided datasets. For the M87
datasets and the ngeht_ref1 Sgr A* datasets, you may also analyze the
230 and 345 GHz data jointly. For Sgr A*, please submit your best
estimate of the intrinsic source structure (i.e. after any scattering
mitigation). You may submit multiple images reconstructed using
different methods; please follow the filename conventions as specified
below. We will be using eht-imaging to load and evaluate the images,
so it may be worth checking if your image loads properly in
eht-imaging.

### Non-imaging results

If you have performed analysis other than imaging (e.g., fit a
geometric model, measured the black hole mass or spin, or constrained
plasma parameters), please provide a text file summarizing your method
and results. These results will not be formally compared or analyzed,
but could certainly provide us with valuable insights.

### Evaluation

It would be helpful but not required to add a txt file summarizing your experience with this challenge. Think of questions like

- What imaging parameters did you find work best on these datasets?
- How difficult was it to image ngeht_ref1 versus eht_2022, or 345 GHz versus 230 GHz?
- Did the reconstruction quality and improvement of different arrays and frequencies meet your expectations?
- Based on your experience with these datasets, do you think there should be more development of the reconstruction method you used?
- What source models, data properties, or specific charges would you like to see in future challenges?
- Do you have any feedback on the infrastructure and organization of the challenges?

### Filename conventions

For the zip files, use the format challenge1\_[firstnamelastname].zip. 

Example: challenge1\_freekroelofs.zip

For the FITS files, use the format challenge1\_[source]\_[array]\_[frequency]\_[method]\_[firstnamelastname].fits

- source: SGRA or M87
- array: eht2022 or ngeht\_ref1
- frequency: 230, 345, or 230 + 345
- method: e.g. ehtim, smili, clean, themage

Example: challenge1\_SGRA\_eht2022\_230\_ehtim\_freekroelofs.fits

For non-imaging results, use the format challenge1\_[source]\_[array]\_[frequency]\_nonimaging\_[firstnamelastname].txt

Example: challenge1\_SGRA\_eht2022\_230\_nonimaging\_freekroelofs.txt

For the evaluation, use the format challenge1\_evaluation\_[firstnamelastname].txt. 

Example: challenge1\_evaluation\_freekroelofs.txt

## Submit your results

<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <input type="hidden" name="challenge" value="challenge1"/>
    <input type="text" name="name" placeholder="Your Name"/><br/>
    <input type="email" name="email" placeholder="Your Email"/><br/>
    <label for="zip">zip file: </label>
    <input id="zip" name="zip" type="file" value=""/><br/>

    <input type="submit" value="submit"/>
</form>

Our server has a 1 gigabit Internet connection, so uploads shouldn't
take too long.  The challenge organizers get notified by Slack for
every failed or successful upload. If you see any problems, we're likely
to reach out to contact you quickly.

## <a name="SourceModels">Source models</a>

### SGRA

![Sgr A* model](../static/sgra_model_challenge1.png)

Description: Semi-analytic stationary RIAF model for SgrA in the literature (see, e.g. Broderick & Loeb 2006). This model can be used to test the capabilities of next generation arrays in precision modeling of BH parameters. High resolution is needed to capture the unique signature from subring structure. This model does not capture any variability due to turbulence in the system.

Details: The basic model is a=0 (Schwarzschild) at an inclination of i=130 deg and all models include non-thermal particles. The model includes disk height (following Pu et al. 2018), sub-Keplerian flow properties (kappa=0.5, alpha=0.5) following the notation of Tiede et al. 2020 -- e.g. Eq. 10 and 11) and fitted to the observed data of Bower et al. 2015, 2019, Liu et al. 2016 and Zhao et al. 2003.

Citation: These images are generated for ngEHT end-to-end simulation studies by Christian Fromm (cfromm@th.physik.uni-frankfurt.de). Please contact C.F. for use outside ngEHT challenge activities.

Parameters:

- GRRT at 230/345 GHz at 4096x4096 pixels
- FOV 128M, d=8.178kpc and m=4.14M\_sun (GRAVITY et al. 2019)

Scattering: The 230 GHz and 345 GHz images were scattered with the
same realization of the Johnson et al. 2018 scattering model before
generating the synthetic data.

### M87

![M87 model](../static/m87_model_challenge1.png)

Description: MAD GRMHD frame from a rapid spinning black hole a=0.94
with electron thermodynamics from reconnection heating (see Mizuno et
al. 2021 for details
[https://ui.adsabs.harvard.edu/abs/2021arXiv210609272M/abstract](https://ui.adsabs.harvard.edu/abs/2021arXiv210609272M/abstract)).
The
GRMHD simulation was performed with the BHAC code (Porth et al. 2017)
using three levels of AMR in logarithm Kerr-Schild coordinates. The
numerical grid covers 384x192x192 cells in radial, azimuthal and theta
direction and is extending up to 2500 M in radial direction. The mass
accretion rate and MAD parameter (see Tchekhovskoy 2012) is monitored
and after obtaining a steady state we perform the general relativistic
radiative transfer calculations (GRRT).

During the radiative transport we include non-thermal particles via
the kappa electron distribution (see Pandya et al 2016) in the jet
sheath while excluding the highly magnetised spine by using a cut in
the magnetisation at a value of 1 (typically referred as sigma
cut.) The power-law slope of the kappa distribution is set by a
particle in cell (PIC) motivated sub-grid model depending on the local
magnetisation and plasma-beta following Ball et al. 2018. In addition
we include a fraction of the magnetic energy density to accelerate the
non-thermal particles (see Davelaar et al. 2019 and Cruz-Osorio
submitted). In the jet wind and disk region we use a thermal electron
distribution, where the electron temperature is directly obtained from
the GRMHD simulation. In order to guarantee capturing small scale
structure on the horizon scale and at the same time the large scale
jet structure, we used a FOV of 1mas using a resolution of 4096x4096
pixels.

Since the GRMHD simulations are scale free we normalise our GRRT
simulations by setting the mass (6.5e9 M_sun) and distance (16.9 Mpc)
of the black hole in M87 and iterate the mass accretion rate until a
compact flux density of 0.8 Jy at 230GHz is obtained.

The radiative transfer is performed with the well tested and highly
accurate radiative transfer code BHOSS (Younsi et al. 2020)

Citation: These images are generated for ngEHT end-to-end simulation
studies by Christian Fromm (cfromm@th.physik.uni-frankfurt.de). Please
cite Mizuno et al. 2021
[https://ui.adsabs.harvard.edu/abs/2021arXiv210609272M/abstract](https://ui.adsabs.harvard.edu/abs/2021arXiv210609272M/abstract)
and contact C.F. for use outside ngEHT challenge activities

Parameters:

- GRRT at 230/345 GHz at 4096x4096 pixels
- FOV 1 mas

## Array and Data Synthesis

### Station locations

Two arrays were used to generate the synthetic data. They are labeled
eht\_2022 and ngeht\_ref1. eht\_2022 consists of the 11 stations expected
to participate in the 2022 EHT observations. In ngeht\_ref1, 10
stations are added to this array. The station locations were chosen
based on a uv-coverage analysis led by Alex Raymond, investigating
which combination of sites from Raymond et al. (2021) provided optimal
uv-coverage, folding in weather dropouts. The LMT, SPT, and KP were
not included in the 345 GHz observations with eht\_2022. The station
locations are shown in the image below.

![ngEHT ref1](../static/ngeht_ref1.png)

### Data properties

A 24-hour observing track was simulated for each array, source, and
frequency, resulting in eight separate datasets. Each track consists
of 10-minute scans interleaved with 10-minute gaps and is identical
for each dataset. A single frequency channel with a time resolution of
10 seconds is provided.

Thermal noise expected from the receiver and enhanced by atmospheric
opacity were added to the complex visibilities. The following
assumptions were made for all sites:

- Receiver temperature:
- - 60 K for 230 GHz
- - 100 K for 345 GHz
- Aperture efficiency:
- - 0.68 for 230 GHz
- - 0.42 for 345 GHz
- Bandwidth: 8 GHz
- Quantization efficiency: 0.88
- Dish diameter: 6 m for new sites, actual diameter for existing sites
- Opacity: median values in April as extracted from the MERRA-2 data by Raymond et al. (2021), at 30 degrees elevation. The opacities were set constant throughout and across the different datasets, but are frequency-dependent.

Visibility phases were scrambled, but stabilized across scans. No further systematic errors were added, this will be done in future challenges.

After data generation, data points with a signal-to-noise ratio less than 1 were flagged.

### Summary table

The table below summarizes the station locations and SEFDs resulting
from the assumptions outlined above. For a more detailed breakdown,
see [arrays/station_info.csv](../c1downloads/Challenge_1/arrays/station_info.csv)

[jtable]
Station, Code, X (m), Y (m), Z (m), SEFD\_230 (Jy), SEFD\_345 (Jy)
IRAM-30m, PV, 5088968, -301682, 3825016, 809, 4456
SMT, AZ, -1828796, -5054407, 3427865, 4973, 27410
SMA, SM, -5464523, -2493147, 2150612, 1500, 5882
LMT, LM, -768714, -5988542, 2063276, 357, 2710
ALMA, AA, 2225061, -5440057, -2481681, 63, 231
SPT, SP, 0, 0, -6359610, 3669, 11552, 
APEX, AP, 2225040, -5441198, -2479303, 2609, 9261
JCMT, JC, -5464585, -2493001, 2150654, 2105, 8259
GLT, GL, 541647, -1388536, 6180829, 2417, 23326
NOEMA, PB, 4523998, 468045, 4460310, 307, 3022
KP, KP, -1994314, -5037909, 3357619, 3535, 34109
BAJA, BA, -2352576, -4940331, 3271508, 11125, 53309
BAR, BR, -2363000, -4445000, 3907000, 10905, 51219
CNI, CI, 5311000, -1725000, 3075000, 11813, 74896
CAT, CT, 1569000, -4559000, -4163000, 15321, 166684
GAM, GB, 5627890, 1637767, -2512493, 6099, 285727
GARS, GR, 1538000, -2462000, -5659000, 28480, 949659
HAY, HA, 1521000, -4417000, 4327000, 1090, 144350
NZ, NZ, -4540000, 719000, -4409000, 16932, 225001
OVRO, OV, -2409598, -4478348, 3838607, 23788, 894355
SGO, SG, 1832000, -5034000, -3455000, 10905, 50204
[/jtable]

## Related links

[ngEHT Winter meeting challenge files (previous work)](https://drive.google.com/drive/folders/10TrAZbQUzyYQzrK7Ruzt-XCR0T31bySe?usp=sharing)

ngEHT Simulation group presentations:
[12/8/2020](https://docs.google.com/presentation/d/1nv3mRWQrk-90J-OzqOQon7R5ZbMEi5OXnxy2p9cjWrk/edit#slide=id.gb228cefa57_7_0),
[4/23/2021](https://docs.google.com/presentation/d/1fhsno3peFbO5tAXeuIVvdPpNSA_IyVYyCHqVn43Z7Hc/edit#slide=id.gd03baebd48_1_15),
[6/4/2021](https://docs.google.com/presentation/d/1dsfEtEMKXrhUgC62tT5O1xG1iqWwrZc40X3-WRslykc/edit?pli=1#slide=id.p)

