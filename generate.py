
import pandas as pd
data = pd.read_csv("./labels_16k_2_Pat2.csv")

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")
# pipe.enable_attention_slicing()

prompt_list = data['title'].to_list()
img_id_list = data['img_id'].to_list()

for i in range(len(prompt_list)):
    print(f'Generating {i}th image: {prompt_list[i]}')
    prompt = prompt_list[i] + ', in traditonal Chinese ink painting'
    image = pipe(prompt).images[0]
    image.save(f"./Generated_Images/{img_id_list[i]}_g.png")
#    break
