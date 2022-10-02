.. sip:method-description::
    :status: todo
    :pysig: 6b2bf89750753e58edf8cbb690cd016f
    :realsig: (int,int,QSizePolicy::Policy,QSizePolicy::Policy)
    :digest: d30ada090859255742efc120286c6023

Changes this spacer item to have preferred width *w*, preferred height *h*, horizontal size policy *hPolicy* and vertical size policy *vPolicy*.

The default values provide a gap that is able to stretch if nothing else wants the space.

Note that if changeSize() is called after the spacer item has been added to a layout, it is necessary to invalidate the layout in order for the spacer item's new size to take effect.

.. seealso:: QSpacerItem::invalidate().
