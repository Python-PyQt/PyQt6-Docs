.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 9e9166f3c68f4fa013b504788dd156c8

Close the window.

This closes the window, effectively calling :sip:ref:`~PyQt6.QtGui.QWindow.destroy`, and potentially quitting the application. Returns ``true`` on success, false if it has a parent window (in which case the top level window should be closed instead).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.destroy`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.quitOnLastWindowClosed`, :sip:ref:`~PyQt6.QtGui.QWindow.closeEvent`.
