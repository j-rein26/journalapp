from database import add_entry, get_entries, create_table
import streamlit as st
from datetime import date

create_table()

greeting = st.title("Welcome to the programming diary!")

menu = st.selectbox("Please select one of the following options: ",
 ("Select an option...", "Add new entry for today",
 "View entries", "Exit"),)


# Only display the selection message after the user has made a valid choice
if menu != "Select an option...":
    st.write(f"You selected: {menu}")


def prompt_new_entry():
    entry_content = st.text_area("What have you learned today? ")
    entry_date = st.date_input("Please select the date:", value=date.today())
    st.write(f"Selected date: {entry_date}")
    
    #Button to save entry
    if st.button("Save Entry"):
        add_entry(entry_content, str(entry_date))
        st.success("Your entry has been saved!")

def view_entries(entries):
    entries = get_entries()
    if not entries:
        st.write("No entries found.")
    else:
        # Display all entries in a user-friendly way
        for entry in entries:
            st.write(f"### {entry['date']}")
            st.write(f"{entry['content']}")
            st.write("---")

# Handling the "Exit" option
if menu == "Exit":
    st.write("Thank you for using the diary! The app will remain active, but you're free to close this window.")
    st.stop()  # This will stop the execution of the app, but it won't stop the app entirely.

# Handling other interactions (Add new entry for today and View entries)
elif menu == "Add new entry for today":
    prompt_new_entry()
        
elif menu == "View entries":
    view_entries(get_entries())

        
