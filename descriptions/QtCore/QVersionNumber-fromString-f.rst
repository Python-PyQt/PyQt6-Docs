.. sip:method-description::
    :status: todo
    :pysig: 9711288ba394f8d301603a3d805aeb3b
    :realsig: (const QString&,int*)
    :digest: d7072740b8b8cd5ae3f752c467ba11e2

Constructs a :sip:ref:`~PyQt6.QtCore.QVersionNumber` from a specially formatted *string* of non-negative decimal numbers delimited by a period (``.``).

Once the numerical segments have been parsed, the remainder of the string is considered to be the suffix string. The start index of that string will be stored in *suffixIndex* if it is not null.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qversionnumber-main.py
    :lines: 94-98

.. seealso:: :sip:ref:`~PyQt6.QtCore.QVersionNumber.isNull`.
