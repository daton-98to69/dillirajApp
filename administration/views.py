from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.


def dashboard(request):
    return render(request, "administration/dashboard.html")


def pdf_view(request):
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(
        100, 100, "This is the result for your child at Dilliraj Secondary School!")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
