.. sip:method-description::
    :status: todo
    :pysig: a224e19238458489966f90a03a7a4379
    :realsig: () const
    :digest: 10146391ce862352abf0fa3bd7264250

Returns the maximum margins that would be applied if the page layout was in :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.StandardMode`.

The maximum margins allowed are calculated as the full size of the page minus the minimum margins set. For example, if the page width is 100 points and the minimum right margin is 10 points, then the maximum left margin will be 90 points.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageLayout.setMinimumMargins`, :sip:ref:`~PyQt6.QtGui.QPageLayout.minimumMargins`.
