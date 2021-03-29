.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fe0faa6298d2c802b8df8b37bc801cfa

Flushes the painting pipeline and prepares for the user issuing commands directly to the underlying graphics context. Must be followed by a call to :sip:ref:`~PyQt6.QtGui.QPainter.endNativePainting`.

Note that only the states the underlying paint engine changes will be reset to their respective default states. The states we reset may change from release to release. The following states are currently reset in the OpenGL 2 engine:

* blending is disabled

* the depth, stencil and scissor tests are disabled

* the active texture unit is reset to 0

* the depth mask, depth function and the clear depth are reset to their default values

* the stencil mask, stencil operation and stencil function are reset to their default values

* the current color is reset to solid white

If, for example, the OpenGL polygon mode is changed by the user inside a beginNativePaint()/\ :sip:ref:`~PyQt6.QtGui.QPainter.endNativePainting` block, it will not be reset to the default state by :sip:ref:`~PyQt6.QtGui.QPainter.endNativePainting`. Here is an example that shows intermixing of painter commands and raw OpenGL commands:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py
    :lines: 374-386

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.endNativePainting`.
