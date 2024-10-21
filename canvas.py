import streamlit as st
from streamlit_drawable_canvas import st_canvas

def Canvas():
    # Sidebar Component
    tool = st.sidebar.selectbox(
        "Tools:", ("Freedraw", "Line", "Rectangle", "Circle", "Transform")
    )
    tool_map = {"Freedraw":"freedraw", "Line":"line", "Rectangle":"rect", "Circle":"circle", "Transform":"transform"}
    drawing_mode = tool_map[tool]
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Pen Color: ", "#EEEEEE")

    # Canvas Component
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",  # For the shapes
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#000000",
        update_streamlit=True,
        height=150,
        drawing_mode=drawing_mode,
        key="canvas",
    )
    return canvas_result