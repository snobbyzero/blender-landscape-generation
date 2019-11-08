import sys
path = "C:/Users/user/PycharmProjects/blender_test"
if path not in sys.path:
    sys.path.append(path)
filename1 = "C:/Users/user/PycharmProjects/blender_test/noise_image.py"
filename2 = "C:/Users/user/PycharmProjects/blender_test/blender_script.py"
exec(compile(open(filename1).read(), filename1, 'exec'))
exec(compile(open(filename2).read(), filename2, 'exec'))
