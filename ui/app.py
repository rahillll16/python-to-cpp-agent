import gradio as gr
from agents.planner import plan
from agents.coder import generate_code
from agents.verifier import verify
from compiler.cpp_compiler import compile_and_run
from core.models import MODELS

LANGUAGE = "C++"

def port(model, python_code):
    plan_text = plan(model, python_code, LANGUAGE)
    code = generate_code(model, python_code, plan_text, LANGUAGE)
    verdict = verify(model, code, LANGUAGE)
    if verdict != "PASS":
        print("Verifier feedback:", verdict)
    return code

with gr.Blocks(theme=gr.themes.Monochrome(), title="Python → C++ Agent") as ui:
    python_code = gr.Code(label="Python Code", language="python")
    cpp_code = gr.Code(label="Generated C++", language="cpp")

    model = gr.Dropdown(MODELS, value=MODELS[0])
    convert = gr.Button("Convert")
    run = gr.Button("Compile & Run")
    output = gr.Textbox(label="Output")

    convert.click(port, [model, python_code], cpp_code)
    run.click(compile_and_run, cpp_code, output)

ui.launch()
