import imageio.v3 as iio

filenames = ['lazy-bella-1.dng', 'lazy-bella-2.dng', 'lazy-bella-3.dng', 'lazy-bella-4.dng']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('lazy-bella.gif', images, duration = 50, loop = 0)