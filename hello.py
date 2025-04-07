def main():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Greeting</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """
    with open("docs/index.html", "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    main()