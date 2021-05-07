.. sip:method-description::
    :status: todo
    :pysig: 4d6c66505eca862e9156683cee5bcac1
    :realsig: (Q3DTheme*)
    :digest: e469016093517265efb3cd48fb230af3

Releases the ownership of the *theme* back to the caller, if it was added to this graph. If the released *theme* is in use, a new default theme will be created and set active.

If the default theme is released and added back later, it behaves as any other theme would.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.addTheme`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.setActiveTheme`.
