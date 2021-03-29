.. sip:method-description::
    :status: todo
    :pysig: da403e299845f8c1b31972a05bd0f8ae
    :realsig: (const QString&,const QString&)
    :digest: 3531fc49c30d7c50345ec858e168af66

Returns ``true`` if the *fileName* matches the wildcard (glob) pattern *filter*; otherwise returns ``false``. The *filter* may contain multiple patterns separated by spaces or semicolons. The matching is case insensitive.

.. seealso:: `QRegularExpression Wildcard Matching <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#wildcard-matching>`_, :sip:ref:`~PyQt6.QtCore.QDir.entryList`, :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`.
