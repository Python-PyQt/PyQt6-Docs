.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: () const
    :digest: e44104ffaed8a926310d3c06992308af

If type() is :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded`, returns the action that should appear before :sip:ref:`~PyQt6.QtGui.QActionEvent.action`. If this function returns ``nullptr``, the action should be appended to already existing actions on the same widget.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QActionEvent.action`, :sip:ref:`~PyQt6.QtWidgets.QWidget.actions`.
