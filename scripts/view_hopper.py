import json
import argparse
import os

import mujoco_py
import numpy as np
from gym import spaces
from mujoco_py import load_model_from_path, MjSim, MjViewer

from HCPI.util import seeding

if __name__ == '__main__':
    desp = 'Display Robot'
    parser = argparse.ArgumentParser(description=desp)
    parser.add_argument('--robot_file', type=str,
                        default='../xml/hopper/hopper.xml')
    args = parser.parse_args()
    np.set_printoptions(precision=6, suppress=True)
    print('Displaying robot from:', os.path.abspath(args.robot_file))
    model = load_model_from_path(args.robot_file)
    sim = MjSim(model, nsubsteps=20)
    sim.reset()
    sim.step()
    viewer = MjViewer(sim)
    while True:
        ctrl = (np.random.random(3) - 0.5)*2
        sim.data.ctrl[:] = ctrl
        sim.step()
        viewer.render()
