import os
import replicate


image = open("sanluca.png", mode="rb")


with open("../replicate_api_token.txt") as file:
    os.environ["REPLICATE_API_TOKEN"] = file.read(40)

output = replicate.run(
    "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
    input={
        "task": "image_captioning",
        "image": image
    }
)

print(output)
