.. sip:class-description::
    :status: todo
    :brief: Scrolling view onto another widget
    :digest: 24f5035757ddc392df34dcf9061235f4

The :sip:ref:`~PyQt6.QtWidgets.QScrollArea` class provides a scrolling view onto another widget.

A scroll area is used to display the contents of a child widget within a frame. If the widget exceeds the size of the frame, the view can provide scroll bars so that the entire area of the child widget can be viewed. The child widget must be specified with :sip:ref:`~PyQt6.QtWidgets.QScrollArea.setWidget`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qscrollarea.py
    :lines: 54-60

The code above creates a scroll area (shown in the images below) containing an image label. When scaling the image, the scroll area can provide the necessary scroll bars:

+--------------------------------------+--------------------------------------+---------------------------------------+
| |image-qscrollarea-noscrollbars-png| | |image-qscrollarea-onescrollbar-png| | |image-qscrollarea-twoscrollbars-png| |
+--------------------------------------+--------------------------------------+---------------------------------------+

The scroll bars appearance depends on the currently set :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy`. You can control the appearance of the scroll bars using the inherited functionality from :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`.

For example, you can set the :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBarPolicy` and :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.verticalScrollBarPolicy` properties. Or if you want the scroll bars to adjust dynamically when the contents of the scroll area changes, you can use the :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBar` and :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.verticalScrollBar` functions (which enable you to access the scroll bars) and set the scroll bars' values whenever the scroll area's contents change, using the QScrollBar::setValue() function.

You can retrieve the child widget using the :sip:ref:`~PyQt6.QtWidgets.QScrollArea.widget` function. The view can be made to be resizable with the :sip:ref:`~PyQt6.QtWidgets.QScrollArea.setWidgetResizable` function. The alignment of the widget can be specified with :sip:ref:`~PyQt6.QtWidgets.QScrollArea.setAlignment`.

Two convenience functions :sip:ref:`~PyQt6.QtWidgets.QScrollArea.ensureVisible` and :sip:ref:`~PyQt6.QtWidgets.QScrollArea.ensureWidgetVisible` ensure a certain region of the contents is visible inside the viewport, by scrolling the contents if necessary.

.. _qscrollarea-size-hints-and-layouts:

Size Hints and Layouts
----------------------

When using a scroll area to display the contents of a custom widget, it is important to ensure that the :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` of the child widget is set to a suitable value. If a standard `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ is used for the child widget, it may be necessary to call :sip:ref:`~PyQt6.QtWidgets.QWidget.setMinimumSize` to ensure that the contents of the widget are shown correctly within the scroll area.

If a scroll area is used to display the contents of a widget that contains child widgets arranged in a layout, it is important to realize that the size policy of the layout will also determine the size of the widget. This is especially useful to know if you intend to dynamically change the contents of the layout. In such cases, setting the layout's :sip:ref:`~PyQt6.QtWidgets.QLayout.sizeConstraint` property to one which provides constraints on the minimum and/or maximum size of the layout (e.g., :sip:ref:`~PyQt6.QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize`) will cause the size of the scroll area to be updated whenever the contents of the layout changes.

For a complete example using the :sip:ref:`~PyQt6.QtWidgets.QScrollArea` class, see the `Image Viewer <https://doc.qt.io/qt-6/qtwidgets-widgets-imageviewer-example.html>`_ example. The example shows how to combine :sip:ref:`~PyQt6.QtWidgets.QLabel` and :sip:ref:`~PyQt6.QtWidgets.QScrollArea` to display an image.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`, :sip:ref:`~PyQt6.QtWidgets.QScrollBar`, `Image Viewer Example <https://doc.qt.io/qt-6/qtwidgets-widgets-imageviewer-example.html>`_.

.. |image-qscrollarea-noscrollbars-png| image:: ../../../images/qscrollarea-noscrollbars.png
.. |image-qscrollarea-onescrollbar-png| image:: ../../../images/qscrollarea-onescrollbar.png
.. |image-qscrollarea-twoscrollbars-png| image:: ../../../images/qscrollarea-twoscrollbars.png
