
import streamlit as st
from pdf_generator import create_pdf
import os
from drive_upload import upload_to_drive

import os

os.makedirs("uploaded_images", exist_ok=True)
os.makedirs("generated", exist_ok=True)

st.set_page_config(page_title="Technical News PDF Generator",
                   layout="centered")

st.title("📰 Technical News PDF Generator")

st.write("Enter the news details below.")

name = st.text_input("Student Name")

student_class = st.text_input("Class")

title = st.text_input("News Title")

description = st.text_area("News Description", height=250)

url = st.text_input("News URL")

image = st.file_uploader(
    "Upload News Image",
    type=["jpg", "jpeg", "png"]
)

if st.button("Generate PDF"):

    if name=="" or student_class=="" or title=="" or description=="":
        st.error("Please fill all mandatory fields.")
    else:

        image_path = None

        if image is not None:

            image_path = os.path.join("generated", image.name)

            with open(image_path,"wb") as f:
                f.write(image.read())

        pdf_file = create_pdf(
                        name,
                        student_class,
                        title,
                        description,
                        url,
                        image_path
                    )

        with open(pdf_file,"rb") as pdf:

            st.success("PDF Generated Successfully.")
            pdf_path="https://drive.google.com/drive/folders/1IJsogdCX9KiuBB953Kp9kBRhfLIYP3vj?usp=sharing"
            upload_to_drive(pdf_path)
            st.download_button(
                "Download PDF",
                pdf,
                file_name="Technical_News.pdf",
                mime="application/pdf"
            )
