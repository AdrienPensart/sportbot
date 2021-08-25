
Commands
--------
.. code-block::

  Usage: sportbot [OPTIONS] COMMAND [ARGS]...

    SportBot.

  Options:
    --debug        Verbose mode
    -V, --version  Show the version and exit.
    -h, --help     Show this message and exit.

  Commands:
    boxing          Boxing Training
    completion      Shell completion
    countdown       Generate sound
    exercice        Exercice Tool
    generate-sound  Generate sound
    help            Print help
    readme (doc)    Generates a README.rst
    sequence        Sequence Tool
    training        Training Tool
    version         Print version

sportbot boxing
***************
.. code-block::

  Usage: sportbot boxing [OPTIONS] COMMAND [ARGS]...

    Boxing Training

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help    Print help
    rounds  Create custom rounds

sportbot boxing rounds
**********************
.. code-block::

  Usage: sportbot boxing rounds [OPTIONS]

    Create custom rounds

  Options:
    --dry
    --name TEXT
    --rounds INTEGER
    --duration INTEGER
    --prepare INTEGER
    --end INTEGER
    --rest INTEGER
    -h, --help          Show this message and exit.

sportbot completion
*******************
.. code-block::

  Usage: sportbot completion [OPTIONS] COMMAND [ARGS]...

    Shell completion subcommand

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help                   Print help
    install                Install the click-completion-command completion
    show (generate,print)  Show the click-completion-command completion code

sportbot completion install
***************************
.. code-block::

  Usage: sportbot completion install [OPTIONS] [[bash|fish|zsh|powershell]] [PATH]

    Auto install shell completion code in your rc file

  Options:
    -i, --case-insensitive  Case insensitive completion
    --append / --overwrite  Append the completion code to the file
    -h, --help              Show this message and exit.

sportbot completion show
************************
.. code-block::

  Usage: sportbot completion show [OPTIONS] [[bash|fish|zsh|powershell]]

    Generate shell code to enable completion

  Options:
    -i, --case-insensitive  Case insensitive completion
    -h, --help              Show this message and exit.

sportbot countdown
******************
.. code-block::

  Usage: sportbot countdown [OPTIONS] DURATION

    Generate sound

  Options:
    --paused
    -h, --help  Show this message and exit.

sportbot exercice
*****************
.. code-block::

  Usage: sportbot exercice [OPTIONS] COMMAND [ARGS]...

    Exercice Tool

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help   Print help
    list   List available exercices
    start  Start exercice
    tags   List available tags

sportbot exercice list
**********************
.. code-block::

  Usage: sportbot exercice list [OPTIONS]

    List available exercices

  Options:
    --tag TEXT  Tag filter
    -h, --help  Show this message and exit.

sportbot exercice start
***********************
.. code-block::

  Usage: sportbot exercice start [OPTIONS] NAME

    Start exercice

  Options:
    --dry
    -h, --help  Show this message and exit.

sportbot exercice tags
**********************
.. code-block::

  Usage: sportbot exercice tags [OPTIONS]

    List available tags

  Options:
    -h, --help  Show this message and exit.

sportbot generate-sound
***********************
.. code-block::

  Usage: sportbot generate-sound [OPTIONS] NAME

    Generate sound

  Options:
    --dry
    --force           Recreate sound if already exists
    --path DIRECTORY  Sound output path  [default: .]
    -h, --help        Show this message and exit.

sportbot help
*************
.. code-block::

  Usage: sportbot help [OPTIONS]

    Print help

  Options:
    -h, --help  Show this message and exit.

sportbot readme
***************
.. code-block::

  Usage: sportbot readme [OPTIONS]

    Generates a complete readme

  Options:
    --output [rst|markdown]  README output format  [default: rst]
    -h, --help               Show this message and exit.

sportbot sequence
*****************
.. code-block::

  Usage: sportbot sequence [OPTIONS] COMMAND [ARGS]...

    Sequence Tool

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help   Print help
    list   List available sequences
    start  Start sequence

sportbot sequence list
**********************
.. code-block::

  Usage: sportbot sequence list [OPTIONS]

    List available sequences

  Options:
    --tag TEXT  Tag filter
    -h, --help  Show this message and exit.

sportbot sequence start
***********************
.. code-block::

  Usage: sportbot sequence start [OPTIONS] NAME

    Start sequence

  Options:
    --dry
    -h, --help  Show this message and exit.

sportbot training
*****************
.. code-block::

  Usage: sportbot training [OPTIONS] COMMAND [ARGS]...

    Training Tool

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help   Print help
    list   List available trainings
    start  Start training

sportbot training list
**********************
.. code-block::

  Usage: sportbot training list [OPTIONS]

    List available trainings

  Options:
    --tag TEXT  Tag filter
    -h, --help  Show this message and exit.

sportbot training start
***********************
.. code-block::

  Usage: sportbot training start [OPTIONS] NAME

    Start training

  Options:
    --dry
    -h, --help  Show this message and exit.

sportbot version
****************
.. code-block::

  Usage: sportbot version [OPTIONS]

    Print version, equivalent to -V and --version

  Options:
    -h, --help  Show this message and exit.
