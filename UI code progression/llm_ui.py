import tkinter as tk
from tkinter import ttk, scrolledtext, font
import time
import threading

# MOCK LLM FUNCTION 
def generate_code_from_llm(prompt: str) -> str:
    """
    placeholder function to sudo-call to a local LLM.
    returns pre-defined code based on keywords.
    """
    print(f"LLM received prompt: '{prompt[:30]}...'")
# sudo-network/processing delay
    time.sleep(3)

# prewritten logic to return different code snippets
    prompt_lower = prompt.lower()
    if "vhdl" in prompt_lower and "adder" in prompt_lower:
        return """-- 4-bit full adder in VHDL
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity full_adder_4bit is
    Port ( a : in STD_LOGIC_VECTOR (3 downto 0);
           b : in STD_LOGIC_VECTOR (3 downto 0);
           cin : in STD_LOGIC;
           sum : out STD_LOGIC_VECTOR (3 downto 0);
           cout : out STD_LOGIC);
end full_adder_4bit;

architecture Behavioral of full_adder_4bit is
    signal temp_sum : unsigned(4 downto 0);
begin
    temp_sum <= unsigned('0' & a) + unsigned('0' & b) + unsigned'("0000" & cin);
    sum <= std_logic_vector(temp_sum(3 downto 0));
    cout <= temp_sum(4);
end Behavioral;
"""
    elif "verilog" in prompt_lower and "flip-flop" in prompt_lower:
        return """// D-type Flip-Flop with asynchronous reset in Verilog
module d_ff_reset (
    input wire clk,
    input wire reset,
    input wire d,
    output reg q
);

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            q <= 1'b0;
        end else begin
            q <= d;
        end
    end

endmodule
"""
    else:
        return "This funtionality coming soon!"

def run_llm_in_thread(prompt):
    """Runs the LLM function in a separate thread and schedules the UI update."""
    # It gets the result from the LLM function.
    generated_code = generate_code_from_llm(prompt)
    # `root.after` schedules a function to be called in the main thread.
    root.after(0, update_output_box, generated_code)

def update_output_box(code):
    """Clears the output box and inserts the new code. Re-enables the button."""
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", code)
    output_text.config(state="disabled") # Make it read-only again
    
    generate_button.config(state="normal") # Re-enable the button

# UI EVENT HANDLER
def handle_generate_click():
    """Handles the 'Generate' button click event."""
    # Get the prompt from the input box
    prompt = input_text.get("1.0", tk.END).strip()
    if not prompt:
        return
    # Disable the button to prevent multiple clicks
    generate_button.config(state="disabled")
    
    # Show a "working" message in the output box
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", "🌀 Generating code, please wait...")
    output_text.config(state="disabled")
    
    # Start the LLM call in a new thread to keep the UI responsive
    threading.Thread(target=run_llm_in_thread, args=(prompt,)).start()

# UI SETUP
root = tk.Tk()
root.title("Local LLM Code Generator")
root.geometry("800x750")

# Configure a style
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TButton", font=("Segoe UI", 10, "bold"))
style.configure("TLabel", font=("Segoe UI", 11))

# Define a monospaced font for the code output
code_font = font.Font(family="Consolas", size=10) 

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

# Input Widgets
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill="x", pady=(0, 10))

input_label = ttk.Label(input_frame, text="Enter Your Prompt:")
input_label.pack(anchor="w", pady=(0, 5))

input_text = scrolledtext.ScrolledText(input_frame, height=8, wrap=tk.WORD, font=("Segoe UI", 10))
input_text.pack(fill="x", expand=True)

# --- Generate Button ---
generate_button = ttk.Button(main_frame, text="Generate Code", command=handle_generate_click)
generate_button.pack(pady=10)

# --- Output Widgets ---
output_frame = ttk.Frame(main_frame)
output_frame.pack(fill="both", expand=True)

output_label = ttk.Label(output_frame, text="Generated Verilog/VHDL Code:")
output_label.pack(anchor="w", pady=(0, 5))

output_text = scrolledtext.ScrolledText(output_frame, height=20, wrap=tk.WORD, font=code_font, state="disabled")
output_text.pack(fill="both", expand=True)

# Start the application
root.mainloop()

