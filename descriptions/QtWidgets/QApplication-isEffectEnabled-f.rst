.. sip:method-description::
    :status: todo
    :pysig: 578b364e043aa443c3eb1e158644a80d
    :realsig: (Qt::UIEffect)
    :digest: d171651e095e308bfd4c1e333e520841

Returns ``true`` if *effect* is enabled; otherwise returns ``false``.

By default, Qt will try to use the desktop settings. To prevent this, call setDesktopSettingsAware(false).

**Note:** All effects are disabled on screens running at less than 16-bit color depth.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.setEffectEnabled`, :sip:ref:`~PyQt6.QtCore.Qt.UIEffect`.
