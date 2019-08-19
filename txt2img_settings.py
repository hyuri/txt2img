#python3
# -*- coding: utf-8 -*-

"""
By Hyuri Pimentel
"""

import os
from pathlib import Path


fonts_folder = Path(os.path.realpath(__file__)).parent/"fonts"

# Settings
settings = {
	"default": {
		"font": fonts_folder/"Plex TrueType/IBM-Plex-Sans/IBMPlexSans-Regular.ttf",
		"color_model": "RGBA",
		"text_color": "black",
		"background_color": (0, 0, 0, 0),
		"padding": 0,
		"text_baseline": 0,
		"resize": None,
		"text_encoding": "utf-8",
		"alpha_supported": ("png", "tga", "webp", "tiff")
	}
}

active = "default"