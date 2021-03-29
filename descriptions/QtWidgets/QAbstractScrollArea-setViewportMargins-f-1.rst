.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int,int,int,int)
    :digest: 47b501ec30c8bd56de05145378dbff42

Sets the margins around the scrolling area to *left*, *top*, *right* and *bottom*. This is useful for applications such as spreadsheets with "locked" rows and columns. The marginal space is is left blank; put widgets in the unused area.

Note that this function is frequently called by :sip:ref:`~PyQt6.QtWidgets.QTreeView` and :sip:ref:`~PyQt6.QtWidgets.QTableView`, so margins must be implemented by :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` subclasses. Also, if the subclasses are to be used in item views, they should not call this function.

By default all margins are zero.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewportMargins`.
