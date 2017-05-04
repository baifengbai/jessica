from jessica import Jessica

photo = Jessica("texture.jpg")
photo.texts = "HATE DESPAIR RAGE ANGER DESTROY BREAK SHUTUP".split()
photo.font_path = "ShadowsIntoLight.ttf"
photo.colors = ["#ff0000", "#e50000", "#cc0000", "#b20000", "#990000", "#7f0000"]
photo.max_font_size = 200
photo.min_font_size = 20
photo.repeat = True
photo.max_repeat = 3

photo.render_and_save("output2.jpg")
