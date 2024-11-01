import datetime
import requests
import re
import json
import os

# Specify the file path
file_path = "data/dangdang.json"

# Check if the file exists before trying to delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been updated.")
else:
    print(f"{file_path} does not exist.")


def request_dandan(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        # response.encoding = "utf-8"  # bug: will cause gradle
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def parse_result(html):
    # Regular expression pattern to match desired book details
    pattern = re.compile(
        '<li.*?list_num.*?(\d+)\.</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">(.*?)</span>.*?</li>',
        re.S,
    )
    # Find all matches for the pattern in the HTML
    items = re.findall(pattern, html)
    # Yield each parsed item as a dictionary, escaping any special characters
    for item in items:
        yield {
            "rank": item[0],
            "image": item[1],
            "title": item[2],
            "recommend": item[3],
            "author": item[4],
            "times": item[5],
            "price": item[6],
        }


# Initialize an empty list to store items
items = []


def write_item_to_file(item):
    items.append(item)


def save_to_json_file(filename="data/dangdang.json"):
    # Prepare data structure for JSON output
    data = {
        "author": "henrifox",
        "source": "DangDang",
        "url": "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-",
        "count": len(items),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "list": items,
    }
    # Write data to file in JSON format
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main(page):
    url = (
        "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
        + str(page)
    )
    html = request_dandan(url)
    if html:  # Check if request was successful
        parsed_items = parse_result(html)  # Parse the HTML to extract items
        for item in parsed_items:
            # for key in item:
            #     item[key] = item[key].replace('%', '%25')
            write_item_to_file(item)
        save_to_json_file()


if __name__ == "__main__":
    # Clear items list before starting to avoid duplicate data
    items.clear()
    for i in range(1, 3):
        main(i)
    # Save final JSON after all pages have been processed
    save_to_json_file()
