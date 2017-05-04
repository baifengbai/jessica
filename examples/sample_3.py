from jessica import Jessica

photo = Jessica("abstract.jpg")
photo.texts = "PEACE FRIENDSHIP LOVE UNITY".split()
photo.colors = ["#" + i + "a0" for i in "B0E0E6 ADD8E6 87CEFA 87CEEB 00BFFF 1E90FF 6495ED 5F9EA0 4169E1".split()]
photo.max_font_size = 100
photo.min_font_size = 30
photo.repeat = True
photo.min_repeat = 10
photo.max_repeat = 50
photo.min_angle = 0
photo.max_angle = 0
photo.font_path = "FrancoisOne-Regular.ttf"
photo.render_and_save("output3.jpg")

photo = Jessica("output3.jpg", *"PEACE LOVE".split())
photo.max_font_size = 200
photo.min_font_size = 150
photo.min_angle = 0
photo.max_angle = 0
photo.colors = [(255, 69, 0, 150), (255, 165, 0, 150)]
photo.font_path = "FrancoisOne-Regular.ttf"

photo.render_and_save("output3.jpg")
