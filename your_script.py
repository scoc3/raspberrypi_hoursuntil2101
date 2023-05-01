import datetime
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

def hours_until_2101():
    now = datetime.datetime.now()
    target_year = 2101
    target_date = datetime.datetime(target_year, 1, 1)
    time_difference = target_date - now
    
    return time_difference.total_seconds() / 3600

def main():
    inky_display = InkyPHAT("black")
    inky_display.set_border(inky_display.WHITE)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)

    message1 = "Life's Short..."
    message2 = f"There are {hours_until_2101():.2f} hours until the year 2101."

    w1, h1 = font.getsize(message1)
    w2, h2 = font.getsize(message2)

    x1 = (inky_display.WIDTH - w1) // 2
    y1 = (inky_display.HEIGHT - h1 - h2) // 2
    x2 = (inky_display.WIDTH - w2) // 2
    y2 = y1 + h1

    draw.text((x1, y1), message1, inky_display.BLACK, font)
    draw.text((x2, y2), message2, inky_display.BLACK, font)

    inky_display.set_image(img)
    inky_display.show()

if __name__ == "__main__":
    main()
