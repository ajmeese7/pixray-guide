# pixray-guide

<p align="center">
    <img src="./example-result.png" alt="Example result of following this guide" />
</p>

When I first tried to break into machine learning and image generation, I quickly grew very frustrated with my inability to get things configured how they needed to be due to conflicting local packages.

Once I found some documentation on another project about how to get your ML environment set up in a virtual Python install, so no package pollution or conflicting versions would be a problem, I decided to make this minimalist repository in hopes of helping others avoid that frustration and also get into machine learning.

## Usage

- Clone this repository with `git clone https://github.com/ajmeese7/pixray-guide`
- Run `bash ./setup.sh`
- Run `source .venv/bin/activate`
- Modify the prompt and/or settings in `create-image.py` to your liking
- Run `python3 create-image.py`
- Sit back and let the magic happen!

## Recommendations

I recommend using `draft` quality at first to experiment with the capabilities of your local machine, because `pixray` is a VRAM-intensive program. Google Colab is a great resource for generating production-quality images in the cloud, especially if you can afford to shell out for the Pro tier, but I am a big proponent of doing things on one's local machine whenever possible.

I have an RTX 2060 and I was able to run the program at `normal` quality on my machine with a lot of other applications running with no issue, so just know that you don't necessarily need top-of-the-line hardware to run `pixray`.

If you are just looking to get an idea of what is possible with top-notch hardware, I recommend checking out [Replicate](https://replicate.com/pixray/text2image) and running some of your prompts through their interface.

## Customization

All the options currently available for `pixray` can be found in the [official documentation](https://dazhizhong.gitbook.io/pixray-docs/docs/primary-settings).
