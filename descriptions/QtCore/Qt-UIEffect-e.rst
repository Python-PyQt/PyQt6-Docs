.. sip:enum-description::
    :status: todo
    :digest: aa80c3c8a77486b0e21cc3430f58a515

This enum describes the available UI effects.

By default, Qt will try to use the platform specific desktop settings for each effect. Use the QApplication::setDesktopSettingsAware() function (passing ``false`` as argument) to prevent this, and the QApplication::setEffectEnabled() to enable or disable a particular effect.

Note that all effects are disabled on screens running at less than 16-bit color depth.

.. seealso:: QApplication::setEffectEnabled()QGuiApplication::setDesktopSettingsAware().
