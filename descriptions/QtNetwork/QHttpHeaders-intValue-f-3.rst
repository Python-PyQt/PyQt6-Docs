.. sip:method-description::
    :status: todo
    :pysig: 36be5d06d42afbd90767181d031c242f
    :realsig: (QAnyStringView) const
    :digest: e8522a6964842c870b4c6488246c3339

Returns the value of the first valid header *name* interpreted as a 64-bit integer. If the header does not exist or cannot be parsed as an integer, returns ``std::nullopt``.

.. seealso:: intValues(QAnyStringView name), intValueAt(qsizetype i).
