# Authoring_Tool

### Configuring The Authoring Tool 
Before you run the main program. You might need to edit the *config.py* file, and 
change the parameters for each virtual reality(VR) object. Currently, the program supports only 3 VR objects, 
a picture, a cube and a sphere. Please note that, all the images should be in bmp format. 

"out_image_size" : (4096, 4096), 		        # Size of the output of an image in pixels
"objects": 
  "sphere":  
          "name": "VRSphere.bmp,            # Name of the sphere image
          "center": (40, 60),               # Its center in the World coordinates
          "radius": 10, 				            # in units of focal length
          "tait-bryan-angles": [0, 30, 69] 	# in degrees

      "cube": 
          # You have to put the name of all 6 images that form a cube
          "square-image-names": ["image_name_1.bmp", "image_name_2.bmp", "image_name_3.bmp", "image_name_4.bmp", "image_name_5.bmp", "image_name_6.bmp"],  
          "center": (250, 350),               # Its center in the World coordinates
          "edge-length": 10, 				          # in units of focal length
          "tait-bryan-angles": [30, 15, 50] 	# in degrees

      "picture":  {   
          "name": "VRPicture.bmp",            # Name of the picture
          "center": (600, 50), 				        # Its center in the World coordinates
          "col-edge-length": 240,	            # in units of focal length
          "tait-bryan-angles": [30, 15, 50] 	# in degrees