tool_config = {
	"out_image_size" : (4096, 4096), 		    # Size of the output of an image in pixels
	"objects": {
		"sphere":  {
            "name": "",  
            "center": (0, 0),                   # Its center in the World coordinates
			"radius": 10, 				        # in units of focal length
			"size": (128, 128),			        # in pixels
            "location": (23, 65), 			    # in pixels
            "tait-bryan-angles": [0, 30, 69] 	# in degrees
		}, 
        "cube":  {
            "name": "",  
            "center": (0, 0),                   # Its center in the World coordinates
			"length": 10, 				        # in units of focal length
			"size": (460, 460),			        # in pixels
            "location": (100, 65), 			    # in pixels
            "tait-bryan-angles": [30, 15, 50] 	# in degrees
		}, 
        "picture":  {   
            "name": "pit_at_pole",            
			"center": (50, 50), 				# Its center in the World coordinates
			"size": (240, 240),			        # in pixels
            "location": (100, 65), 			    # in pixels
            "tait-bryan-angles": [30, 15, 50] 	# in degrees
		}, 
    }   
}
