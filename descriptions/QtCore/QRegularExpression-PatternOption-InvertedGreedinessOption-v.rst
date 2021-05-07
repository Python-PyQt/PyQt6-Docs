.. sip:enum-member-description::
    :status: todo
    :value: 0x0010
    :digest: 9e57c7d0779deaf328065615ae8cbaa2

The greediness of the quantifiers is inverted: ``\*``, ``+``, ``?``, ``{m,n}``, etc. become lazy, while their lazy versions (``\*?``, ``+?``, ``??``, ``{m,n}?``, etc.) become greedy. There is no equivalent for this option in Perl regular expressions.
