import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
from plotting import *


def main():
    st.title("SF Budget Analysis 2022-25")
    df = load_data()
    display_data_overview(df)

    df_melted = pd.melt(
        df,
        id_vars=None,
        value_vars=["budget_2022_23", "budget_2023_24", "budget_2024_25"],
        var_name="Budget Year",
        value_name="Budget",
    )
    plot_budget_box(df_melted, "Box Plot of Budget by Year")
    plot_budget_box(df_melted, "Box Plot of Budget by Year (Without Outliers)", True)

    # Budget distribution and changes
    plot_budget_distribution(df)
    plot_budget_changes(df)

    # Top departments by budget
    plot_top_departments_by_budget(df)


if __name__ == "__main__":
    main()
