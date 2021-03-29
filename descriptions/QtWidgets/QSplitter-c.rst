.. sip:class-description::
    :status: todo
    :brief: Implements a splitter widget
    :digest: 22fdc2ddcf53684e1937f8d0d4c13d5b

The :sip:ref:`~PyQt6.QtWidgets.QSplitter` class implements a splitter widget.

A splitter lets the user control the size of child widgets by dragging the boundary between them. Any number of widgets may be controlled by a single splitter. The typical use of a :sip:ref:`~PyQt6.QtWidgets.QSplitter` is to create several widgets and add them using :sip:ref:`~PyQt6.QtWidgets.QSplitter.insertWidget` or :sip:ref:`~PyQt6.QtWidgets.QSplitter.addWidget`.

The following example will show a :sip:ref:`~PyQt6.QtWidgets.QListView`, :sip:ref:`~PyQt6.QtWidgets.QTreeView`, and :sip:ref:`~PyQt6.QtWidgets.QTextEdit` side by side, with two splitter handles:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-splitter-splitter.py
    :lines: 64-70

If a widget is already inside a :sip:ref:`~PyQt6.QtWidgets.QSplitter` when :sip:ref:`~PyQt6.QtWidgets.QSplitter.insertWidget` or :sip:ref:`~PyQt6.QtWidgets.QSplitter.addWidget` is called, it will move to the new position. This can be used to reorder widgets in the splitter later. You can use :sip:ref:`~PyQt6.QtWidgets.QSplitter.indexOf`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.widget`, and :sip:ref:`~PyQt6.QtWidgets.QSplitter.count` to get access to the widgets inside the splitter.

A default :sip:ref:`~PyQt6.QtWidgets.QSplitter` lays out its children horizontally (side by side); you can use :sip:ref:`~PyQt6.QtWidgets.QSplitter.setOrientation`\ (\ :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Vertical`) to lay its children out vertically.

By default, all widgets can be as large or as small as the user wishes, between the :sip:ref:`~PyQt6.QtWidgets.QSplitter.minimumSizeHint` (or minimumSize()) and maximumSize() of the widgets.

:sip:ref:`~PyQt6.QtWidgets.QSplitter` resizes its children dynamically by default. If you would rather have :sip:ref:`~PyQt6.QtWidgets.QSplitter` resize the children only at the end of a resize operation, call :sip:ref:`~PyQt6.QtWidgets.QSplitter.setOpaqueResize`\ (false).

The initial distribution of size between the widgets is determined by multiplying the initial size with the stretch factor. You can also use :sip:ref:`~PyQt6.QtWidgets.QSplitter.setSizes` to set the sizes of all the widgets. The function :sip:ref:`~PyQt6.QtWidgets.QSplitter.sizes` returns the sizes set by the user. Alternatively, you can save and restore the sizes of the widgets from a :sip:ref:`~PyQt6.QtCore.QByteArray` using :sip:ref:`~PyQt6.QtWidgets.QSplitter.saveState` and :sip:ref:`~PyQt6.QtWidgets.QSplitter.restoreState` respectively.

When you hide() a child, its space will be distributed among the other children. It will be reinstated when you show() it again.

**Note:** Adding a :sip:ref:`~PyQt6.QtWidgets.QLayout` to a :sip:ref:`~PyQt6.QtWidgets.QSplitter` is not supported (either through setLayout() or making the :sip:ref:`~PyQt6.QtWidgets.QSplitter` a parent of the :sip:ref:`~PyQt6.QtWidgets.QLayout`); use :sip:ref:`~PyQt6.QtWidgets.QSplitter.addWidget` instead (see example above).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle`, :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout`, :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.
