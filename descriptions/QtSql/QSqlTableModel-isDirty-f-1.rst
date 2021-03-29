.. sip:method-description::
    :status: todo
    :pysig: 6fb4529d327b1b51fc62577b3656a5a6
    :realsig: (const QModelIndex&) const
    :digest: 24c0064da964bb582801db0102336e5d

Returns ``true`` if the value at the index *index* is dirty, otherwise false. Dirty values are values that were modified in the model but not yet written into the database.

If *index* is invalid or points to a non-existing row, false is returned.
