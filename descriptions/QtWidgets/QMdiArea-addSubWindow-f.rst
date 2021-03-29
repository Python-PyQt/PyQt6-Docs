.. sip:method-description::
    :status: todo
    :pysig: 875f667ac2f2fb33f32a7f16cd0225fc
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: e2d83f75dadfcc291f1ef3b6cd0d3a84

Adds *widget* as a new subwindow to the MDI area. If *windowFlags* are non-zero, they will override the flags set on the widget.

The *widget* can be either a :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` or another `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ (in which case the MDI area will create a subwindow and set the *widget* as the internal widget).

**Note:** Once the subwindow has been added, its parent will be the *viewport widget* of the :sip:ref:`~PyQt6.QtWidgets.QMdiArea`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-mdiarea-mdiareasnippets.py
    :lines: 74-82

When you create your own subwindow, you must set the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` widget attribute if you want the window to be deleted when closed in the MDI area. If not, the window will be hidden and the MDI area will not activate the next subwindow.

Returns the :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` that is added to the MDI area.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.removeSubWindow`.
