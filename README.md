# jessica
Generate texts on your photos!

## Who is Jessica?
Jessica will quickly generate texts on your photos, much like word clouds, with the power of Python! Something like this:

![example from wikipedia](https://upload.wikimedia.org/wikipedia/en/5/5f/Original_Doge_meme.jpg)

## Sounds cool. What do I need?
* [Python](http://python.org), of course. Not tested with Python 3, though. :stuck_out_tongue:
* [Pillow](http://pillow.readthedocs.io/). Install it with `sudo pip install pillow` if you have `pip`.

## Great. Now how do I use it?
* Cone the repository using `git clone http://github.com/naeem-hasan/jessica`.
* Move to the directory with `cd jessica`.
* Open a new Python file(E.G. `nano test.py`) and `import jessica`.
* Make a Jessica object and customize stuff! Like this:
```python
from jessica import Jessica
photo = Jessica("sample.jpg", "cute", "what a smile", "hot damn", "beautiful", "nyc lagca")
photo.repeat = True
photo.max_repeat = 10
photo.min_font_size = 30
photo.max_font_size = 80
photo.render_and_save("output.jpg")
```
This will produce a result like:

![sample](https://raw.githubusercontent.com/naeem-hasan/jessica/master/examples/output.jpg)

## Cool! Show me some other examples.
Sure! Look below.

![sample_2](https://raw.githubusercontent.com/naeem-hasan/jessica/master/examples/output2.jpg)

![sample_3](https://raw.githubusercontent.com/naeem-hasan/jessica/master/examples/output3.jpg)

Thank you! I'd love if you contributed!!
