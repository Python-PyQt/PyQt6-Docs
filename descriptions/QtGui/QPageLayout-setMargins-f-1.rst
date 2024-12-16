.. sip:method-description::
    :status: todo
    :pysig: 1d68dfcaabf269f899a0114a3cdcebdb
    :realsig: (const QMarginsF&, QPageLayout::OutOfBoundsPolicy)
    :digest: 908f3ae1533066e9cbe1a163b07ddf95

Sets the page margins of the page layout to *margins*. Returns true if the margins were successfully set.

The units used are those currently defined for the layout. To use different units then call :sip:ref:`~PyQt6.QtGui.QPageLayout.setUnits` first.

Since Qt 6.8, the optional *outOfBoundsPolicy* can be used to specify how margins that are out of bounds are handled.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageLayout.margins`, :sip:ref:`~PyQt6.QtGui.QPageLayout.units`.
