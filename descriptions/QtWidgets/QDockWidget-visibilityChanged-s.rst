.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 8c52f45aad9c3833e2f3981979b32511

This signal is emitted when the dock widget becomes *visible* (or invisible). This happens when the widget is hidden or shown, as well as when it is docked in a tabbed dock area and its tab becomes selected or unselected.

**Note:** The signal can differ from :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`. This can be the case, if a dock widget is minimized or tabified and associated to a non-selected or inactive tab.
