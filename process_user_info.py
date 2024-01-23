from plotting import (
    load_data,
    display_data_overview,
    plot_budget_changes,
    plot_budget_distribution,
)


def show_stuff(user_data):
    df = load_data()
    if user_data["which_graph"] == "overview":
        display_data_overview(df)
    elif user_data["which_graph"] == "budget changes":
        plot_budget_changes(df)
    elif user_data["which_graph"] == "budget distribution":
        plot_budget_distribution(df)
