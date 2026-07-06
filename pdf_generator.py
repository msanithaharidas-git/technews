
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch
from reportlab.lib.colors import navy, darkblue, grey
from reportlab.lib.utils import ImageReader
import datetime
import os

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = navy

heading = styles["Heading2"]
heading.textColor = darkblue

body = styles["BodyText"]
body.alignment = TA_JUSTIFY

small = styles["Normal"]
small.textColor = grey

def create_pdf(name,student_class,title,description,url,image):

    if not os.path.exists("generated"):
        os.mkdir("generated")

    filename="generated/Technical_News.pdf"

    doc = SimpleDocTemplate(
        filename,
        rightMargin=25,
        leftMargin=25,
        topMargin=20,
        bottomMargin=20
    )

    story=[]

    story.append(Paragraph("<b>TECH TODAY</b>",title_style))

    story.append(Paragraph(
        "Department of Computer Science",
        heading))

    story.append(Spacer(1,15))

    story.append(Paragraph(
        f"<b>Student :</b> {name}",
        body))

    story.append(Paragraph(
        f"<b>Class :</b> {student_class}",
        body))

    story.append(Paragraph(
        f"<b>Date :</b> {datetime.date.today()}",
        body))

    story.append(Spacer(1,15))

    story.append(Paragraph(title,heading))

    story.append(Spacer(1,10))

    if image:

        img=Image(image)

        img.drawHeight=3*inch
        img.drawWidth=5*inch

        story.append(img)

        story.append(Spacer(1,15))

    story.append(Paragraph(description,body))

    story.append(Spacer(1,20))

    story.append(Paragraph(
        "<b>Source:</b>",
        heading))

    story.append(Paragraph(url,small))

    doc.build(story)

    return filename
