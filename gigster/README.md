# Json Parser

## Problem
Given a valid json string (with simplified format), parse the string and return the corresponding object made of dict, list, str and float.

### First Step
Please implement the `parse` to parse a list of floats. Here we assume that float is formatted as followed, `100, 20.0, 0.2` and you don't need to worry about cases like `2e+5, .2309, etc.`. In fact, for the sake of simplicity, don't even worry about negative values. Please be aware that there could be empty space that need to be taken care of. For instance,

~~~python
# should return a list with three floats
JsonParser().parse(" [ 10 , 20.0, 0.2 ] ");
~~~

### Second Step
Generalize the parse function to be able to parse a list of both floats and strs. The str is assumed to be surrounded by double quote only and each string value does not contain double quotes. For instance,

~~~python
# should return a List with (float) 10, (float) 20.0, (str) "hello", (float) 0.2
JsonParser().parse(" [ 10, 20.0, "hello", 0.2 ] ");
~~~

### Third Step
Generalize the parse function to be able to parse an object. The key of each attribute is assumed to be a str surrounded by double quote only. For instance,

~~~python
# should return a dict with key values "foo" => "bar" and "hello" => 100
JsonParser().parse("{ \"foo\": \"bar\", \"hello\" : 100 }");
~~~

### Fourth Step
Generalize the parse function to be able to parse an object with nested object.

~~~python
JsonParser().parse("{ \"key\": { \"foo\": \"bar\", \"hello\" : 100 } }");
~~~

## Submission
Upon completion, please follow the instruction described in the website (where you found the instruction to download the project) to submit your solution. You can submit as many times as you like and your last submission will be used for the final evaluation as well as marking the end of your interview.

Lastly, do not worry about submitting many times nor running a little bit over time as they will not be penalized.

