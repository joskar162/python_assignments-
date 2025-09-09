import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for URL
    url = input("week 6\screenshot.png ").strip()

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Get the image response
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename found, give it a default
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully as {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Please check your internet or the URL.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
