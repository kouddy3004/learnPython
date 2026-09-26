from jsonpath_ng import parse


def getValueByJsonPath(jsonVal,jsonPath):
    path_expression = parse(jsonPath)
    matches = path_expression.find(jsonVal)
    # .value retrieves the extracted data
    return matches