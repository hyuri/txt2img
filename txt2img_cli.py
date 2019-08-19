#python3
# -*- coding: utf-8 -*-

"""
By Hyuri Pimentel
"""

import argparse
from pathlib import Path

import txt2img_settings as settings
from txt2img import text_to_image


SETTINGS = settings.settings[settings.active]


def main():
	parser = argparse.ArgumentParser(description="Generates an image file from a string or text file.")

	# Add required arguments
	parser.add_argument("text", type=str, help="Text or file.")
	parser.add_argument("font_size", type=int, help=f"Font size.")
	
	# Add optional arguments
	for setting in SETTINGS:
		parser.add_argument(f"--{setting}", f"--{setting}", type=type(SETTINGS[setting]), default=SETTINGS[setting], help=f"{setting.capitalize()}. Default is {SETTINGS[setting]}.")

	# Add required argument (last)
	parser.add_argument("output", type=Path, help="Output image file.")

	# Parse args
	args = parser.parse_args()

	# Generate image, passing all parsed args
	text_to_image(**{key: value for key, value in vars(args).items()})


if __name__ == "__main__":
	main()