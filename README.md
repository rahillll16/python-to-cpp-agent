# 🚀 Python → High-Performance C++ Agentic Code Generator

An **agent-based system** that automatically converts **Python programs into ultra-optimized C++ code** using **frontier LLMs**, with a focus on **maximum runtime performance**, correctness, and clean systems-level code.

This project was built as an **LLM-driven compiler / transpiler prototype**, combining **planning, generation, and verification agents** with optional native compilation and execution.

---

## ✨ What This Project Does

- Takes **Python code** as input
- Uses a **Planner Agent** to analyze logic and performance bottlenecks
- Uses a **Coder Agent** to generate **high-performance C++**
- Uses a **Verifier Agent** to check correctness, output equivalence, and documentation
- Optionally **compiles and runs** the generated C++ code
- Benchmarks **Python vs C++ runtime performance**
- Supports **frontier models** (GPT-OSS-120B, Grok-4, GPT-5-Nano, Gemini, etc.)

📈 In benchmarks, **GPT-OSS-120B produced C++ code ~100,000× faster than Python** for compute-heavy workloads.

---

## 🧠 Architecture (Agentic Design)

```Python Code
↓
Planner Agent
↓
Coder Agent
↓
Verifier Agent
↓
(Optional) Compile & Execute
```


### Agents
- **Planner**: Understands the Python algorithm and suggests optimal C++ strategy
- **Coder**: Generates optimized, well-documented C++ code
- **Verifier**: Checks correctness, performance intent, and documentation quality

---

## 📁 Project Structure
```
python-to-cpp-agent/
│
├── agents/
│ ├── planner.py # Algorithm analysis agent
│ ├── coder.py # High-performance C++ generator
│ └── verifier.py # Correctness & performance checker
│
├── compiler/
│ └── cpp_compiler.py # g++ compile & run pipeline
│
├── core/
│ ├── prompts.py # All LLM prompts
│ └── models.py # Model & client registry
│
├── ui/
│ └── app.py # Gradio UI
│
├── main.py # Entry point
├── requirements.txt
├── .env.example
└── README.md
```


---

## ⚙️ Complete Setup Guide

1. Clone the repository  
Run: `git clone https://github.com/rahillll16/python-to-cpp-agent.git`  
Then: `cd python-to-cpp-agent`

2. (Recommended) Create and activate a virtual environment  
Linux / macOS: `python -m venv venv && source venv/bin/activate`  
Windows: `python -m venv venv && venv\Scripts\activate`

3. Install dependencies  
Run: `pip install -r requirements.txt`

4. Configure API keys  
Create a file named `.env` in the project root and add:  
`OPENAI_API_KEY=your_openai_key_here`  
`GOOGLE_API_KEY=your_gemini_key_here` (optional)  
Only one valid provider key is required.

5. (Optional) Install C++ compiler  
This is required only if you want to compile and run generated C++ locally.  
Linux (Ubuntu/Debian): `sudo apt update && sudo apt install g++`  
macOS: `xcode-select --install`  
Windows: Install MinGW-w64 or Visual Studio Build Tools and ensure `g++` is in PATH.

6. Run the application  
Run: `python main.py`  
Open the browser link shown in the terminal to access the Gradio UI.

✅ Setup complete — the system is now ready to convert Python code into high-performance C++ using an agentic LLM pipeline.

