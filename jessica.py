from PIL import ImageDraw, ImageFont, Image
from random import choice, randint
from os.path import realpath, dirname, join


class Jessica(object):
    COLORS = ["#FF0000", "#FF4500", "#00EE00", "#00BFFF", "#FF1493", "#DC143C"]
    MAX_F_SIZE = 40
    MIN_F_SIZE = 8
    DEFAULT_FONT = "DroidSans.ttf"
    MIN_ANGLE = -30
    MAX_ANGLE = 30
    MAX_REPEAT = 5
    MIN_REPEAT = 1
    REPEAT = False

    def __init__(self, file_name, *texts):
        self.main_copy = Image.open(file_name)
        self.texts = texts

        self.max_font_size = Jessica.MAX_F_SIZE
        self.min_font_size = Jessica.MIN_F_SIZE
        self.max_angle = Jessica.MAX_ANGLE
        self.min_angle = Jessica.MIN_ANGLE
        self.colors = Jessica.COLORS
        self.repeat = Jessica.REPEAT
        self.max_repeat = Jessica.MAX_REPEAT
        self.min_repeat = Jessica.MIN_REPEAT
        self.font_path = join(dirname(realpath(__file__)), Jessica.DEFAULT_FONT)

        self.width, self.height = self.main_copy.size

    def place_text(self, text):
        font = ImageFont.truetype(self.font_path, size=randint(self.min_font_size, self.max_font_size))
        text_image = Image.new('RGBA', font.getsize(text))
        draw_text = ImageDraw.ImageDraw(text_image)
        draw_text.text((0, 0), text, font=font, fill=choice(self.colors))
        text_image = text_image.rotate(randint(self.min_angle, self.max_angle), expand=1)

        w, h = text_image.size
        point = (randint(0, self.width - w), randint(0, self.height - h))
        self.image.paste(text_image, point, text_image)

    def render_image(self):
        self.image = self.main_copy
        for text in self.texts:
            if self.repeat:
                for _ in range(randint(self.min_repeat, self.max_repeat)):
                    self.place_text(text)
            else:
                self.place_text(text)

        return self.image

    def render_and_save(self, file_name):
        self.render_image().save(file_name)
