.. sip:method-description::
    :status: todo
    :pysig: 6b16365c76467cbb63d7779f3524ef66
    :realsig: (QValue3DAxis*)
    :digest: d9456095fe1059e062e8bf9c71064b61

Releases the ownership of the *axis* back to the caller, if it is added to this graph. If the released *axis* is in use, a new default axis will be created and set active.

If the default axis is released and added back later, it behaves as any other axis would.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.setAxisX`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.setAxisY`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.setAxisZ`.
