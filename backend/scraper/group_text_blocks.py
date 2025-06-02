def group_text_blocks(element_text_pairs: list) -> list:
    """
    Group text blocks into blocks based on headers. 

    Input: list of {"tag": "h1", "text": "This is a Header!"}

    Output: list of 
    {"header": {"tag": "h1", "header-text": "This is a Header!"},
     "body-text": "This is text from non-header elements like paragraphs"}
    """
    blocks = []
    current_block = {"header": {"tag": None, "header-text": None}, "body-text": ""}

    for el in element_text_pairs:
        tag, text = el.get("tag"), el.get("text").strip()
        if not text:
            continue

        # headers start new block
        if tag.startswith("h"):
            if current_block["body-text"]:
                blocks.append(current_block)
            current_block = {"header": {"tag": tag, "header-text": text}, "body-text": ""}
        # append paragraphs (non-headers) to current block's body
        else:
            if current_block["body-text"]:
                current_block["body-text"] += "\n\n" + text
            else:
                current_block["body-text"] = text

    if current_block["body-text"]:
        blocks.append(current_block)

    return blocks