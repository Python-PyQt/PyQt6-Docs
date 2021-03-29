.. sip:method-description::
    :status: todo
    :pysig: a61fe7e508af5dd2047f6abeb10536f5
    :realsig: (const QKeySequence&,Qt::ShortcutContext)
    :digest: 88fb6bc0d5821e54c0ee6f922dec1858

Adds a shortcut to Qt's shortcut system that watches for the given key *sequence* in the given *context*. If the *context* is :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext.ApplicationShortcut`, the shortcut applies to the application as a whole. Otherwise, it is either local to this widget, :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext.WidgetShortcut`, or to the window itself, :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext.WindowShortcut`. For widgets that are not part of a window (i.e., top-level widgets and their children), :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext.WindowShortcut` shortcuts apply to the scene.

If the same key *sequence* has been grabbed by several widgets, when the key *sequence* occurs a :sip:ref:`~PyQt6.QtCore.QEvent.Type.Shortcut` event is sent to all the widgets to which it applies in a non-deterministic order, but with the ``ambiguous'' flag set to true.

**Warning:** You should not normally need to use this function; instead create :sip:ref:`~PyQt6.QtGui.QAction`\ s with the shortcut key sequences you require (if you also want equivalent menu options and toolbar buttons), or create :sip:ref:`~PyQt6.QtGui.QShortcut`\ s if you just need key sequences. Both :sip:ref:`~PyQt6.QtGui.QAction` and :sip:ref:`~PyQt6.QtGui.QShortcut` handle all the event filtering for you, and provide signals which are triggered when the user triggers the key sequence, so are much easier to use than this low-level function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.releaseShortcut`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setShortcutEnabled`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabShortcut`.
