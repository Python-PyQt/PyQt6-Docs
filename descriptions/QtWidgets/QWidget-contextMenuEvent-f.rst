.. sip:method-description::
    :status: todo
    :pysig: 99c427938ef8054d6f5d0ab09f02da65
    :realsig: (QContextMenuEvent*)
    :digest: 893835ba9bbf7cf16b3fe68d0f99060a

This event handler, for event *event*, can be reimplemented in a subclass to receive widget context menu events.

The handler is called when the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.contextMenuPolicy` is :sip:ref:`~PyQt6.QtCore.Qt.ContextMenuPolicy.DefaultContextMenu`.

The default implementation ignores the context event. See the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` documentation for more details.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.customContextMenuRequested`.
