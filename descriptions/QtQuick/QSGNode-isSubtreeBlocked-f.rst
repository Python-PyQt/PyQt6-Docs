.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 844a5c891620f5a59217f05ba8776c99

Returns whether this node and its subtree is available for use.

Blocked subtrees will not get their dirty states updated and they will not be rendered.

The :sip:ref:`~PyQt6.QtQuick.QSGOpacityNode` will return a blocked subtree when accumulated opacity is 0, for instance.
