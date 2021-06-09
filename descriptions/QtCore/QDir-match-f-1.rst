.. sip:method-description::
    :status: todo
    :pysig: da403e299845f8c1b31972a05bd0f8ae
    :realsig: (const QString&,const QString&)
    :digest: dec2c2a4fa57278088956ab064aac766

Returns ``true`` if the *fileName* matches the wildcard (glob) pattern *filter*; otherwise returns ``false``. The *filter* may contain multiple patterns separated by spaces or semicolons. The matching is case insensitive.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpression.fromWildcard`, :sip:ref:`~PyQt6.QtCore.QDir.entryList`, :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`.
