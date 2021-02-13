.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b7aaac2012feebd8238605489da9170c

This signal is emitted when an action has changed. If you are only interested in actions in a given widget, you can watch for QWidget::actionEvent() sent with an :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionChanged`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.actionEvent`.
