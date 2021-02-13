.. sip:signal-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint&)
    :digest: f99eeba97b283f65fcf39e74376bdbb2

This signal is emitted when the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.contextMenuPolicy` is :sip:ref:`~PyQt6.QtCore.Qt.ContextMenuPolicy.CustomContextMenu`, and the user has requested a context menu on the widget. The position *pos* is the position of the context menu event that the widget receives. Normally this is in widget coordinates. The exception to this rule is :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` and its subclasses that map the context menu event to coordinates of the :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewport`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`, :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtWidgets.QWidget.contextMenuPolicy`.
