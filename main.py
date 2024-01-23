import streamlit as st
from process_user_info import show_stuff

st.set_page_config(
    page_title="Hello!",
    page_icon="👋",
)


st.write("# Welcome to Dollars and Sense!")

st.sidebar.success("How can we help you?")

st.write(
    "The 2023-2024 San Francisco budget was over $14bn and approved by the Board of Supervisors. But do you know where that money goes?"
)

st.write(
    "The city has a lot of useful data but spreadsheets with thousands of rows and confusing codes make it impossible for voters to truly understand how our tax dollars are being spent."
)

st.write(
    "Public safety, education, homelessness, public transportation and many other priorities are all top of mind for voters going into the 2024 election cycle. We know we need to make choices, but we are not equipped to ask the hard questions and make sure our money is being spent wisely."
)

st.write(
    "Our goal is to provide San Francisco voters with graphics, visuals and insights to understand the budgeting process and give answers to our most pressing questions on how tax dollars are spent."
)

st.write(
    "It’s time to take back control of our budget and vote with our wallets. It’s just simple dollars and sense."
)

st.write(
    "## Tell us about yourself to get personalized information, or feel free to browse out data insights page"
)


# TODO: give a couple options to select some basic graphs
# TODO: Add a 'just let me browse' button
def create_form():
    with st.form("budget_form"):
        st.subheader("What are you interested in learning about?")
        concern = st.radio("I am most concerned about:", ("Revenue", "Spending"))

        which_graph = st.selectbox(
            "Which graphs do you wanna see?",
            ["don't care", "overview", "budget changes", "budget distribution"],
        )
        categories = st.selectbox(
            "If you chose Spending, please choose the category of spending that most interests you:",
            [
                "Select an option",
                "Public Health",
                "Culture and Recreation",
                "Administration and Finance",
                "General City Expenditures",
                "Welfare and Neighborhood",
                "Public Protection",
                "Public Works/Transit/Commerce",
            ],
        )

        sf_school_district = st.checkbox(
            "The SF Unified School District has a separate budget. Click here if this interests you",
        )

        questions = st.text_area(
            "Please send us as many specific questions you may have about our budget:"
        )

        first_name = st.text_input("First Name (optional)")
        last_name = st.text_input("Last Name (optional)")

        email = st.text_input("Email (optional)")

        # TODO: Don't allow user to submit without giving name and email if box is checked
        updates = st.checkbox("Sign up for news and updates")

        submitted = st.form_submit_button("Show Me the Money!")

        if submitted:
            st.write("Thanks for the input!")
            return {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "updates": updates,
                "concern": concern,
                "which_graph": which_graph,
                "categories": categories,
                "sf_school_district": sf_school_district,
                "questions": questions,
            }

    return None


form_data = create_form()
if form_data:
    if form_data["which_graph"] != "don't care":
        show_stuff(form_data)
    # st.json(form_data)
