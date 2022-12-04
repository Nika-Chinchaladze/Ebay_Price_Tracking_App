import json


class JsonDealer:
    def __init__(self):
        self.hello = "world"

    def create_json(self):
        dictionary = {
            "None": {
                "link": "None"
            }
        }
        with open("JSON/info.json", "w") as file:
            json.dump(dictionary, file, indent=4)
            file.close()

    def append_jason(self, product_name, link):
        data = {
            product_name: {
                "link": link
            }
        }
        with open("JSON/info.json", "r") as file:
            result = json.load(file)
            result.update(data)
            file.close()
        with open("JSON/info.json", "w") as file2:
            json.dump(result, file2, indent=4)
            file2.close()

    def get_product_names(self):
        with open("JSON/info.json", "r") as docs:
            answer = json.load(docs)
            docs.close()
            result = [key for key in answer.keys()]
            result.remove("None")
            return tuple(result)

    def get_product_link(self, product_name):
        with open("JSON/info.json", "r") as docs:
            df = json.load(docs)
            docs.close()
            return df[product_name]["link"]
