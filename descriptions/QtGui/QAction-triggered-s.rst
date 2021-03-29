.. sip:signal-description::
    :status: todo
    :pysig: 172b3fa18e5b4fe980b90f7beb495fa0
    :realsig: (bool)
    :digest: d52124bf75a9a598a8016e939fddf875

This signal is emitted when an action is activated by the user; for example, when the user clicks a menu option, toolbar button, or presses an action's shortcut key combination, or when :sip:ref:`~PyQt6.QtGui.QAction.trigger` was called. Notably, it is *not* emitted when :sip:ref:`~PyQt6.QtGui.QAction.setChecked` or :sip:ref:`~PyQt6.QtGui.QAction.toggle` is called.

If the action is checkable, *checked* is true if the action is checked, or false if the action is unchecked.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.activate`, :sip:ref:`~PyQt6.QtGui.QAction.toggled`, checked.
