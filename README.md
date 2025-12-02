# VerilogPal
VerilogPal is a lightweight large language model designed to generate Verilog code. Its name is a triple wordplay describing its function.
1. Pal (English noun): friend. VerilogPal acts as a friend to aid engineers.
2. Pal (Hindi noun): moment. VerilogPal requires only a relative moment to generate code.
3. Pal (name): a phenomenal computer engineering professor.

This repository is a compilation of files used to train two HuggingFace models: [jmccoy7/VerilogPal270M](https://huggingface.co/jmccoy7/VerilogPal270M) and [jmccoy7/VerilogPal1B](https://huggingface.co/jmccoy7/VerilogPal1B). These models are fine-tuned models based off of Google's gemma-3 models. They were fine-tuned to generate Verilog code using the [KSU-HW-SEC/Verilog_code](https://huggingface.co/datasets/KSU-HW-SEC/Verilog_code) dataset and tested using the testbenches in [shailja-thakur/VGen](https://github.com/shailja-thakur/VGen). If you would like to try the models out, you must only obtain them from HuggingFace. If you would like to attempt to replicate out process, follow the instructions below. 

## Instructions
1. Run the code in training.ipynb. It was originally run in Google Colab. Therefore, it may require some tweaks to run on a local machine. You will also want to read through it to change some values to match your own (hyperparameters, model names, etc).
2. Run the code in testing.ipynb. This will run inference on the model using prompts from [shailja-thakur/VGen](https://github.com/shailja-thakur/VGen). Then move the generated files into the appropriate folders in /tests. If you would like, you may use the file prep.sh to zip up all the generated Verilog files. 
3. With all the generated files in their proper folder in /tests, run tests/test.sh. It is currently configured to only test one difficulty level at a time. If you would like to run test all difficulty levels, you will need to tweak the first line of the file and run it three times. Note: this step requires you to have [ICARUS Verilog](https://github.com/steveicarus/iverilog) installed. 
4. Review the output files to see how many outputs compiled and passed the testbenches. 

## Additional Resources
If you'd like, you may use the file "UI code progression"/LLM_UI_gardio2.0.py to create a GUI of the model.

https://github.com/user-attachments/assets/9409584c-3202-440d-a9f0-b5f33acea905

