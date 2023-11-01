.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 128c5b5943358769542f1ccef9c85088

Sets the list format's *start* index.

This allows you to start a list with an index other than 1. This can be used with all sorted list types: for example if the :sip:ref:`~PyQt6.QtGui.QTextListFormat.style` is :sip:ref:`~PyQt6.QtGui.QTextListFormat.Style.ListLowerAlpha` and :sip:ref:`~PyQt6.QtGui.QTextListFormat.start` is ``4``, the first list item begins with "d". It does not have any effect on unsorted list types.

The default start is ``1``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextListFormat.start`.
