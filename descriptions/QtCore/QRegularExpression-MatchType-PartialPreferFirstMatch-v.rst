.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 97c1c3fd96a791746e30e473e7dcb37c

The pattern string is matched partially against the subject string. If a partial match is found, then matching stops and the partial match is reported. In this case, other matching alternatives (potentially leading to a complete match) are not tried. Moreover, this match type assumes that the subject string only a substring of a larger text, and that (in this text) there are other characters beyond the end of the subject string. This can lead to surprising results; see the discussion in the :ref:`partial matching<qregularexpression-partial-matching>` section for more details.
