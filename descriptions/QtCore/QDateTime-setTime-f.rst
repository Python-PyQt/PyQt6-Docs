.. sip:method-description::
    :status: todo
    :pysig: 40d2a07ce48f13a248736bbf57ccf45d
    :realsig: (QTime)
    :digest: aa2ac08dd0b9fd00d96a4c752b409896

Sets the time part of this datetime to *time*. If *time* is not valid, this function sets it to midnight. Therefore, it's possible to clear any set time in a :sip:ref:`~PyQt6.QtCore.QDateTime` by setting it to a default :sip:ref:`~PyQt6.QtCore.QTime`:

::

    QDateTime dt = QDateTime::currentDateTime();
    dt.setTime(QTime());

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.time`, :sip:ref:`~PyQt6.QtCore.QDateTime.setDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeSpec`.
