tool_config = {
	"out_image_size" : (4096, 4096), 		    # Size of the output of an image in pixels
	"objects": {
		"sphere":  {
            "name": "VRSphere.bmp",
            "center": (40, 60),                   # Its center in the World coordinates
			"radius": 10, 				        # in units of focal length
            "tait-bryan-angles": [0, 30, 69] 	# in degrees
		},
        "cube": {
            # You have to put the name of all 6 images that form a cube
            "square-image-names": ["image_name_1.bmp", "image_name_2.bmp", "image_name_3.bmp", \
                                    "image_name_4.bmp", "image_name_5.bmp", "image_name_6.bmp"],
            "center": (250, 350),                   # Its center in the World coordinates
			"edge-length": 10, 				    # in units of focal length
            "tait-bryan-angles": [30, 15, 50] 	# in degrees
		},
        "picture":  {
            "name": "beachball_5.bmp",
			"center": (0, 2,2), 				# Its center in the World coordinates
			"col-edge-length": 3,	            # in units of focal length
            "tait-bryan-angles": [0, 0, 45] 	# in degrees
		},

		"red_square":  {
            "name": "image_test02.bmp",
			"center": (0, 3 ,3), 				# Its center in the World coordinates
			"col-edge-length": 5,	            # in units of focal length
            "tait-bryan-angles": [0, 0, -70] 	# in degrees
		},

		"red_square2":  {
            "name": "image_test01.bmp",
			"center": (0, 0 ,1), 				# Its center in the World coordinates
			"col-edge-length": 1,	            # in units of focal length
            "tait-bryan-angles": [0, -15, 0] 	# in degrees

		},
    }
}
