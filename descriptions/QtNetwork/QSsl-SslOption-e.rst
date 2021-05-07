.. sip:enum-description::
    :status: todo
    :digest: aea6d8b955c9f14ba8ff66692c783b2d

Describes the options that can be used to control the details of SSL behaviour. These options are generally used to turn features off to work around buggy servers.

By default,  is turned on since this causes problems with a large number of servers.  is also turned on, since it introduces a security risk.  is turned on to prevent the attack publicised by CRIME.  is turned on to optimize memory usage. The other options are turned off.

**Note:** Availability of above options depends on the version of the SSL backend in use.
