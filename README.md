# 3D printed Robotic Actuator

This robotic actuator provides high torque and speeds at a reasonable cost. It utilzes a moteus r4.11 bldc driver and a mj5208 brushless motor and has an 8:1 reduction. The components used are included in the [BOM](BOM.md). This actuator can be controlled through multiple different methods outlined in the [moteus documentation](https://github.com/mjbots/moteus), however the python files in this repo assume usage of a raspberry pi with a mjbots pi3hat r4.5. 

[Cad Overview](https://www.youtube.com/watch?v=ny0xnwEDxxo&ab_channel=OwenMcKenney)

## Specs

- Diameter: 82mm
- Width: 64mm
- ~2.5 Nm of torque

## Manufacturing & Assembly Tips

- Most components fit together intuitively as there is only one way that this actuator can be assembled. Only STL files are provided. For access to specifc source files, email owen.mckenney1@gmail.com. 
- The 3D printed components of the original implementation were printed on a Ender 3 using PLA. All components have a naturally built-in tolerance of 0.2mm; this value may not be perfect depending on the tuning of your printer. 
- The moteus r4.11 driver has 4 M2.5 mounting holes. For simplicity, this actuator uses only M3 components; in order to interface with M3 threaded inserts, these holes must be drilled out to 3mm. Drilling these holes has no percieved impact on the board.

## Setup

Before usage, the moteus r4.11 and mj5208 must be configured and calibrated per the steps outlined in the moteus documentation. Calibration must be carried out with nothing attatched to the motor. 

