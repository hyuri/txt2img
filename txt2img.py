#python3
# -*- coding: utf-8 -*-

"""
txt2img(Text-To-Image) — Generates an image file from a string or text file.
Configurable: Font, Font Size, Text Color, Background Color, Color Model, Padding, Image Size(resizing).
Image format of your choice.
(i) Ignores alpha channel for formats that do not support it.

TODO:
(!) Args/Value checking still needs to be written.

By Hyuri Pimentel
"""


from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import txt2img_settings as settings


SETTINGS = settings.settings[settings.active]


def text_to_image(text, font_size, output, **optional_settings):
	"""
	Generates an image file from a string or text file.
	
	Required args:, text, font_size, output
	Optional args: font, color_model, text_color, background_color, padding, resize

	Default settings:
		font = "IBMPlexSans-Regular.ttf"
		color_model = "RGBA"
		text_color = "black"
		background_color = (0, 0, 0, 0) # fully transparent
		padding = 0
		resize = None
		text_encoding = "utf-8"
	"""
	
	# Replace default SETTINGS with passed SETTINGS
	for key in optional_settings:
		if key not in SETTINGS:
			raise KeyError(f"{key} is not a recognized setting.")

		SETTINGS[key] = optional_settings[key]

	# If user asks for a format that does not support an alpha channel,
	# ignore alpha channel, and change color model to RGB
	if output.suffix.lower().strip(".") not in SETTINGS["alpha_supported"]:
		if SETTINGS["color_model"] == "RGBA":
			SETTINGS["color_model"] = "RGB"
			print(f"(i) Alpha channel has been ignored for {output.suffix}. Using RGB instead.")
	
	font = ImageFont.truetype(SETTINGS["font"] if type(SETTINGS["font"]) == str else str(SETTINGS["font"].resolve()), font_size)

	# If passed text is a file, replace text with that file's text
	lines_count = 1
	longest_line = text
	try:
		text = Path(text).read_text(encoding=SETTINGS["text_encoding"])
		lines = text.split("\n")
		lines_count = len(lines)
		longest_line = max(lines, key=lambda line: font.getsize(line)[0])
	except FileNotFoundError:
		pass

	# Get an image size that accommodates text set to font size
	image_size = (font.getsize(longest_line)[0] + SETTINGS["padding"], (font.getsize(longest_line)[1] * lines_count) + SETTINGS["padding"])
	img = Image.new(SETTINGS["color_model"], image_size, color=SETTINGS["background_color"])

	# Create drawing and write given text
	drawing = ImageDraw.Draw(img)
	drawing.text(text=text, font=font, fill=SETTINGS["text_color"], xy=(int(SETTINGS["padding"]/2), int(SETTINGS["padding"]/2)))

	# If resize provided, resize width to given value(Height is resized proportionally)
	if SETTINGS["resize"]:
		img = img.resize((SETTINGS["resize"], int((image_size[1]/image_size[0]) * SETTINGS["resize"])), Image.LANCZOS)

	# Save image to disk
	img.save(str(output.resolve()))