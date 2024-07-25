import os

def create_html_files(iframes):
    """
    Create separate HTML files for each iframe.

    Args:
        iframes (list): List of iframe URLs.
    """
    for i, iframe in enumerate(iframes):
        filename = f"iframe_{i+1}.html"
        with open(filename, "w") as f:
            f.write(f"<html><body><iframe src='{iframe}' width='100%' height='100%'></iframe></body></html>")
        print(f"Created {filename}")

def main():
    iframes = input("Enter a list of iframe URLs (separated by commas): ")
    iframes = [iframe.strip() for iframe in iframes.split(",")]
    create_html_files(iframes)

if __name__ == "__main__":
    main()