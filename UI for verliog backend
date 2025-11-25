# 1. Install necessary libraries
!pip install -q transformers gradio torch accelerate

import gradio as gr
from transformers import pipeline
import time

# 2. Load the Model
print("Loading model, this takes a few moments.")
generator = pipeline(
    "text-generation",
    model="jmccoy7/MyGemmaVerilog5",
    device="cuda"
)

# 3. Define the Function
def generate_verilog(prompt):
    # Start the timer
    start_time = time.time()

    messages = [
        {"role": "user", "content": prompt}
    ]

    # Generate the output
    output = generator(
        messages,
        max_new_tokens=2048,
        return_full_text=False
    )

    generated_text = output[0]['generated_text']

    # Stop the timer
    end_time = time.time()
    duration = end_time - start_time
    time_message = f"Done! Generated in {duration:.2f} seconds."

    return generated_text, time_message

# 4. Start the Server
demo = gr.Interface(
    fn=generate_verilog,
    inputs=gr.Textbox(lines=5, label="Input Prompt"),
    outputs=[
        gr.Code(lines=30, label="Generated Code"),
        gr.Textbox(label="Time Taken")],

    title="Verilog Model",
    allow_flagging="never"
)

print("Starting server... Wait for the URL that ending in 'gradio.live'")
demo.launch(share=True)
