.. sip:class-description::
    :status: todo
    :brief: Convenience class for drawing QStyle elements inside a widget
    :digest: c152905c60583ce5fcdf7c8f92920bdf

The :sip:ref:`~PyQt6.QtWidgets.QStylePainter` class is a convenience class for drawing :sip:ref:`~PyQt6.QtWidgets.QStyle` elements inside a widget.

:sip:ref:`~PyQt6.QtWidgets.QStylePainter` extends :sip:ref:`~PyQt6.QtGui.QPainter` with a set of high-level ``draw...()`` functions implemented on top of :sip:ref:`~PyQt6.QtWidgets.QStyle`'s API. The advantage of using :sip:ref:`~PyQt6.QtWidgets.QStylePainter` is that the parameter lists get considerably shorter. Whereas a :sip:ref:`~PyQt6.QtWidgets.QStyle` object must be able to draw on any widget using any painter (because the application normally has one :sip:ref:`~PyQt6.QtWidgets.QStyle` object shared by all widget), a :sip:ref:`~PyQt6.QtWidgets.QStylePainter` is initialized with a widget, eliminating the need to specify the `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, the :sip:ref:`~PyQt6.QtGui.QPainter`, and the :sip:ref:`~PyQt6.QtWidgets.QStyle` for every function call.

Example using :sip:ref:`~PyQt6.QtWidgets.QStyle` directly:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-styles-styles.py
    :lines: 66-80

Example using :sip:ref:`~PyQt6.QtWidgets.QStylePainter`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-styles-styles.py
    :lines: 66-66

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-styles-styles.py
    :lines: 85-85

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-styles-styles.py
    :lines: 87-97

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle`, :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
