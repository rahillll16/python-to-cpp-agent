def system_prompt(language: str) -> str:
    return f"""
You are an expert systems programmer.

Convert Python into high-performance {language}.

Rules:
- Output ONLY valid {language} code
- Add file-level and function-level docstrings
- Add inline comments for complex logic
- Preserve identical output
- Optimize for fastest runtime
"""


def planner_prompt(python_code: str, language: str) -> str:
    return f"""
Analyze the Python code.

Tasks:
- Explain algorithm
- Identify bottlenecks
- Suggest fastest {language} approach

Python:
```python
{python_code}
```
"""

def coder_prompt(python_code: str, plan: str, language: str) -> str:
    return f"""
Optimization Plan:
{plan}
Requirements:
-Identical output
-Maximum performance
-Proper comments and docstrings
-ONLY {language} code 
{python_code}"""

def verifier_prompt(code: str, language: str) -> str:
    return f"""
Review the {language} code.
Check:
-Correctness
-Output equivalence
-Performance
-Documentation

Reply ONLY:
PASS
or
Short list of fixes

{code}"""