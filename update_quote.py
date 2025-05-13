import requests
import re
import sys
import os

try:
    print(f"📁 Current directory: {os.getcwd()}")
    print("📄 Files:", os.listdir())
    
    # ✅ New API
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()[0]  # returns a list with one quote
    quote = f"_{data['q']}_\n\n**— {data['a']}**"
    print("✅ Quote fetched successfully")

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

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
