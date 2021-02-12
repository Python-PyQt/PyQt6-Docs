.. sip:enum-member-description::
    :status: todo
    :value: 0x0008
    :realname: QRegularExpression::PatternOption::ExtendedPatternSyntaxOption
    :digest: 65a3f1d99c9ca6fd5f426cc9398aed6b

Any whitespace in the pattern string which is not escaped and outside a character class is ignored. Moreover, an unescaped sharp (\ **#**) outside a character class causes all the following characters, until the first newline (included), to be ignored. This can be used to increase the readability of a pattern string as well as put comments inside regular expressions; this is particularly useful if the pattern string is loaded from a file or written by the user, because in C++ code it is always possible to use the rules for string literals to put comments outside the pattern string. This option corresponds to the ``/x`` modifier in Perl regular expressions.
