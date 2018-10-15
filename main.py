import argparse
import sys
import os
import numpy as np
import bmp_io_c
import math
import h_builders
import VRpicture
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from config import tool_config


objects = []
h_comp = []
occlusion_distance = -1 * np.ones((4096,4096))
# blank_image  = np.zeros((3,4096,4096))
"""
This lookup table contains occlusion distance at every
"""
lookupTable = -1 * np.ones((4096,4096))
blank_image  = np.zeros((3,4096,4096))
PI = math.pi


image_left = np.zeros((3,2048,4096))
image_right = np.zeros((3,2048,4096))

PI = math.pi

def compute_h_comp(params):
    
    #converting from body to world coordinates
    #h_bw = h_builders.wb_build(TBA,t)
    
    #converting from the world to left  camera coordinates 
    h_wcl = h_builders.wb_build((0,0,0),(-0.25, 0, 0))
    
    #converting from the world to left  camera coordinates 
    h_wcr = h_builders.wb_build((0,0,0),(0.25, 0, 0))
    
    #composite hmatrix
    #h_comp = h_wc.dot(h_bw) 
    
    return h_wcl, h_wcr

   
def check_occlusion(x, y, occlusiondist):
    if lookupTable[x, y] < occlusiondist:
        lookupTable[x, y] = occlusiondist
        return True
    return False

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

def project(left_cor,right_cor):
    for i in range(len(left_cor)):
        x,y,z,_,R,G,B = left_cor[i,:]
        x,y,z = x/_,y/_,z/_
        r = np.sqrt(x**2+y**2+z**2)
        phi = np.arcsin(y/r)
        theta = np.arcsin(x/(r*np.cos(phi)))
        phi_deg = phi * 180 / PI
        theta_deg =  theta * 180 / PI
        if np.isnan(phi_deg) :
            lat = 0
        else:
            lat = int( 2048 / 180 * phi_deg )
        if np.isnan(theta_deg):
            long = 0
        else:
            long = int( 4096 / 180 * theta_deg )

        # Check occulusion here
        image_left[:,lat+1024,long+2048] = [R,G,B]
        image_right[:,lat+1024,long+2048] = [R,G,B]
    return

def main(argv):
    parser = argparse.ArgumentParser(description='Authroing tool')
    __init__()
    for object in objects:
        obj_params = object.get_wc_list()
        # Call and get HComp Here
        project(obj_params,obj_params)
        image_left = np.zeros((3,2048,4096))
        image_right = np.zeros((3,2048,4096))

    blank_image = np.concatenate((image_left,image_right),1)
    bmp_io_c.output_bmp_c('outputimage'+str(i)+'.bmp',(blank_image))

if __name__ == '__main__':
        main(sys.argv)
