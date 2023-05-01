import re

# Define regular expressions for the various tokens
token_regexes = {
    'identifier': r'[a-z]+[a-z0-9]*',
    'number': r'[0-9]+',
    'operator': r'[\+\-\*/]',
    'comparison': r'[<>]=?|==',
    'open_paren': r'\(',
    'close_paren': r'\)',
    'comma': r',',
    'colon': r':',
    'equal': r'=',
    'if': r'if',
    'else': r'else'
}

# Compile regular expressions into pattern objects
patterns = {name: re.compile(regex) for name, regex in token_regexes.items()}

# Define a function to tokenize the input source code
def tokenize(code):
    tokens = []
    i = 0
    while i < len(code):
        match = None
        for pattern in patterns.values():
            match = pattern.match(code[i:])
            if match:
                token_type = [name for name, regex in patterns.items() if regex == pattern][0]
                token_value = match.group(0)
                tokens.append((token_type, token_value))
                i += len(token_value)
                break
        if not match:
            raise SyntaxError(f'Invalid syntax near "{code[i:]}"')
    return tokens
