# Import the necessary modules
import sys
sys.path.append("pixray")
import pixray

# Specify the image generation prompt here
prompt = "dark dystopian cyberpunk skyscape"

# This is where the magic happens
pixray.run(
    prompts = prompt,
    aspect = "widescreen", # widescreen, portrait, or square
    drawer = "pixel", # pixel, vqgan, clipdraw, or line_sketch
        # NOTE: You will likely be unable to use 'vqgan' on your local machine,
        # it requires a lot of VRAM.
    pixel_scale = 0.5,
    pixel_type = "rect", # rect, rectshift, hex, tri, or diamond
        # https://colab.research.google.com/github/dribnet/clipit/blob/master/demos/PixelDrawer_Init_Image.ipynb
    quality = "better", # draft, normal, better, or best
    custom_loss = "aesthetic, smoothness, palette",
        # Examples at https://replicate.com/dribnet/pixray/examples
        # Documentation at https://dazhizhong.gitbook.io/pixray-docs/docs/losses
    smoothness_weight = 4,
    palette_weight = 3,
    init_noise = "snow",
    # noise_prompt_seeds = [1,2,3],
    # init_image: "https://pbs.twimg.com/media/E9GszX4XoAo7Z2-?format=png&name=900x900",
    display_clear = True,
    scale = 3.5,
    batches = 4,
    num_cuts = 2,
    smoothness_type = "log",
    palette = "neon green->neon blue->neon pink\12; black->grey->grey blue",
        # All named colors come from https://xkcd.com/color/rgb/
        # More info here: https://dazhizhong.gitbook.io/pixray-docs/docs/image-filters#palette
)
