from generate_chart_code import generate_chart_code
from reflect_chart import reflect_chart
from utils import extract_and_run_code, load_and_prepare_data

chart_v1_path = "./charts/chart_v1.png"
chart_v2_path = "./charts/chart_v2.png"
main_data_path = "./coffee_sales.csv"
data_ready = load_and_prepare_data(main_data_path).head()

# GENERATE
generated_code_v1 = generate_chart_code(chart_v1_path)
extract_and_run_code(generated_code_v1, data_ready)

# REFLECT
generated_code_v2 = reflect_chart(chart_v1_path, chart_v2_path, generated_code_v1)
extract_and_run_code(generated_code_v2, data_ready)
