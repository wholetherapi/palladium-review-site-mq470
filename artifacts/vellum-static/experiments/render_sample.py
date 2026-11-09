import json
import time

from src.renderer import Renderer

def main():
    payload = json.load(open("data/site_fixture.json"))
    renderer = Renderer()
    pages = {page["path"]: page["template"] for page in payload["pages"]}
    started = time.perf_counter()
    for page in payload["pages"]:
        renderer.render_page(page["path"], payload["context"], pages.__getitem__)
    print("rendered %d pages in %.4f s" % (len(payload["pages"]), time.perf_counter() - started))

if __name__ == "__main__":
    main()
