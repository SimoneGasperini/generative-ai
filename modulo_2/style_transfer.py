import os
import replicate


content_image = open(f"data/bologna.png", mode="rb")
style_image = open(f"data/notte_stellata.png", mode="rb")


with open("../replicate_api_token.txt") as file:
    os.environ["REPLICATE_API_TOKEN"] = file.read(40)

out_url = replicate.run(
    ref="huage001/adaattn:957250892e7125f4834c5b5e5b5b2b43dc18ff174a6d70958574d08298567a21",
    input={
        "content": content_image,
        "style": style_image
    }
)
os.system(command=f'wget -O output_style_transfer.png {out_url}')
