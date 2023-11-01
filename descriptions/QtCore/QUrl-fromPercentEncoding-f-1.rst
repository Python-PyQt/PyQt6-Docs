.. sip:method-description::
    :status: todo
    :pysig: 25020546d254065a1e96280fc4c14887
    :realsig: (const QByteArray&)
    :digest: 4dee15520b97b07b3f1213dc57bc1da1

Returns a decoded copy of *input*. *input* is first decoded from percent encoding, then converted from UTF-8 to unicode.

**Note:** Given invalid input (such as a string containing the sequence "%G5", which is not a valid hexadecimal number) the output will be invalid as well. As an example: the sequence "%G5" could be decoded to 'W'.
