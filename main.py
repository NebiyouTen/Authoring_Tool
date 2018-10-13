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
"""
This lookup table contains occlusion distance at every
"""
lookupTable = -1 * np.ones((4096,4096))
blank_image  = np.zeros((3,4096,4096))
PI = math.pi


def cics_to_pics(image):
    _,row,col = image.shape
    mid_row = row//2
    mid_col = col//2
    converted_image = np.zeros_like(image)
    for i in range(row):
        for j in range(col):
            converted_image[0,i,j] = image[0,i-mid_row,j-mid_col]
            converted_image[1,i,j] = image[1,i-mid_row,j-mid_col]
            converted_image[2,i,j] = image[2,i-mid_row,j-mid_col]
    return converted_image


def __init__():
    object1 = VRpicture.VRpicture([0,0,0], [1.5,1.5,5], "beachball_5.bmp", 512)
    objects.append(object1)
    # init will be done here

def compute_h_comp(params):
    return None
    #compute h

def project(left_cor,right_cor):
    for i in range(len(left_cor)):
        x,y,z,_,R,G,B = left_cor[i,:]
        # print (x,y,z,_,R,G,B)
        r = np.sqrt(x**2+y**2+z**2)
        phi = np.arcsin(y/r)
        theta = np.arcsin(x/(r*np.cos(phi)))

        phi_deg = phi * 180 / PI
        theta_deg =  theta * 180 / PI
        lat = int( 2048 / 180 * phi_deg )
        long = int( 4096 / 180 * theta_deg )
        # print (lat,long)
        blank_image[0,lat,long] = R
        blank_image[1,lat,long] = G
        blank_image[2,lat,long] = B
        # blank_image[0,int(y),int(x)] = R
        # blank_image[1,int(y),int(x)] = G
        # blank_image[2,int(y),int(x)] = B

        # x,y,z,_,R,G,B = right_cor[i,:]
        # r = np.sqrt(x**2+y**2+z**2)
        # phi = np.arcsin(y/r)
        # theta = np.arccos(z/(r*np.cos(phi)))
        #
        # phi_deg = phi * 180 / PI
        # theta_deg =  theta * 180 / PI
        # lat = int( 1024 / 90 * phi_deg )
        # long = int( 2048 / 90 * theta_deg )
        #
        # blank_image[0,lat+2048,long] = R
        # blank_image[1,lat+2048,long] = G
        # blank_image[2,lat+2048,long] = B

        # print (x,y,z,_,R,G,B)
        # break
    return None
    #project h
   
def check_occlusion(x, y, occlusiondist):
    if lookupTable[x, y] < occlusiondist:
        lookupTable[x, y] = occlusiondist
        return True
    return False


def main(argv):
    parser = argparse.ArgumentParser(description='Authroing tool')
    __init__()
    for object in objects:
        obj_params = object.get_wc_list()
        project(obj_params,obj_params)
        print (obj_params.shape)

    bmp_io_c.output_bmp_c('outputimage.bmp',cics_to_pics(blank_image))



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


if __name__ == '__main__':
        main(sys.argv)
