from PIL import Image, ImageDraw, ImageFont
from typing import Tuple
import os
import random


class MemeEngine:

    def __init__(self, output_dir: str) -> None:
        self.outout_dir = output_dir
        self.img_num = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path: str, text: str,
                  author: str, width: int = 500) -> str:
        img: Image = Image.open(img_path)
        original_width: int
        original_height: int
        original_width, original_height = img.size
        # Compute the aspect ratio, which is width / height
        aspect_ratio: float = original_width / original_height
        """Get the new height, so that the image
         remains proportional in both the cases.
        """
        new_height: int = int(width / aspect_ratio)
        # Resize image to the new width and height
        """I have used thumbnail as Image. thumbnail resizes to the largest
         size that (a) preserves the aspect ratio,
          (b) does not exceed the original image,
          and (c) does not exceed the size specified
           in the arguments of thumbnail.
        The below lines of code are inspired from the
         following stackoverflow post:
        https://stackoverflow.com/questions/29367990/what-is-the-difference-between-image-resize-and-image-thumbnail-in-pillow-python
        and the answer I've chosen is:
        https://stackoverflow.com/a/65506534
        """
        max_size: Tuple[int, int] = (width, new_height)
        img = img.thumbnail(max_size)
        # declare font
        body_font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                       size=20)
        author_font = ImageFont.truetype('./fonts/Merriweather-Regular.ttf',
                                         size=18)
        # Make random location for writing text
        """Subtracting text length so as to ensure that
         the text is inside the picture.
        """
        random_width = random.choice(0, width - 30)
        """ Accounting for the height, here since height also needs
         to accomodate for the author, so the subtractions
          would be higher than that for the width.
        """
        random_height = random.choice(0, new_height - 50)
        # Select color and stroke_fill
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)
        # draw the text on image
        draw: ImageDraw = ImageDraw.Draw(img)
        # Write quote
        draw.text((random_width, random_height), text, fill, body_font,
                  stroke_width=1, stroke_fill=stroke_fill)
        # Write author name
        draw.text((random_width + 16, random_height + 32), f'- {author}',
                  fill, author_font, stroke_width=1, stroke_fill=stroke_fill)
        # Crete out_path
        out_img_name = f"dog_img_{self.img_num}.jpg"
        out_path = os.path.join(self.outout_dir, out_img_name)
        img.save(out_path)
        return out_path
