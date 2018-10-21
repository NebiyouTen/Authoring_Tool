import argparse
import sys
import os
import numpy as np
import bmp_io_c
import math
import H_builders
import VRSphere as V
import VRCube as C
import VRpicture as P
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from config import tool_config


objects = []
h_comp = []
# blank_image  = np.zeros((3,4096,4096))
"""
This lookup table contains occlusion distance at every
"""
lookupTable_left = np.Inf * np.ones((2048,4096))
lookupTable_right = np.Inf * np.ones((2048,4096))

image_left = np.zeros((3,2048,4096))
image_right = np.zeros((3,2048,4096))

PI = math.pi

def compute_h_comp():

    h_wc_left = H_builders.wb_build([0,0,0],np.array([-0.01, 0, 0]))

    h_wc_right = H_builders.wb_build([0,0,0],np.array([0.01, 0, 0]))

    return h_wc_left, h_wc_right


def check_occlusion(x, y, occlusiondist,left = True):
    # print (lookupTable_left)
    # print (x_.shape, y_.shape , occlusiondist_.shape)
    # sorted_args_ =  np.argsort(-occlusiondist)
    # x,y,occlusiondist = np.copy(x_[sorted_args_]), np.copy(y_[sorted_args_]),\
    #                     np.copy(occlusiondist_[sorted_args_])
    # lookupTable_right = lookupTable_right[x, y]
    if left:
        print (x,y)
        closer = np.zeros((len(x))).astype(bool)
        for i in range(len(x)):
            if lookupTable_left[x[i], y[i]] > occlusiondist[i]:
                closer[i] = True
                lookupTable_left[x[i], y[i]] = occlusiondist[i]

        # closer = lookupTable_left[x, y] > occlusiondist
        # closer = (closer[sorted_args_])
        # print (occlusiondist)
        # lookupTable_left[x[closer], y[closer]] = occlusiondist[closer]
        return closer#[sorted_args_]

    closer = np.zeros((len(x))).astype(bool)
    for i in range(len(x)):
        if lookupTable_right[x[i], y[i]] > occlusiondist[i]:
            closer[i] = True
            lookupTable_right[x[i], y[i]] = occlusiondist[i]
    # closer = lookupTable_right[x, y] > occlusiondist
    # closer = (closer[sorted_args_])
    # print (np.all(lookupTable_right[x_, y_]==lookupTable_right[x, y]))#,np.all(x_==x))
    # lookupTable_right[x[closer], y[closer]] = occlusiondist[closer]
    return closer#[sorted_args_]



def __init__():
        image_width, image_height = tool_config["out_image_size"]
        occlusion_distance = -1 * np.ones((image_width, image_height))

        # Init VR Picture
        picture_cfg = tool_config["objects"]["red_square"]
        image_name = picture_cfg["name"]
        t = picture_cfg["center"]
        edge_length_col = picture_cfg["col-edge-length"]
        TBA = picture_cfg["tait-bryan-angles"]

        object1 = P.VRpicture(TBA, t, image_name, edge_length_col)
        objects.append(object1)
        #
        # picture_cfg = tool_config["objects"]["red_square"]
        # image_name = picture_cfg["name"]
        # t = picture_cfg["center"]
        # edge_length_col = picture_cfg["col-edge-length"]
        # TBA = picture_cfg["tait-bryan-angles"]
        #
        # object1 = VRpicture.VRpicture(TBA, t, image_name, edge_length_col)
        # objects.append(object1)

        # picture_cfg = tool_config["objects"]["red_square2"]
        # image_name = picture_cfg["name"]
        # t = picture_cfg["center"]
        # edge_length_col = picture_cfg["col-edge-length"]
        # TBA = picture_cfg["tait-bryan-angles"]
        #
        # object1 = VRpicture.VRpicture(TBA, t, image_name, edge_length_col)
        # objects.append(object1)

        # Init VR Cube
        cube_cfg = tool_config["objects"]["cube1"]
        cube_square_image_names = cube_cfg["square-image-names"]
        t = cube_cfg["center"]
        TBA = cube_cfg["tait-bryan-angles"]
        edge_length = cube_cfg["edge-length"]
        # Init VR Sphere

        object2 = C.VRCube(TBA,t,cube_square_image_names,edge_length)
        objects.append(object2)

        # cube_cfg = tool_config["objects"]["cube2"]
        # cube_square_image_names = cube_cfg["square-image-names"]
        # t = cube_cfg["center"]
        # TBA = cube_cfg["tait-bryan-angles"]
        # edge_length = cube_cfg["edge-length"]
        # # Init VR Sphere
        #
        # object2 = C.VRCube(TBA,t,cube_square_image_names,edge_length)
        # objects.append(object2)
        #
        # cube_cfg = tool_config["objects"]["cube3"]
        # cube_square_image_names = cube_cfg["square-image-names"]
        # t = cube_cfg["center"]
        # TBA = cube_cfg["tait-bryan-angles"]
        # edge_length = cube_cfg["edge-length"]
        # Init VR Sphere

        object2 = C.VRCube(TBA,t,cube_square_image_names,edge_length)
        objects.append(object2)



        # cube_cfg = tool_config["objects"]["cube2"]
        # cube_square_image_names = cube_cfg["square-image-names"]
        # t = cube_cfg["center"]
        # TBA = cube_cfg["tait-bryan-angles"]
        # edge_length = cube_cfg["edge-length"]
        #
        # object2 = C.VRCube(TBA,t,cube_square_image_names,edge_length)
        # objects.append(object2)
        #
        sphere_cfg = tool_config["objects"]["sphere"]
        sphere_name = sphere_cfg["name"]
        t = sphere_cfg["center"]
        TBA = sphere_cfg["tait-bryan-angles"]
        radius = sphere_cfg["radius"]

        objects3 = V.VRSphere(TBA,t,sphere_name,radius)
        objects.append(objects3)

# def project(left_cor,right_cor):
def project(cor,image,left=True):
    # for i in range(len(left_cor)):
    x,y,z,_,R,G,B = cor[:,0],cor[:,1],cor[:,2],\
                    cor[:,3],cor[:,4],cor[:,5],cor[:,6]
    x,y,z = x/_,y/_,z/_
    # print (x,y,z,_)
    r = np.sqrt(x**2+y**2+z**2)
    phi = np.arcsin(y/r)

    temp = z / (r*np.cos(phi))
    temp[temp>1] = 1
    # temp[temp<-1] = -1
    theta = np.arccos( temp)

    phi_deg = phi * 180 / PI
    theta_deg =  theta * 180 / PI
    theta_deg[x<0] = -theta_deg[x<0]

    lat = ( 2048 / 180 * phi_deg ).astype(int)
    long = ( 2048 / 180 * theta_deg ).astype(int)
    updates = check_occlusion(lat,long,r,left)
    image[:,lat[updates]+1023,long[updates]+2047] = [R[updates],G[updates],B[updates]]

def main(argv):
    parser = argparse.ArgumentParser(description='Authroing tool')
    __init__()
    for object in objects:
        obj_wc_list = object.get_wc_list()
        h_wc_left, h_wc_right = compute_h_comp()

        cam_cord_left = np.copy(obj_wc_list)
        cam_cord_left[:,:4] = h_wc_left.dot(cam_cord_left[:,:4].T).T

        cam_cord_right = np.copy(obj_wc_list)
        cam_cord_right[:,:4] = h_wc_right.dot(cam_cord_right[:,:4].T).T
        project(cam_cord_right,image_right,left=False)
        project(cam_cord_left,image_left)


    print("Image processing is done. Now Writing image to file ")
    blank_image = np.concatenate((image_left,image_right),1)
    bmp_io_c.output_bmp_c('Picture2.bmp',(blank_image))

if __name__ == '__main__':
        main(sys.argv)
