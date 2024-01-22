import os
import replicate


prompt = "An oil painting of a humanoid robot playing chess"


with open("../replicate_api_token.txt") as file:
    os.environ["REPLICATE_API_TOKEN"] = file.read(40)

out_url = replicate.run(
    ref="stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
    input={"prompt": prompt}
)[0]

os.system(command=f'wget -O output_text_to_image.png {out_url}')
