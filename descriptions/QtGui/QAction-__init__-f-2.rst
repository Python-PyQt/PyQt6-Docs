.. sip:method-description::
    :status: todo
    :pysig: f2ba375ef49a240c9e5f8fdab57ac9c8
    :realsig: (const QIcon&,const QString&,QObject*)
    :digest: 6e1955ee1fc3591388ac013e42fffc63

Constructs an action with an *icon* and some *text* and *parent*. If *parent* is an action group the action will be automatically inserted into the group.

The action uses a stripped version of *text* (e.g. "&Menu Option..." becomes "Menu Option") as descriptive text for tool buttons. You can override this by setting a specific description with :sip:ref:`~PyQt6.QtGui.QAction.setText`. The same text will be used for tooltips unless you specify a different text using :sip:ref:`~PyQt6.QtGui.QAction.setToolTip`.
