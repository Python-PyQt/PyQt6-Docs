.. sip:method-description::
    :status: todo
    :pysig: d4a876a1050c3c6176211bf95f61ce45
    :realsig: (const QByteArray&,int)
    :digest: 4acd35bcaa5da5de22ee3d297a26f8d8

Restores the *state* of this mainwindow's toolbars and dockwidgets. Also restores the corner settings too. The *version* number is compared with that stored in *state*. If they do not match, the mainwindow's state is left unchanged, and this function returns ``false``; otherwise, the state is restored, and this function returns ``true``.

To restore geometry saved using :sip:ref:`~PyQt6.QtCore.QSettings`, you can use code like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmainwindow.py
    :lines: 65-70

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow.saveState`, :sip:ref:`~PyQt6.QtWidgets.QWidget.saveGeometry`, :sip:ref:`~PyQt6.QtWidgets.QWidget.restoreGeometry`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.restoreDockWidget`.
