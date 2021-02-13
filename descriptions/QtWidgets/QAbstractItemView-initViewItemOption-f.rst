.. sip:method-description::
    :status: todo
    :pysig: 6eb9d9b83b0045868fcce4b82464953d
    :realsig: (QStyleOptionViewItem*) const
    :digest: 719ee51d8e487381a38e0e6eff61601a

Initialize the *option* structure with the view's palette, font, state, alignments etc.

**Note:** Implementations of this methods should check the version of the structure received, populate all members the implementation is familiar with, and set the version member to the one supported by the implementation before returning.
