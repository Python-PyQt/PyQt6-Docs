.. sip:method-description::
    :status: todo
    :pysig: b16a546a263ee3fad1b76b5f0d76d77e
    :realsig: (const QTextCursor&) const
    :digest: ae3776e529ef4f9fa6ad19b4a134e560

Returns ``true`` if this cursor and *other* are copies of each other, i.e. one of them was created as a copy of the other and neither has moved since. This is much stricter than equality.

.. seealso:: operator=(), operator==().
