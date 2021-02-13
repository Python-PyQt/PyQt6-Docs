.. sip:method-description::
    :status: todo
    :pysig: aa1ba9d76abe46cbd94da153f8fd9029
    :realsig: (QMenu*)
    :digest: 79f482480bc77442917fd9bdcfa5e01c

Appends *menu* to the menu bar. Returns the menu's menuAction(). The menu bar does not take ownership of the menu.

**Note:** The returned :sip:ref:`~PyQt6.QtGui.QAction` object can be used to hide the corresponding menu.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu.menuAction`.
