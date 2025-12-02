# 1. Install necessary libraries
!pip install -q transformers gradio torch accelerate

import gradio as gr
from transformers import pipeline
import torch
import gc
import time

# --- Global Variables to track the loaded model ---
# We keep track of what is currently on the GPU so we don't reload it unnecessarily
current_model_name = None
generator = None

# List of models you want in the dropdown
MODEL_OPTIONS = [
    "Select Model....",
    "jmccoy7/VerilogPal1B",
    "jmccoy7/VerilogPal270M"
]

# 2. Helper Function: Load Model Safely
def load_model(model_name):
    global generator, current_model_name

    # If the requested model is already loaded, skip this step (saves time!)
    if generator is not None and current_model_name == model_name:
        return generator

    print(f"Switching model to {model_name}...")

    # MEMORY CLEANUP: Delete old model to free up GPU VRAM
    if generator is not None:
        del generator
        gc.collect()
        torch.cuda.empty_cache()

    # Load the new model
    generator = pipeline(
        "text-generation",
        model=model_name,
        device="cuda"
    )
    current_model_name = model_name
    return generator

# 3. Main Generation Function
def generate_verilog(model_choice, prompt):
    # Step A: Ensure the correct model is loaded
    try:
        active_generator = load_model(model_choice)
    except Exception as e:
        return f"Error loading model: {e}", "Failed"

    # Step B: Start Timer
    start_time = time.time()

    messages = [
        {"role": "user", "content": prompt}
    ]

    # Step C: Generate
    output = active_generator(
        messages,
        max_new_tokens=2048,
        return_full_text=False
    )

    generated_text = output[0]['generated_text']

    # Step D: Stop Timer
    end_time = time.time()
    duration = end_time - start_time
    time_message = f"Model: {model_choice}\nTime: {duration:.2f} seconds"

    return generated_text, time_message

# 4. Start the Server with Dropdown
demo = gr.Interface(
    fn=generate_verilog,
    inputs=[
        # NEW: The Dropdown Menu
        gr.Dropdown(
            choices=MODEL_OPTIONS,
            value=MODEL_OPTIONS[0], # Default selection
            label="Select AI Model"
        ),
        # The Prompt Box
        gr.Textbox(lines=5, label="Input Prompt")
    ],
    outputs=[
        gr.Code(lines=30, label="Generated Code"),
        gr.Textbox(label="Status & Time")
    ],
    title="VerilogPAL",
    allow_flagging="never"
)

print("Starting server... Wait for the URL that ending in 'gradio.live'")
demo.launch(share=True)
