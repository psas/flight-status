TAXONOMY = {
    "types": {
        "launch": {"contains": ["system"]},
        "system": {"contains": ["module"]},
        "module": {"contains": ["part", "software"]},
        "part": {"contains": []},
        "software": {"contains": []},
    },
    "top": "launch",
}
