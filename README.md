##keep running

Kepp a script or bash cmd running. Relaunch the command or script when exit.

https://pypi.python.org/pypi/keep-running

##installation
```bash
pip install keep-running
```

##usage

For example: `test-program.sh`

```bash
#!/bin/bash
for i in {1..10}
do
    echo `date` ':' $i
    sleep 1
done
```

Keep it running:

```bash
$ keep-running test-program.sh
```

## files

*   log file

    The log file will be: `test-program.sh.log` in the same directory with `test-program.sh`.

*   lock file

    The file used to lock is `test-program.sh.lock`.

Enjoy coding!
