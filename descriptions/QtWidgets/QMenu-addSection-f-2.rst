.. sip:method-description::
    :status: todo
    :pysig: 925c718874d262ea938e2e6d7d77a1fd
    :realsig: (const QString&)
    :digest: 8429dd67282193953bc0c5f7809dee8f

This convenience function creates a new section action, i.e. an action with :sip:ref:`~PyQt6.QtGui.QAction.isSeparator` returning true but also having *text* hint, and adds the new action to this menu's list of actions. It returns the newly created action.

The rendering of the hint is style and platform dependent. Widget styles can use the text information in the rendering for sections, or can choose to ignore it and render sections like simple separators.

:sip:ref:`~PyQt6.QtWidgets.QMenu` takes ownership of the returned :sip:ref:`~PyQt6.QtGui.QAction`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`.
