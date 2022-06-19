# Import the necessary modules
import sys
sys.path.append("pixray")
import pixray

# Specify the image generation prompt here
prompt = "dystopian cyberpunk skyscape"

# This is where the magic happens
pixray.run(
    prompts = prompt,
    aspect="widescreen", # widescreen, portrait, or square
    drawer="pixel", # pixel, vqgan, clipdraw, or line_sketch
    quality="normal", # draft, normal, better, or best
    custom_loss="aesthetic",
    init_noise="snow",
    display_clear=True,
    scale=2,
    batches=4,
    num_cuts=2,
)
