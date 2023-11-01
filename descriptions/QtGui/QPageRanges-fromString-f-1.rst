.. sip:method-description::
    :status: todo
    :pysig: 926a89cdbe01ede9b29c0779f9f41845
    :realsig: (const QString&)
    :digest: bdcc4281843e3a57391f1095fafca630

Constructs and returns a :sip:ref:`~PyQt6.QtGui.QPageRanges` object populated with the *ranges* from the string representation.

::

    QPrinter printer;
    QPageRanges ranges = QPageRanges::fromString("1-3,6-7");
    printer.setPageRanges(ranges);

In case of parsing error, returns an empty :sip:ref:`~PyQt6.QtGui.QPageRanges` object.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageRanges.isEmpty`.
