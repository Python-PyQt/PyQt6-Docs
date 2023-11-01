.. sip:method-description::
    :status: todo
    :pysig: d6503b4cded8d487320ad24902b1373f
    :realsig: (qreal, const QString&) const
    :digest: e80de319469b850edbe618db94261cb1

Returns the formatted label string using the specified *value* and *format*.

Reimplement this method in a subclass to resolve the formatted string for a given *value* if the default formatting rules specified for :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.labelFormat` property are not sufficient.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.labelStrings`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.labelFormat`.
