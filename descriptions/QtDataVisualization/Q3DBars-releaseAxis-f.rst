.. sip:method-description::
    :status: todo
    :pysig: 929c9801a762c543b67465c2eb7bdf15
    :realsig: (QAbstract3DAxis*)
    :digest: c7ba9fc7f437162d1096003a64f9c0a0

Releases the ownership of the *axis* back to the caller, if it is added to this graph. If the released *axis* is in use, a new default axis will be created and set active.

If the default axis is released and added back later, it behaves as any other axis would.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.setValueAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.setRowAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.setColumnAxis`.
