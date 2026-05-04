import base64
import re
import pandas as pd


def extract_and_run_code(llm_output: str, df: pd.DataFrame) -> bool:
    match = re.search(r"<execute_python>([\s\S]*?)</execute_python>", llm_output)
    if not match:
        print("❌ No se encontró código entre los tags.")
        return False

    code = match.group(1).strip()
    print("📝 Código extraído:\n", code)

    exec_globals = {"df": df}  # el DataFrame disponible para el código
    exec(code, exec_globals)  # ejecuta el código dinámicamente
    return True


def load_and_prepare_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["quarter"] = df["date"].dt.quarter
    return df


def encode_image_b64(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
