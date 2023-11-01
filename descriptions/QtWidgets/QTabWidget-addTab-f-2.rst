.. sip:method-description::
    :status: todo
    :pysig: 2775b83bc7961876b93bee98cb97da10
    :realsig: (QWidget*, const QString&)
    :digest: 0d236a67d82c9beb457c6a0736a236ed

Adds a tab with the given *page* and *label* to the tab widget, and returns the index of the tab in the tab bar. Ownership of *page* is passed on to the :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

If the tab's *label* contains an ampersand, the letter following the ampersand is used as a shortcut for the tab, e.g. if the label is "Bro&wse" then Alt+W becomes a shortcut which will move the focus to this tab.

**Note:** If you call addTab() after show(), the layout system will try to adjust to the changes in its widgets hierarchy and may cause flicker. To prevent this, you can set the :sip:ref:`~PyQt6.QtWidgets.QWidget.updatesEnabled` property to false prior to changes; remember to set the property to true when the changes are done, making the widget receive paint events again.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget.insertTab`.
