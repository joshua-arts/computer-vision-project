import cv2
import numpy as np
import math
import base64

class Encoder:
  def __init__(self, hexcode):
    self.hexcode = hexcode

    self.bar_width = 20
    self.bar_chunk_height = 52

  def encode(self):
    # The region that represents on hex character (left pad plus bar size).
    bar_region = self.bar_width * 3

    # The size of the orientation bar.
    orientation_bar = self.bar_width * 2

    # Calculating the width of the actual code, ignoring padding.
    width = orientation_bar + (len(self.hexcode) * bar_region)

    # Height of the code is ten bar chunks, ignoring padding.
    height = self.bar_chunk_height * 10

    # Initialize a fully white images of correct size.
    encoded = np.full((height, width), 255, np.uint8)

    # Draw in the orientation bar.
    encoded = cv2.rectangle(encoded, (0, 0), (orientation_bar, height), 0, -1)

    # Iterate through the self.hexcode and draw the corresponding bars.
    for i, c in enumerate(self.hexcode):
      # Find the base 16 of the character.
      v = int(c, 16)

      # Calculate the height of the bar (number of chunks).
      chunks = 9 - math.floor(v / 2)

      # Calculate the distance from the left side of the image.
      distance = orientation_bar + ((i + 1) * bar_region)

      # Determine if the bar starts from the top or the bottom, and set points.
      if v % 2 == 0:
        start = (distance - self.bar_width, 0)
        end = (distance, self.bar_chunk_height * chunks)
      else:
        start = (distance - self.bar_width, height - (self.bar_chunk_height * chunks))
        end = (distance, height)

      # Draw the bar.
      encoded = cv2.rectangle(encoded, start, end, 0, -1)

    # Add some padding to the encoded image.
    width_pad = self.bar_width * 4
    encoded = cv2.copyMakeBorder(
      encoded,
      self.bar_chunk_height, self.bar_chunk_height,
      width_pad, width_pad,
      cv2.BORDER_CONSTANT,
      value = 255)

    # Get the image into a format we can easily send over HTTP.
    _, buffer = cv2.imencode('.png', encoded)
    return buffer.tobytes()

# # Define the hex strings to encode.
# sample_self.hexcode = '0123456789abcdef'
# random_self.hexcode = '1453ad8e82da85a3'

# # The size of a single bar, scalable.
# bar_width = 20

# # The height of a 'chunk', of which the code has ten, scalable.
# bar_chunk_height = 52

# encoded_sample = encode(sample_hexcode, bar_width, bar_chunk_height)
# encoded_random = encode(random_hexcode, bar_width, bar_chunk_height)

# # Show the images.
# cv2.imshow('Encoded sample', encoded_sample)
# cv2.imshow('Encoded random', encoded_random)

# # Destroy all windows on keypress.
# cv2.waitKey(0)
# cv2.destroyAllWindows()
