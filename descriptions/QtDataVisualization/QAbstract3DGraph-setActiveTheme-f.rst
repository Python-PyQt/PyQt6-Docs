.. sip:method-description::
    :status: todo
    :pysig: 4d6c66505eca862e9156683cee5bcac1
    :realsig: (Q3DTheme*)
    :digest: 180e7679474b9b3e21be475bc2722547

Sets *theme* as the active theme to be used for the graph. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.addTheme` to transfer the ownership of the theme to this graph.

If *theme* is null, a temporary default theme is created. This temporary theme is destroyed if any theme is explicitly set later. Properties of the theme can be modified even after setting it, and the modifications take effect immediately.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.activeTheme`.
