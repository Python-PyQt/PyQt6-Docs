.. sip:enum-description::
    :status: todo
    :digest: 73a113fdadf6ad3e6471466c6de32300

This enum describes the available UI effects.

By default, Qt will try to use the platform specific desktop settings for each effect. Use the QApplication::setDesktopSettingsAware() function (passing ``false`` as argument) to prevent this, and the :sip:ref:`~PyQt6.QtWidgets.QApplication.setEffectEnabled` to enable or disable a particular effect.

Note that all effects are disabled on screens running at less than 16-bit color depth.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.setEffectEnabled`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.setDesktopSettingsAware`.
