.. sip:enum-description::
    :status: todo
    :digest: 63d24124f83e18361b3a336f79cfef33

Specifies the direction of Qt's layouts and text handling.

Right-to-left layouts are necessary for certain languages, notably Arabic and Hebrew.

serves two purposes. When used in conjunction with widgets and layouts, it will imply to use the layout direction set on the parent widget or :sip:ref:`~PyQt6.QtWidgets.QApplication`. This has the same effect as :sip:ref:`~PyQt6.QtWidgets.QWidget.unsetLayoutDirection`.

When  is used in conjunction with text layouting, it will imply that the text directionality is determined from the content of the string to be layouted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.setLayoutDirection`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayoutDirection`, :sip:ref:`~PyQt6.QtGui.QTextOption.setTextDirection`, QString::isRightToLeft().
