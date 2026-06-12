# 100 µm × 100 µm Tritiated-Graphene Source for Tritium Endpoint Mass Measurement

This note is only about an **ordinary tritium beta-decay endpoint neutrino-mass measurement**. It is **not** about relic-neutrino capture.

The concept considered here is a small pixelated source/detector geometry:

- Source patch size: **100 µm × 100 µm**
- Source material: **two tritiated graphene monolayers**
- Tritium areal density per monolayer: approximately  
  \[
  n_T \approx 5\times 10^{14}\ \mathrm{T/cm^2}
  \]
  representative of demonstrated partial tritiation, not ideal full graphane coverage.
- Tritium atoms per pixel:
  \[
  N_T \approx 2\,(100\ \mu\mathrm{m})^2\,n_T
  \]
  Since
  \[
  100\ \mu\mathrm{m}=10^{-2}\ \mathrm{cm},
  \]
  the area is
  \[
  A_{\rm pix}=10^{-4}\ \mathrm{cm^2}.
  \]
  Therefore
  \[
  N_T \approx 2\times 10^{-4}\times5\times10^{14}
  \approx 10^{11}\ \mathrm{T\ atoms/pixel}.
  \]

Using the tritium half-life

\[
t_{1/2}\approx 12.32\ \mathrm{yr},
\]

the activity per pixel is

\[
A=\frac{\ln2}{t_{1/2}}N_T\approx178\ \mathrm{Bq}.
\]

So each pixel produces roughly

\[
\boxed{A\approx180\ \mathrm{decays/s}}
\]

before angular, voltage, scattering, detector, and analysis-window cuts.

---

## Endpoint spectrum model

Near the endpoint, a simple allowed-beta approximation is adequate for a first statistical model:

\[
\frac{dN}{dK}\propto w\sqrt{w^2-m_\nu^2},
\]

where

\[
w=E_0-K,
\]

\(K\) is the electron kinetic energy, and

\[
E_0\approx18.6\ \mathrm{keV}
\]

is the tritium beta endpoint for a massless neutrino.

For \(m_\nu=0\), this becomes

\[
\frac{dN}{dK}\propto (E_0-K)^2.
\]

The approximate fraction of all decays falling within the last \(\Delta E\) below the endpoint is

\[
f(\Delta E)\approx\left(\frac{\Delta E}{E_0}\right)^3.
\]

This cubic endpoint suppression is the main reason the required detector-years are large even though the total pixel activity is about 180 Bq.

---

## Blocking-voltage acceptance

Assume a retarding voltage blocks low-energy electrons. An electron with kinetic energy \(K\) and emission angle \(\theta\), measured relative to the direction up the retarding-potential gradient, passes if

\[
K\cos^2\theta > eV_{\rm block}.
\]

Equivalently,

\[
\theta < \theta_{\max}=\cos^{-1}\sqrt{\frac{eV_{\rm block}}{K}}.
\]

For endpoint electrons and a blocking voltage equal to half the endpoint energy,

\[
eV_{\rm block}=0.5E_0,
\]

so

\[
\theta_{\max}=\cos^{-1}\sqrt{0.5}=45^\circ.
\]

For isotropic emission into the upward hemisphere, the accepted fraction of the upward hemisphere is

\[
f_{\rm angle|up}=1-\cos45^\circ\approx0.293.
\]

Because only the upward hemisphere is assumed to escape toward the detector, the total accepted fraction of all decays is

\[
f_{\rm angular,total}=\frac{1}{2}(1-
\cos45^\circ)\approx0.146.
\]

Thus the 0.5-endpoint blocking voltage increases the required exposure by

\[
\frac{1}{0.146}\approx6.83
\]

relative to a hypothetical calculation using total activity with no angular loss.

---

## Effective energy resolution including zero-point motion

The tritium bound to graphene has intrinsic zero-point motion. The paper **“Navigating the pitfalls of relic neutrino detection”** estimates that localization of tritium on graphene can introduce an intrinsic electron-energy broadening of roughly

\[
\Delta E_{\rm zp}\sim0.3\text{–}0.7\ \mathrm{eV}.
\]

For a first statistical Monte Carlo, this can be treated as an additional known Gaussian resolution term. If the detector energy resolution and zero-point-motion broadening are both approximated as Gaussian FWHM values, use

\[
\mathrm{FWHM}_{\rm eff}^2
=
\mathrm{FWHM}_{\rm det}^2+
\mathrm{FWHM}_{\rm zp}^2.
\]

Or, in standard deviations,

\[
\sigma_{\rm eff}^2=\sigma_{\rm det}^2+\sigma_{\rm zp}^2,
\]

with

\[
\sigma=\frac{\mathrm{FWHM}}{2.355}.
\]

Example: if

\[
\mathrm{FWHM}_{\rm det}=0.1\ \mathrm{eV}
\]

and

\[
\mathrm{FWHM}_{\rm zp}=0.5\ \mathrm{eV},
\]

then

\[
\mathrm{FWHM}_{\rm eff}\approx\sqrt{0.1^2+0.5^2}=0.51\ \mathrm{eV}.
\]

For a first-pass statistical forecast, treating zero-point motion this way is reasonable. For a more serious model, the Gaussian should be replaced by a source-specific final-state / momentum-distribution response function.

---

## 1σ calendar-time table with upward hemisphere and 0.5 endpoint blocking voltage

These estimates use the previous toy counting model for distinguishing

\[
m_\nu=0
\]

from

\[
m_\nu=100\ \mathrm{meV}
\]

at **1σ**, using counts in a narrow endpoint window.

The statistical criterion is

\[
\frac{N_0-N_m}{\sqrt{N_0}}=1,
\]

where \(N_0\) is the expected number of detected events in the chosen endpoint window for \(m_\nu=0\), and \(N_m\) is the expected number for \(m_\nu=100\ \mathrm{meV}\).

The table includes:

- total tritium activity per pixel: \(A\approx180\ \mathrm{Bq}\),
- upward hemisphere only,
- 0.5-endpoint retarding-voltage angular acceptance,
- ideal beta endpoint shape,
- no scattering loss,
- no dead time,
- no background,
- no uncertainty in the endpoint energy,
- no systematic uncertainty in the response function.

| Pixels | 1 eV window | 0.5 eV window | 0.2 eV window | 0.1 eV window | 0.05 eV window |
|---:|---:|---:|---:|---:|---:|
| \(10^3\) | 35,000 yr | 18,000 yr | 8,200 yr | 7,500 yr | 62,000 yr |
| \(10^4\) | 3,500 yr | 1,800 yr | 820 yr | 750 yr | 6,200 yr |
| \(10^5\) | 350 yr | 180 yr | 82 yr | 75 yr | 620 yr |
| \(10^6\) | 35 yr | 18 yr | 8.2 yr | 7.5 yr | 62 yr |
| \(10^7\) | 3.5 yr | 1.8 yr | 0.82 yr | 0.75 yr | 6.2 yr |
| \(10^8\) | 0.35 yr | 0.18 yr | 0.082 yr | 0.075 yr | 0.62 yr |

The rough optimum in this simplified counting model is around a 0.1–0.2 eV endpoint window. However, once the effective resolution is dominated by a 0.3–0.7 eV zero-point-motion broadening, windows narrower than that are no longer independent clean spectral regions. A Monte Carlo or likelihood model should therefore include the resolution convolution directly instead of relying only on this window-counting table.

---

## Monte Carlo simulation needed

A simple Monte Carlo can be used to estimate statistical sensitivity to neutrino mass. The purpose is to model the measured spectrum near the endpoint, including the retarding-voltage angular acceptance and effective energy resolution.

### Inputs

Recommended first-pass parameters:

| Parameter | Symbol | Example value |
|---|---:|---:|
| Tritium atoms per pixel | \(N_T\) | \(10^{11}\) |
| Activity per pixel | \(A\) | 178 Bq |
| Endpoint energy | \(E_0\) | 18.6 keV |
| Blocking voltage | \(eV_{\rm block}\) | \(0.5E_0\) |
| Pixel count | \(N_{\rm pix}\) | variable |
| Live time | \(t\) | variable |
| Detector FWHM | \(\Delta E_{\rm det}\) | e.g. 0.05–0.2 eV |
| Zero-point-motion FWHM | \(\Delta E_{\rm zp}\) | 0.3–0.7 eV |
| Effective FWHM | \(\Delta E_{\rm eff}\) | quadrature sum |
| Test neutrino mass | \(m_\nu\) | 0, 0.05, 0.1 eV |

### Event generation

For each generated decay:

1. Draw whether the electron is emitted into the upward hemisphere.  
   In a simple model, keep half the decays.

2. Draw the emission direction in the upward hemisphere.  
   Use
   \[
   \cos\theta\sim U(0,1).
   \]

3. Draw the true electron kinetic energy \(K\) from the endpoint beta spectrum:
   \[
   \frac{dN}{dK}\propto w\sqrt{w^2-m_\nu^2},
   \qquad w=E_0-K.
   \]

4. Apply the retarding-voltage cut:
   \[
   K\cos^2\theta > eV_{\rm block}.
   \]
   If this condition fails, reject the event.

5. Smear the detected energy:
   \[
   K_{\rm meas}=K+\mathcal{N}(0,\sigma_{\rm eff}).
   \]

6. Fill a histogram or unbinned likelihood dataset near the endpoint.

### Efficient sampling

It is inefficient to simulate all beta decays from zero to 18.6 keV. Instead, simulate only a window near the endpoint, for example the last 5–10 eV, and weight the generated sample by

\[
f(\Delta E_{\rm sim})\approx\left(\frac{\Delta E_{\rm sim}}{E_0}\right)^3.
\]

The total expected number of decays generated in the simulated endpoint region is

\[
N_{\rm sim-region}
=
A\,N_{\rm pix}\,t\,
\left(\frac{\Delta E_{\rm sim}}{E_0}\right)^3.
\]

Then apply upward-hemisphere, angular, voltage, and resolution effects inside the simulation.

### Fitting / sensitivity estimation

A better approach than a single endpoint-window count is to fit the spectrum using a binned or unbinned likelihood.

For a binned likelihood:

\[
\ln L(m_\nu^2,E_0,A,b,\ldots)
=
\sum_i
\left[n_i\ln\mu_i-\mu_i-\ln(n_i!)\right],
\]

where:

- \(n_i\) is the observed count in energy bin \(i\),
- \(\mu_i\) is the predicted count after applying the beta spectrum, angular acceptance, retarding-voltage cut, and resolution convolution,
- nuisance parameters may include endpoint energy \(E_0\), normalization, background, and resolution.

The statistical sensitivity can be estimated by repeated pseudoexperiments:

1. Generate pseudo-data with an assumed true \(m_\nu\).
2. Fit each pseudoexperiment for \(m_\nu^2\).
3. Extract the distribution of fitted \(m_\nu^2\).
4. Quote the 1σ statistical uncertainty from the spread.

Alternatively, use an Asimov dataset: generate the expected spectrum without Poisson fluctuations and compute the curvature of \(\ln L\) near the best-fit mass.

---

## Important limitations

This Monte Carlo would be a useful first statistical model, but it would still be optimistic because it treats the zero-point-motion effect as a known Gaussian broadening. A real tritiated-graphene source may produce a non-Gaussian spectral response due to bound-state momentum distributions, final-state excitations, helium/graphene interactions, phonons, and electronic excitations.

For a mass measurement, the source-response function does not have to be zero. But it must be known well enough that it does not mimic the endpoint distortion caused by nonzero \(m_\nu\). That is likely the central systematic issue for a tritiated-graphene endpoint-mass experiment.

---

## References

1. S. Betts et al., **“Development of a Relic Neutrino Detection Experiment at PTOLEMY: Princeton Tritium Observatory for Light, Early-Universe, Massive-Neutrino Yield,”** arXiv:1307.4738v2, 2013.
2. Y. Cheipesh, V. Cheianov, and A. Boyarsky, **“Navigating the pitfalls of relic neutrino detection,”** *Physical Review D* **104**, 116004, 2021. DOI: 10.1103/PhysRevD.104.116004.
3. PTOLEMY Collaboration, A. Apponi et al., **“Heisenberg’s uncertainty principle in the PTOLEMY project: A theory update,”** *Physical Review D* **106**, 053002, 2022. DOI: 10.1103/PhysRevD.106.053002.
