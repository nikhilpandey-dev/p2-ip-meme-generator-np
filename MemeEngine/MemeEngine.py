from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir
        current_dir = os.getcwd()
        final_directory = os.path.join(current_dir, fr'{output_dir}')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

    def __str__(self) -> str:
        return f"{self.output_dir}"

    def make_meme(self, img_path, body, author, width=500):
        """Create a Postcard With a Text Greeting

        in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a
             (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        if width > 500:
            width = 500
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir,
                               f"temp-{random.randint(0, 100000)}.jpg")

        original_width: int
        original_height: int
        original_width, original_height = img.size
        aspect_ratio: float = original_width / original_height
        # ratio = width/float(img.size[0])
        height = int(width / aspect_ratio)
        img = img.resize((width, height), Image.NEAREST)
        print('Image after resize is: ', img.size)

        draw = ImageDraw.Draw(img)
        body_font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                       size=22)
        author_font = ImageFont.truetype('./fonts/DancingScript-Bold.ttf',
                                         size=24)
        # draw.text((10, 30), body, font=font, fill='white')
        author_name = f"-{author}"
        text_position_x: int = random.choice(range(0, int(width * 0.5)))
        text_position_y: int = random.choice(range(0, int(height * 0.75)))
        fill = (255, 255, 255)
        stroke_fill = (41, 110, 1)
        draw.text((text_position_x, text_position_y), body, font=body_font,
                  fill=fill, stroke_fill=stroke_fill)
        draw.text((text_position_x + 20, text_position_y + 40), author_name,
                  font=author_font,
                  fill=fill, stroke_fill=stroke_fill)
        img.save(outfile, "JPEG")
        return outfile
