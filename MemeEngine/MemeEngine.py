from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def __str__(self) -> str:
        return f"{self.output_dir}"

    def make_meme(self, in_path, out_path, body=None, author=None, width=500):
        """Create a Postcard With a Text Greeting

        in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        if width > 500:
            width = 500
        img = Image.open(in_path)
        print('Image size is: ', img.size)

        if author is None:
            author = "Unknown"

        original_width:int
        original_height: int
        original_width, original_height = img.size
        asppect_ratio: float = original_width / original_height
        # ratio = width/float(img.size[0])
        height = int(width / asppect_ratio)
        img = img.resize((width, height), Image.NEAREST)
        print('Image after resize is: ', img.size)
        if body is not None:
            draw = ImageDraw.Draw(img)
            body_font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=22)
            author_font = ImageFont.truetype('./fonts/DancingScript-Bold.ttf', size=24)
            # draw.text((10, 30), body, font=font, fill='white')
            author_name = f"-{author}"
            text_position_x: int = random.choice(range(0, int(width * 0.5)))
            text_position_y: int = random.choice(range(0, int(height * 0.75)))
            fill = (255, 255, 255)
            stroke_fill = (41, 110, 1)
            draw.text((text_position_x, text_position_y), body, font=body_font, fill=fill, stroke_fill=stroke_fill)
            draw.text((text_position_x + 20, text_position_y + 40), author_name, font=author_font, fill=fill,stroke_fill=stroke_fill)
            
        out_file = os.path.join(self.output_dir, out_path)
        print('Outfile is:', out_file)
        img.save(out_file)
        return out_file