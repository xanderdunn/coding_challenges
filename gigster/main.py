#!/usr/bin/env python

# System
import sys
import tokenize
import cStringIO

# Recursive-decent itrator-based parsing from http://effbot.org/zone/simple-iterator-parser.htm
def atom(next, token):
    if token[1] == "[":
        out = []
        token = next()
        while token[1] != "]":
            out.append(atom(next, token))
            token = next()
            if token[1] == ",":
                token = next()
        return out
    elif token[1] == "{":
        out = {}
        token = next()
        while token[1] != "}":
            key = atom(next, token)
            token = next() # Skip :
            value = atom(next, next())
            out.update({key : value})
            token = next()
            if token[1] in [',', ':']:
                token = next()
        return out
    elif token[0] is tokenize.STRING:
        return token[1][1:-1].decode("string-escape")
    elif token[0] is tokenize.NUMBER:
        return float(token[1])
    raise SyntaxError("malformed expression (%s)" % token[1])

def simple_eval(source):
    src = cStringIO.StringIO(source).readline
    src = tokenize.generate_tokens(src)
    return atom(src.next, src.next())

class JsonParser(object):

    @staticmethod
    def parse(input_str):
        return simple_eval(input_str.replace('\n', '').strip())

def main(argv):
    json_parser = JsonParser()

    print "First Step"
    for value in json_parser.parse(" [ 10, 20, 30.1 ] "):
        print value

    print "\nSecond Step"
    for value in json_parser.parse(" [ 10 , 20, \"hello\", 30.1 ] "):
        print value

    print "\nThird Step"
    for key, value in json_parser.parse("""{
            "hello": "world",
            "key1": 20,
            "key2": 20.3,
            "foo": "bar" }""").items():
        print key, value

    print "\nFourth Step"
    result = json_parser.parse("""{
            "hello": "world",
            "key1": 20,
            "key2": 20.3,
            "foo": {
                "hello1": "world1",
                "key3": [200, 300]
            } }""")
    print(result)
    for key, value in result.items():
        if isinstance(value, dict):
            for key2, value2 in value.items():
                print key2, value2
        else:
            print key, value


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
