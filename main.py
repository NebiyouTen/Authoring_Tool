import argparse
import sys
import os
import numpy as np
import bmp_io_c
import math
import VRpicture
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from config import tool_config


objects = []
h_comp = []
occlusion_distance = None 


def __init__():
        image_width, image_height = tool_config["out_image_size"]
        occlusion_distance = -1 * np.ones((image_width, image_height)) 

        # Init VR Picture
        picture_cfg = tool_config["objects"]["picture"]
        image_name = picture_cfg["name"]
        t = picture_cfg["center"]
        edge_length_col = picture_cfg["col-edge-length"]
        TBA = picture_cfg["tait-bryan-angles"]

        object1 = VRpicture.VRpicture(TBA, t, image_name, edge_length_col)
        objects.append(object1)
    
        # Init VR Cube 
        cube_cfg = tool_config["objects"]["cube"]
        cube_square_image_names = cube_cfg["square-image-names"]
        t = cube_cfg["center"]
        TBA = cube_cfg["tait-bryan-angles"]
        edge_length = cube_cfg["edge-length"]
     
        object2 = None
        objects.append(object2)

        # Init VR Sphere
        sphere_cfg = tool_config["objects"]["sphere"]
        sphere_name = sphere_cfg["name"]
        t = sphere_cfg["center"]
        TBA = sphere_cfg["tait-bryan-angles"]
        radius = sphere_cfg["radius"]

        objects3 = None
        objects.append(objects3)

def compute_h_comp(params):
        #compute h
        pass

def project(params):
        #project h
        pass

def check_occlusion(params):
        #return True or False
        pass


def main(argv):
        parser = argparse.ArgumentParser(description='Authoring tool')
        __init__()

        for object in objects:
                obj_params = object.some_params
                h = compute_h_comp(obj_params)
                h_comp.append(())
                project(obj_params)
                print (type(object))

if __name__ == '__main__':
        main(sys.argv)
