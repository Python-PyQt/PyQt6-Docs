.. sip:method-description::
    :status: todo
    :pysig: 1bdc2b4a53d782fd6f3ac0fcb4a269bd
    :realsig: (QAnyStringView) const
    :digest: a457cb9ac3bdc1deeb4f7d4190c21caa

Returns the values of the header *name* interpreted as 64-bit integer in a list. If the header does not exist or cannot be parsed as an integer, returns ``std::nullopt``.

.. seealso:: intValue(QAnyStringView name), intValueAt(qsizetype i).
