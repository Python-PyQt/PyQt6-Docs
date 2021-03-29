.. sip:method-description::
    :status: todo
    :pysig: 612a790c5848953ce4791ed22ee10fa3
    :realsig: (const QString&,int) const
    :digest: 6c1aa9b48e118b7eecf04917f3923865

Returns the horizontal advance in pixels of the first *len* characters of *text*. If *len* is negative (the default), the entire string is used.

This is the distance appropriate for drawing a subsequent character after *text*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.boundingRect`.
