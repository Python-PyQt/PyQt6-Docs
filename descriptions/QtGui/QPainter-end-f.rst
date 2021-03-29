.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: ff5791d5daa10f15b338d08f14806ec9

Ends painting. Any resources used while painting are released. You don't normally need to call this since it is called by the destructor.

Returns ``true`` if the painter is no longer active; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.begin`, :sip:ref:`~PyQt6.QtGui.QPainter.isActive`.
