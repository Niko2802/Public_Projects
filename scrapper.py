import requests
from pyquery import PyQuery as pq


def get_post_data(headers):
    r = requests.get("https://morpher.ru/Demo.aspx", headers=headers)
    post_data = {}
    if r.status_code == 200:
        html_text = r.text
        doc = pq(html_text)
        for x in doc.items("div input"):
            key = x.attr("name")
            val = x.attr("value")
            post_data[key] = val
        post_data["ctl00$ctl00$ctl00$BodyPlaceHolder$ContentPlaceHolder1$ContentPlaceHolder1$TextBox1"] = s
    return post_data


s = "красный"
mask = {"Именительный", "Рoдительный2", "Дательный",
        "Винительный", "Творительный", "Предложный"}
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
post_data = get_post_data(headers)
headers["origin"] = "https://morpher.ru"
headers["refer"] = "https://morpher.ru/Demo.aspx"
r = requests.post("https://morpher.ru/Demo.aspx",
                  headers=headers, data=post_data)
print(r.status_code)
if r.status_code == 200:
    html_text = r.text
    with open("test.html", "w", encoding="utf-8") as f:
        f.write(html_text)
    res_doc = pq(html_text)
    for x in res_doc.items("td.answer > span"):
        id = x.attr("id")
        if id is None:
            xs = str(x)
            pos = xs.split("Рoдительный2\">")
            pos = pos.pop().split("</span>")
            print(pos[0])
            continue
        parts = set(id.split("_"))
        res = mask.intersection(parts)
        if res:
            print(x.text())
