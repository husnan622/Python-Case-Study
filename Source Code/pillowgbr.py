from PIL import Image

def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)

if __name__ == '__main__':
    img = 'hydrangeas.jpg'
    watermark_photo(img, 'tekselex2.jpg', 'tekselex.jpg', position=(0,0))
