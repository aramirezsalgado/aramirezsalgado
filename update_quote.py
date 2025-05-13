import requests
import re
import sys
import os

try:
    # Log current directory
    print(f"📁 Current directory: {os.getcwd()}")
    print("📄 Files:", os.listdir())

    # Fetch quote
    print("🔄 Fetching quote...")
    response = requests.get("https://api.quotable.io/random")
    response.raise_for_status()
    data = response.json()

    quote = f"_{data['content']}_\n\n**— {data['author']}**"
    print("✅ Quote fetched successfully")

    # Read README
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Replace between the markers
    if "<!--QUOTE_START-->" in content and "<!--QUOTE_END-->" in content:
        new_content = re.sub(
            r"<!--QUOTE_START-->.*?<!--QUOTE_END-->",
            f"<!--QUOTE_START-->\n{quote}\n<!--QUOTE_END-->",
            content,
            flags=re.DOTALL,
        )

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)

        print("✅ README updated with new quote")
    else:
        raise ValueError("❌ Quote markers not found in README.md")

except Exception as e:
    print(f"❌ Script failed with error: {e}")
    sys.exit(1)
