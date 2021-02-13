.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 002a3b83e48120a3cf5516cc9ed951c9

Removes all the actions from the menu bar.

**Note:** On macOS, menu items that have been merged to the system menu bar are not removed by this function. One way to handle this would be to remove the extra actions yourself. You can set the :sip:ref:`~PyQt6.QtGui.QAction.MenuRole` on the different menus, so that you know ahead of time which menu items get merged and which do not. Then decide what to recreate or remove yourself.

.. seealso:: removeAction().
