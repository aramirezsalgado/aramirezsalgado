import requests
import re

response = requests.get("https://api.quotable.io/random")
data = response.json()
quote = f"_{data['content']}_\n\n**— {data['author']}**"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!--QUOTE_START-->.*?<!--QUOTE_END-->",
    f"<!--QUOTE_START-->\n{quote}\n<!--QUOTE_END-->",
    content,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
