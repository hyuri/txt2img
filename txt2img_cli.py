#python3
# -*- coding: utf-8 -*-

"""
By Hyuri Pimentel
"""


import argparse
from pathlib import Path

import txt2img_settings as settings
from txt2img import text_to_image


def main():
	SETTINGS = settings.settings[settings.active]

	parser = argparse.ArgumentParser(description="Generate an image out of a piece of text or text file.")

	parser.add_argument("text", type=str, help="Text or file.")
	parser.add_argument("-e", "--text_encoding", "-text_encoding", type=str, default=SETTINGS["text_encoding"], help=f"Text encoding. Default is {SETTINGS['text_encoding']}.")
	parser.add_argument("font_size", type=int, help="Font size.")
	parser.add_argument("-fg", "--text_color", "-text_color", type=str, default=SETTINGS["text_color"], help=f"Text color. Default os {SETTINGS['text_color']}.")
	parser.add_argument("-bg", "--background_color", "-background_color", type=str, default=SETTINGS["background_color"], help=f"Background color. Default is {SETTINGS['background_color']}.")
	parser.add_argument("-cm", "--color_model", "-color_model", type=str, default=SETTINGS["color_model"], help=f"Color model. Default is {SETTINGS['color_model']}.")
	parser.add_argument("-p", "--padding", "-padding", type=int, default=SETTINGS["padding"], help=f"Padding. Default is {SETTINGS['padding']}.")
	parser.add_argument("-f", "--font", "-font", type=str, default=SETTINGS["font"], help=f"Font file. Must be TrueType. Default is {SETTINGS['font']}.")
	parser.add_argument("-r", "--resize", "-resize", type=int, default=SETTINGS["resize"], help=f"Resize image width(in pixels)—height resizes proportionally. Default is {SETTINGS['resize']}.")
	parser.add_argument("output", type=str, help="Output image file.")

	args = parser.parse_args(["uga buga", "54", "text.png"])
	text_to_image(
		text=args.text,
		font_size=args.font_size,
		text_color=args.text_color,
		background_color=args.background_color,
		color_model=args.color_model,
		padding=args.padding,
		font=args.font,
		resize=args.resize,
		output=Path(args.output)
	)


if __name__ == "__main__":
	main()