.. sip:method-description::
    :status: todo
    :pysig: be4cf29ba73c5c1c9c66cbed303bedcd
    :realsig: (const QString&,QObject*)
    :digest: 652e109a004c465941065db0014f496a

Constructs an action with some *text* and *parent*. If *parent* is an action group the action will be automatically inserted into the group.

The action uses a stripped version of *text* (e.g. "&Menu Option..." becomes "Menu Option") as descriptive text for tool buttons. You can override this by setting a specific description with :sip:ref:`~PyQt6.QtGui.QAction.setText`. The same text will be used for tooltips unless you specify a different text using :sip:ref:`~PyQt6.QtGui.QAction.setToolTip`.
