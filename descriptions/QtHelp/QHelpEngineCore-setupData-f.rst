.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: cc93743f79fa10e43c24dff540197a49

Sets up the help engine by processing the information found in the collection file and returns true if successful; otherwise returns false.

By calling the function, the help engine is forced to initialize itself immediately. Most of the times, this function does not have to be called explicitly because getter functions which depend on a correctly set up help engine do that themselves.

**Note:** ``qsqlite4.dll`` needs to be deployed with the application as the help system uses the sqlite driver when loading help collections.
