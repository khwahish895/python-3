from PIL import Image, ImageDraw, ImageFilter
import random
import math

# Set image dimensions (width, height)
WIDTH, HEIGHT = 800, 600

# Create a blank RGB image with white background
img = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(img)

# -------------------------------------------------------
# 1. Draw a gradient background (sky-like)
# -------------------------------------------------------
for y in range(HEIGHT):
    # Interpolate between two colors (blue to light blue)
    r = int(135 + (200 - 135) * (y / HEIGHT))
    g = int(206 + (230 - 206) * (y / HEIGHT))
    b = int(235 + (255 - 235) * (y / HEIGHT))
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

# -------------------------------------------------------
# 2. Add random shapes (e.g., circles, rectangles)
# -------------------------------------------------------
for _ in range(20):
    # Random color
    color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
    
    # Random position and size
    x1 = random.randint(0, WIDTH)
    y1 = random.randint(0, HEIGHT)
    size = random.randint(20, 100)
    
    # Draw a random shape
    if random.choice([True, False]):
        draw.ellipse([x1, y1, x1 + size, y1 + size], fill=color, outline="black")
    else:
        draw.rectangle([x1, y1, x1 + size, y1 + size], fill=color, outline="black")

# -------------------------------------------------------
# 3. Generate procedural patterns (e.g., fractal-like)
# -------------------------------------------------------
for x in range(0, WIDTH, 10):
    for y in range(0, HEIGHT, 10):
        # Check if point belongs to a pattern (e.g., sine wave effect)
        n = math.sin(x * 0.05) * math.cos(y * 0.05) * 255
        if abs(n) > 50:
            draw.point((x, y), fill=(int(abs(n)), 100, 150))

# -------------------------------------------------------
# 4. Apply a blur effect (optional)
# -------------------------------------------------------
img = img.filter(ImageFilter.GaussianBlur(radius=1))

# -------------------------------------------------------
# 5. Save the image
# -------------------------------------------------------
img.save("custom_image.png")
print("Digital image created: 'custom_image.png'")

# Display the image (optional)
img.show()
