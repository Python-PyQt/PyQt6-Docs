.. sip:enum-member-description::
    :status: todo
    :value: 0x0040
    :digest: 85de1bc6ffa59f46f8e9db3a535d7bf5

The meaning of the ``\w``, ``\d``, etc., character classes, as well as the meaning of their counterparts (``\W``, ``\D``, etc.), is changed from matching ASCII characters only to matching any character with the corresponding Unicode property. For instance, ``\d`` is changed to match any character with the Unicode Nd (decimal digit) property; ``\w`` to match any character with either the Unicode L (letter) or N (digit) property, plus underscore, and so on. This option corresponds to the ``/u`` modifier in Perl regular expressions.
