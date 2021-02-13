.. sip:method-description::
    :status: todo
    :pysig: 43cc8e7273b526a91035ca8472a045a7
    :realsig: (QStyleOptionMenuItem*,const QAction*) const
    :digest: 3d61ac48cd0817d2bde3a8994f028b3b

Initialize *option* with the values from the menu bar and information from *action*. This method is useful for subclasses when they need a :sip:ref:`~PyQt6.QtWidgets.QStyleOptionMenuItem`, but don't want to fill in all the information themselves.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption.initFrom`, :sip:ref:`~PyQt6.QtWidgets.QMenu.initStyleOption`.
