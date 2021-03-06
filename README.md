# kineticstoolkit_pushrimkinetics

Provide functions to process kinetic data from instrumented wheelchair wheels such as the SmartWheel, pictured below.

![SmartWheel](SmartWheel.jpg)

The functions provided by this extension are:

- `read_smartwheel(filename)`: Read a file generated by the SmartWheel instrumented wheel.
- `apply_calibration(ts, gains, offsets, *, transducer, reference_frame)`: Calculate pushrim forces and moments based on raw channel values.
- `remove_offsets(ts, baseline_kinetics)`: Remove dynamic offsets in forces and moments.
- `calculate_velocity(ts)`: Calculate velocity based on wheel angle.
- `calculate_power(ts)`: Calculate power based on wheel velocity and moment.

This extension replaces the former `ktk.pushrimkinetics` module that is now being deprecated.

## Installing

```
pip install git+https://github.com/felixchenier/kineticstoolkit_pushrimkinetics
```

## Uninstalling

```
pip uninstall kineticstoolkit_pushrimkinetics
```

## How to use this extension

Please refer to [this tutorial](tutorials/tutorial.ipynb) to see the extension in action.
