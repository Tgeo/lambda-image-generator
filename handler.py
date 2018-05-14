def hello(event, context):
    base64str = get_art()
    response = {
        'statusCode': 200,
        'body': base64str,
        'headers': {
            'Content-Type': 'image/png'
        },
        'isBase64Encoded': True
    }
    return response

def get_art():
    import base64
    from wand.image import Image
    from wand.drawing import Drawing
    from wand.color import Color

    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 2
        draw.fill_color = Color('white')
        draw.arc(( 25, 25),  # Stating point
                ( 75, 75),  # Ending point
                (135,-45))  # From bottom left around to top right
        with Image(width=100,
                height=100,
                background=Color('lightblue')) as img:
            draw.draw(img)
            return base64.b64encode(img.make_blob('png')).decode('utf8')