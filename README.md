# Tritiated Graphene Endpoint Simulator

This is a modified version of the neighboring Monte Carlo GUI for the
tritiated-graphene tritium endpoint experiment described in
`tritium_graphene_mass_measurement_mc.md`.

Run the GUI:

```powershell
python run_gui.py
```

The GUI keeps the same four-panel workflow as the original simulator:

- full spectrum preview;
- accumulated binned counts;
- fit diagnostic;
- sensitivity history.

The full-spectrum preview includes an orange reference pileup curve computed
with `tau_eff = 0.5 ms`, independent of the run's current pileup setting. This
is meant as an unfiltered-pileup comparison curve.

Tritium-specific inputs include:

- endpoint energy, default `18600 eV`;
- blocking voltage fraction of the endpoint, default `0.51`, giving a
  two-electron pileup threshold near `1.02 E0`;
- detector energy resolution FWHM;
- zero-point-motion FWHM;
- pixel count and activity per pixel;
- optional pileup resolving time.

The model uses the allowed tritium beta endpoint shape, isotropic emission into
the upward hemisphere, the retarding-voltage angular cut
`K cos^2(theta) > f_block E0`, source zero-point broadening before the
potential cut, and detector Gaussian smearing after the potential cut. The GUI
also reports the equivalent endpoint voltage `f_block * E0`.

The default fit method is `robust_mle` and the default energy grid is `65536`
points. `linearized` is available in the GUI dropdown for faster interactive
checks.
