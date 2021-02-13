.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: d996d9ef0bda423a9761e3d85995e7ec

the widget does not feature a context menu, and in contrast to ``NoContextMenu``, the handling is *not* deferred to the widget's parent. This means that all right mouse button events are guaranteed to be delivered to the widget itself through :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent`, and :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseReleaseEvent`.
