import streamlit as st
import functions

import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will help increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo... ",
              on_change=add_todo, key="new_todo")