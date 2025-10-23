.. sip:method-description::
    :status: todo
    :pysig: 6d83182b8c497cc5f4344045498e539c
    :realsig: (const QStringList&, const QString&)
    :digest: 73fdae843a6de32bf8eb68751a285fff

Returns ``true`` if the *fileName* matches any of the wildcard (glob) patterns in the list of *filters*; otherwise returns ``false``. The matching is case insensitive.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpression.fromWildcard`, :sip:ref:`~PyQt6.QtCore.QDir.entryList`, :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`.
