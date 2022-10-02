.. sip:enum-description::
    :status: todo
    :digest: f1a5887157e659b0e02b3c7b8f55e808

Specifies the direction of Qt's layouts and text handling.

Right-to-left layouts are necessary for certain languages, notably Arabic and Hebrew.

LayoutDirectionAuto serves two purposes. When used in conjunction with widgets and layouts, it will imply to use the layout direction set on the parent widget or :sip:ref:`~PyQt6.QtWidgets.QApplication`. This has the same effect as :sip:ref:`~PyQt6.QtWidgets.QWidget.unsetLayoutDirection`.

When LayoutDirectionAuto is used in conjunction with text layouting, it will imply that the text directionality is determined from the content of the string to be layouted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.setLayoutDirection`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayoutDirection`, :sip:ref:`~PyQt6.QtGui.QTextOption.setTextDirection`, QString::isRightToLeft().
