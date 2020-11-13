__version__ = "0.17"


def jiradls():
    # Shortcut to create a Diamond JIRA object.
    import jiradls.dlsjira

    return jiradls.dlsjira.DLSJIRA()
