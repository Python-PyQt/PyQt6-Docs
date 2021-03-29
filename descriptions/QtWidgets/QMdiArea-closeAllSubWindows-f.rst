.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d7aa33ee8e5899ca64be15739a4f8c85

Closes all subwindows by sending a :sip:ref:`~PyQt6.QtGui.QCloseEvent` to each window. You may receive :sip:ref:`~PyQt6.QtWidgets.QMdiArea.subWindowActivated` signals from subwindows before they are closed (if the MDI area activates the subwindow when another is closing).

Subwindows that ignore the close event will remain open.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.closeActiveSubWindow`.
