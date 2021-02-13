.. sip:method-description::
    :status: todo
    :pysig: 67ee2b41666e72cf350bc2e589a4b154
    :realsig: (const QDateTime&) const
    :digest: 2df4218b1cebc1b2cfc0cd812f04f5f0

This virtual function is used by the date time edit whenever it needs to display *dateTime*.

If you reimplement this, you may also need to reimplement :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.validate`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.dateTimeFromText`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.validate`.
