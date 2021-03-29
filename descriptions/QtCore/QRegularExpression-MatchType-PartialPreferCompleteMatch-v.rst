.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 06f6f35033744683cdef895e24ecb907

The pattern string is matched partially against the subject string. If a partial match is found, then it is recorded, and other matching alternatives are tried as usual. If a complete match is then found, then it's preferred to the partial match; in this case only the complete match is reported. If instead no complete match is found (but only the partial one), then the partial one is reported.
