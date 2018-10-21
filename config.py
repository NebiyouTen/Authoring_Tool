tool_config = {
	"out_image_size" : (4096, 4096), 		    # Size of the output of an image in pixels
	"objects": {
		"sphere":  {
            "name": "beachball_5.bmp",
            "center": (-3,-2,3),                   # Its center in the World coordinates
			"radius": 0.7, 				        # in units of focal length
            "tait-bryan-angles": [90, 0, 0] 	# in degrees
		},
        # "cube": {
        #     # You have to put the name of all 6 images that form a cube
        #     "square-image-names": ["image1.bmp", "image2.bmp", "image3.bmp", \
        #                             "image4.bmp", "image5.bmp", "image6.bmp"],
        #     "center": (0, 0,2),                   # Its center in the World coordinates
		# 	"edge-length": 1, 				    # in units of focal length
        #     "tait-bryan-angles": [35, 75, 13] 	# in degrees
		# },
		"cube1": {
            # You have to put the name of all 6 images that form a cube
            "square-image-names": ["image1.bmp", "image2.bmp", "image3.bmp", \
                                    "image4.bmp", "image5.bmp", "image6.bmp"],
            "center": (2, -10,3.5),                   # Its center in the World coordinates
			"edge-length": 1, 				    # in units of focal length
            "tait-bryan-angles": [0, 90, 0] 	# in degrees
		},
		"cube2": {
            # You have to put the name of all 6 images that form a cube
            "square-image-names": ["image1.bmp", "image2.bmp", "image3.bmp", \
                                    "image4.bmp", "image5.bmp", "image6.bmp"],
            "center": (0, 0,2.1),                   # Its center in the World coordinates
			"edge-length": 1, 				    # in units of focal length
            "tait-bryan-angles": [-30, 93, 120] 	# in degrees
		},
		"cube3": {
            # You have to put the name of all 6 images that form a cube
            "square-image-names": ["image1.bmp", "image2.bmp", "image3.bmp", \
                                    "image4.bmp", "image5.bmp", "image6.bmp"],
            "center": (0, 0,2.1),                   # Its center in the World coordinates
			"edge-length": 1, 				    # in units of focal length
            "tait-bryan-angles": [10, 20, 30] 	# in degrees
		},
        "picture":  {
            "name": "beachball_5.bmp",
			"center": (0, 0,3), 				# Its center in the World coordinates
			"col-edge-length": 3,	            # in units of focal length
            "tait-bryan-angles": [0, 0, 0] 	# in degrees
		},
		"red_square":  {
            "name": "image_test02.bmp",
			"center": (2, 2 ,2), 				# Its center in the World coordinates
			"col-edge-length": 3,	            # in units of focal length
            "tait-bryan-angles": [0, -15, 0] 	# in degrees
		},
		"red_square2":  {
            "name": "image_test01.bmp",
			"center": (0, 0 ,1), 				# Its center in the World coordinates
			"col-edge-length": 1,	            # in units of focal length
            "tait-bryan-angles": [0, -15, 0] 	# in degrees
		},
    }
}
