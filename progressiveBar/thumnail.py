from thumbnail import generate_thumbnail

#generate_thumbnail(input, output, options)

options = {
	'trim': False,
	'height': 300,
	'width': 300,
	'quality': 85,
	'type': 'thumbnail'
}
generate_thumbnail('test.pdf', 'thumbnail.png', options)