.. sip:method-description::
    :status: todo
    :pysig: a73944383ffd572ba8b60debc3383262
    :realsig: (QWidget*)
    :digest: 367abf587072779fe44e70d2cfd96d67

Constructs a :sip:ref:`~PyQt6.QtWidgets.QFocusFrame`.

The focus frame will not monitor *parent* for updates but rather can be placed manually or by using :sip:ref:`~PyQt6.QtWidgets.QFocusFrame.setWidget`. A :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` sets :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_NoChildEventsForParent` attribute; as a result the parent will not receive a :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildAdded` event, this will make it possible to manually set the geometry of the :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` inside of a :sip:ref:`~PyQt6.QtWidgets.QSplitter` or other child event monitoring widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFocusFrame.setWidget`.
