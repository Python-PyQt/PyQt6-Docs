.. sip:method-description::
    :status: todo
    :pysig: a73944383ffd572ba8b60debc3383262
    :realsig: (QWidget*)
    :digest: ef7db887ac5aaa4b314d6386e10f6c92

Constructs a new :sip:ref:`~PyQt6.QtWidgets.QGridLayout` with parent widget, *parent*. The layout has one row and one column initially, and will expand when new items are inserted.

The layout is set directly as the top-level layout for *parent*. There can be only one top-level layout for a widget. It is returned by :sip:ref:`~PyQt6.QtWidgets.QWidget.layout`.

If *parent* is ``nullptr``, then you must insert this grid layout into another layout, or set it as a widget's layout using :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayout`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayout`.
