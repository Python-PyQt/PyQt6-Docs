.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 5a26b634fa098092d3694ccdb6aa244d

Removes the directory, including all its contents.

Returns ``true`` if successful, otherwise false.

If a file or directory cannot be removed,  keeps going and attempts to delete as many files and sub-directories as possible, then returns ``false``.

If the directory was already removed, the method returns ``true`` (expected result already reached).

**Note:** This function is meant for removing a small application-internal directory (such as a temporary directory), but not user-visible directories. For user-visible operations, it is rather recommended to report errors more precisely to the user, to offer solutions in case of errors, to show progress during the deletion since it could take several minutes, etc.
