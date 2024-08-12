from fasthtml.common import *

app, rt = fast_app(live=True)


@@rt('/')
def landing_page():
    return Div(
        Div(
            H1("Welcome to Our Service!"),
            P("Discover the world's easiest way to get things done."),
            style="text-align: center; padding: 50px;"
        ),
        Div(
            A("Get Started", href="/get-started", style="background-color: #4CAF50; color: white; padding: 14px 25px; text-align: center; text-decoration: none; display: inline-block; border-radius: 8px;"),
            style="text-align: center; padding: 20px;"
        ),
        style="font-family: Arial, sans-serif;"
    )

@rt('/get-started')
def get_started():
    return Div(
        H1("Getting Started"),
        P("To get started with our service, simply follow the instructions below."),
        style="font-family: Arial, sans-serif; padding: 30px;"
    )


serve()