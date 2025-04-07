from app import FrameWorkApp
app = FrameWorkApp()

@app.route('/home')
def home(request,response):
    response.text = "Home page. Bugun biz Waitress , app.router Dakaratori haqida gaplashdik."

@app.route('/about')
def about(request,response):
    response.text = "About page. Salom men Muhammadamin Pulatov yoshim 16 da va men hozrda PDP School da talim olaman "

@app.route('/contact')
def contact(request,response):
    response.txt = "Contact page tez orada qoshiladi"
    # response.html = """
    # <html>
    #     <head>
    #         <title>Contact</title>
    #     </head>
    #     <body>
    #         <h1>Contact Page</h1>
    #         <p>Bugun biz Waitress , app.router Dakaratori haqida gaplashdik.</p>
    #
    #         <img src=""C:/Users/muham/Downloads/M3-MacBook-Pro-Wallpaper-8K.png"" alt="Mac Image">
    #     </body>
    # </html>
    # """
