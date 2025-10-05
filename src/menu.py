
## Starter code — `src/menu.py`

def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    """
    # TODO: implement recursively
    if not node:
        return []

    if node.get("type") == "item":
        # If an item has no name, ignore it (treat as missing)
        name = node.get("name")
        if name is None:
            return []
        return [name]

    if node.get("type") == "category":
        flat_list = []
        for child in node.get("children", []):
            flat_list.extend(flatten_menu(child))
        return flat_list

    return []

