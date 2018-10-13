import argparse
import sys
import os
import numpy as np
import bmp_io_c
import math
import VRpicture
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


objects = []
h_comp = []
occlusion_distance = -1 * np.ones((4096,4096))


def __init__():
    object1 = VRpicture.VRpicture(TBA, t, image_name, edge_length_col)
    objects.append(object1)
    # init will be done here

def compute_h_comp(params):
    #compute h

def project(params):
    #project h

def check_occlusion(params):
    #return True or False


def main(argv):
    parser = argparse.ArgumentParser(description='Authroing tool')
    __init__()
    for object in objects:
        obj_params = object.some_params
        h = compute_h_comp(obj_params)
        h_comp.append(())
        project(params):
        print (type(object))



if __name__ == '__main__':
    main(sys.argv)
