import json

class FragmentCache:
    def __init__(self):
        self.entries = {}

    def get(self, key, loader):
        if key not in self.entries:
            self.entries[key] = loader()
        return self.entries[key]

class Renderer:
    def __init__(self, cache=None):
        self.cache = cache or FragmentCache()

    def render(self, template, context):
        def substitute(match):
            key = match.group(1).strip()
            return str(context.get(key, ""))
        import re
        return re.sub(r"{{ (.*?) }}", substitute, template)

    def render_page(self, path, context, loader):
        template = self.cache.get(path, lambda: loader(path))
        return self.render(template, context)
