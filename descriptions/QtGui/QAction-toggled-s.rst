.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: f57baedbe0775f314947529de50d636a

This signal is emitted whenever a checkable action changes its :sip:ref:`~PyQt6.QtGui.QAction.isChecked` status. This can be the result of a user interaction, or because :sip:ref:`~PyQt6.QtGui.QAction.setChecked` was called. As :sip:ref:`~PyQt6.QtGui.QAction.setChecked` changes the :sip:ref:`~PyQt6.QtGui.QAction`, it emits :sip:ref:`~PyQt6.QtGui.QAction.changed` in addition to .

*checked* is true if the action is checked, or false if the action is unchecked.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.activate`, :sip:ref:`~PyQt6.QtGui.QAction.triggered`, checked.
