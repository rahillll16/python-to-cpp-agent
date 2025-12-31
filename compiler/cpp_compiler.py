import subprocess

COMPILE_COMMAND = [
    "g++",
    "-std=c++17",
    "-O3",
    "-Ofast",
    "-march=native",
    "main.cpp",
    "-o",
    "main.exe"
]

RUN_COMMAND = ["./main.exe"]

def compile_and_run(code: str) -> str:
    with open("main.cpp", "w") as f:
        f.write(code)

    subprocess.run(COMPILE_COMMAND, check=True)
    result = subprocess.run(RUN_COMMAND, capture_output=True, text=True, check=True)
    return result.stdout
