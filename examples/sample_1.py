from jessica import Jessica

photo = Jessica("sample.jpg", "cute", "what a smile", "hot damn", "beautiful", "nyc lagca")
photo.repeat = True
photo.max_repeat = 10
photo.min_font_size = 30
photo.max_font_size = 80
photo.render_and_save("output.jpg")
