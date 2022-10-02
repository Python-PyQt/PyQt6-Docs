.. sip:method-description::
    :status: todo
    :pysig: 856526e8e295804b2008d19fc80d5966
    :realsig: (QAnyStringView,qsizetype*)
    :digest: 8f7c379eec664c1d659a5ec44764aaa6

Constructs a :sip:ref:`~PyQt6.QtCore.QVersionNumber` from a specially formatted *string* of non-negative decimal numbers delimited by a period (``.``).

Once the numerical segments have been parsed, the remainder of the string is considered to be the suffix string. The start index of that string will be stored in *suffixIndex* if it is not null.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qversionnumber-main.py
    :lines: 102-106

**Note:** In versions prior to Qt 6.4, this function was overloaded for QString, QLatin1StringView and QStringView instead, and *suffixIndex* was an ``int\*``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QVersionNumber.isNull`.
