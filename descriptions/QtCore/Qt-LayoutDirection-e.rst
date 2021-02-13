.. sip:enum-description::
    :status: todo
    :digest: b23afc27f754df5631cc5ac6e2f0fe69

Specifies the direction of Qt's layouts and text handling.

Right-to-left layouts are necessary for certain languages, notably Arabic and Hebrew.

serves two purposes. When used in conjunction with widgets and layouts, it will imply to use the layout direction set on the parent widget or QApplication. This has the same effect as QWidget::unsetLayoutDirection().

When  is used in conjunction with text layouting, it will imply that the text directionality is determined from the content of the string to be layouted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.setLayoutDirection`, :sip:ref:`~PyQt6.QtGui.QTextOption.setTextDirection`, QString::isRightToLeft().
