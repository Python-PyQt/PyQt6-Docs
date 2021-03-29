.. sip:method-description::
    :status: todo
    :pysig: 2f0da4d3658dfe115217ca868dfa5e64
    :realsig: (QLayout*)
    :digest: cf63381f4a2f23a1412e38b7237c4434

Sets the layout manager for this widget to *layout*.

If there already is a layout manager installed on this widget, `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ won't let you install another. You must first delete the existing layout manager (returned by :sip:ref:`~PyQt6.QtWidgets.QWidget.layout`) before you can call  with the new layout.

If *layout* is the layout manager on a different widget,  will reparent the layout and make it the layout manager for this widget.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-layouts-layouts.py
    :lines: 174-176

An alternative to calling this function is to pass this widget to the layout's constructor.

The `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ will take ownership of *layout*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.layout`, `Layout Management <https://doc.qt.io/qt-6/layout.html>`_.
