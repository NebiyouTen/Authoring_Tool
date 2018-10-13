tool_config = {
	"out_image_size" : (4096, 4096), 		    # Size of the output of an image in pixels
	"objects": {
		"sphere":  {
            "name": "",  
            "center": (0, 0),                   # Its center in the World coordinates
			"radius": 10, 				        # in units of focal length
            "location": (23, 65), 			    # in pixels
            "tait-bryan-angles": [0, 30, 69] 	# in degrees
		}, 
        "cube": {
            # You have to put the name of all 6 images that form a cube
            "square-image-names": ["image_name_1", "image_name_2", "image_name_3", "image_name_4", "image_name_5", "image_name_6"],  
            "center": (0, 0),                   # Its center in the World coordinates
			"edge-length": 10, 				    # in units of focal length
            "location": (100, 65), 			    # in pixels
            "tait-bryan-angles": [30, 15, 50] 	# in degrees
		}, 
        "picture":  {   
            "name": "pit_at_pole",            
			"center": (50, 50), 				# Its center in the World coordinates
			"col-edge-length": (240, 240),	    # in units of focal length
            "location": (100, 65), 			    # in pixels
            "tait-bryan-angles": [30, 15, 50] 	# in degrees
		}, 
    }   
}
