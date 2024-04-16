from PIL import Image
import random
import os
import colorsys
from colorutils import *


size = 16


def chance(prob):
	return random.randrange(1_000_000) < prob * 1_000_000


def generate_minecraft_texture(filename):
	variation = random.randint(15, 30)

	overlay_weight = random.randint(30, 60) / 100
	chisel_weight = random.randint(30, 60) / 100

	has_overlay = chance(0.9)
	has_chisel = chance(0.2)
	is_stone_like = chance(0.4)

	# to make textures more stripy or stone-like
	change_noise_value_chance = random.randrange(30, 80)

	# only affects stone-like textures
	swap_xy = random.randrange(100) < 30

	if not has_overlay:
		overlay_weight = 0
	if not has_chisel:
		chisel_weight = 0
	if not is_stone_like:
		change_noise_value_chance = 100

	hue = random.uniform(0, 360)
	saturation = random.uniform(0.1, 0.7)
	brightness = random.uniform(0.2, 1.0)
	# hue = random.uniform(0, 360)
	# saturation = random.uniform(0.0, 0.2)
	# brightness = random.uniform(0.2, 1.0)
	color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue / 360, saturation, brightness))

	hue = random.uniform(0, 360)
	saturation = random.uniform(0.6, 1.0)
	brightness = random.uniform(0.2, 0.6)
	dark_color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue / 360, saturation, brightness))

	# Create overlay_weight blank sizexsize image
	base_image = Image.new("RGB", (size, size))

	# Fill the base image with random noise using the chosen color
	noise = 0

	for y in range(size):
		for x in range(size):
			# Generate overlay_weight random color variation based on the chosen color
			if random.randrange(100) < change_noise_value_chance:
				noise = random.randint(-variation, variation)

			# Add the noise to the base color
			pixel_color = (color[0] + noise, color[1] + noise, color[2] + noise)

			# Ensure the RGB values are within the valid range (0-255)
			pixel_color = tuple(max(0, min(255, channel)) for channel in pixel_color)

			coord = (y, x) if swap_xy else (x, y)
			base_image.putpixel(coord, pixel_color)

	overlay_file = os.path.join("overlays", random.choice(os.listdir("overlays")))
	overlay_image = Image.open(overlay_file).resize((size, size), resample=Image.NEAREST)

	chisel_file = os.path.join("chisels", random.choice(os.listdir("chisels")))
	chisel_image = Image.open(chisel_file).resize((size, size), resample=Image.NEAREST)

	# Multiply each color in the base image by the corresponding pixel in the overlay
	final_image = Image.new("RGB", (size, size))
	for y in range(size):
		for x in range(size):
			base_pixel = base_image.getpixel((x, y))
			overlay_pixel = overlay_image.getpixel((x, y))
			chisel_pixel = chisel_image.getpixel((x, y))

			overlay_pixel_scaled = scale_tuple(to_white(overlay_pixel, overlay_weight), 1/255)
			chisel_pixel_scaled = scale_tuple(to_white(chisel_pixel, chisel_weight), 1/255)

			mixed_pixel = multiply_tuples(multiply_tuples(base_pixel, overlay_pixel_scaled), chisel_pixel_scaled)

			final_image.putpixel((x, y), round_tuple(mixed_pixel))

	# Save the final image
	final_image.save(filename)


# Generate and save 100 textures
for i in range(1, 401):
	generate_minecraft_texture(f"textures/minecraft_texture{i}.png")


grid_size = 20
texture_size = size

# Create a blank square image to hold all the textures
final_image = Image.new("RGB", (grid_size * texture_size, grid_size * texture_size))

# Iterate through the textures and arrange them in the final square
for i in range(1, 401):
	# Load each texture
	texture = Image.open(f"textures/minecraft_texture{i}.png")

	# Calculate the position to paste the texture in the final image
	x = (i - 1) % grid_size * texture_size
	y = (i - 1) // grid_size * texture_size

	# Paste the texture in the final image
	final_image.paste(texture, (x, y))

final_image.save("final_minecraft_textures.png")
