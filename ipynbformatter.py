import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

# 입력 디렉터리 및 출력 디렉터리 설정
input_dir = "input_dir"
output_dir = "Converted_Notebooks"
os.makedirs(output_dir, exist_ok=True)

# 모든 .py 파일 변환
for file_name in os.listdir(input_dir):
    if file_name.endswith(".py"):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name.replace(".py", ".ipynb"))

        # Python 스크립트 읽기
        with open(input_path, "r") as f:
            script_content = f.read()

        # 노트북 생성 및 변환
        notebook = new_notebook()
        notebook.cells.append(new_code_cell(script_content))
        with open(output_path, "w") as f:
            nbformat.write(notebook, f)

        print(f"Converted {file_name} to {output_path}")
