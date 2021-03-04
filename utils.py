def parse_tbody(table_body):
    rows = table_body.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [element.text.strip() for element in cols]
        data.append([element for element in cols if [element]])
    return data

def table_to_dict(head, body):
    final = []
    for item in body:
        obj = [{ f"{head[key]}": val } for key, val in enumerate(item)]
        final.append(obj)
    return final