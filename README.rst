
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
    countdown       Generate sound
    exercise        Exercise Tool
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
    --dry / --no-dry          [default: no-dry]
    --silence / --no-silence  [default: no-silence]
    --duration INTEGER
    --prepare INTEGER
    --end INTEGER
    --rest INTEGER
    --rounds INTEGER
    --name TEXT
    -h, --help                Show this message and exit.

sportbot countdown
******************
.. code-block::

  Usage: sportbot countdown [OPTIONS] DURATION

    Generate sound

  Options:
    --paused
    -h, --help  Show this message and exit.

sportbot exercise
*****************
.. code-block::

  Usage: sportbot exercise [OPTIONS] COMMAND [ARGS]...

    Exercise Tool

  Options:
    -h, --help  Show this message and exit.

  Commands:
    custom  Start custom exercise
    help    Print help
    list    List available exercises
    start   Start exercise
    tags    List available tags

sportbot exercise custom
************************
.. code-block::

  Usage: sportbot exercise custom [OPTIONS] NAME

    Start custom exercise

  Options:
    --duration INTEGER
    --dry / --no-dry          [default: no-dry]
    --silence / --no-silence  [default: no-silence]
    -h, --help                Show this message and exit.

sportbot exercise list
**********************
.. code-block::

  Usage: sportbot exercise list [OPTIONS]

    List available exercises

  Options:
    --tag TEXT  Tag filter
    -h, --help  Show this message and exit.

sportbot exercise start
***********************
.. code-block::

  Usage: sportbot exercise start [OPTIONS] NAME

    Start exercise

  Options:
    --dry / --no-dry          [default: no-dry]
    --silence / --no-silence  [default: no-silence]
    -h, --help                Show this message and exit.

sportbot exercise tags
**********************
.. code-block::

  Usage: sportbot exercise tags [OPTIONS]

    List available tags

  Options:
    -h, --help  Show this message and exit.

sportbot generate-sound
***********************
.. code-block::

  Usage: sportbot generate-sound [OPTIONS] NAME

    Generate sound

  Options:
    --dry / --no-dry  [default: no-dry]
    --test            Test sound afterwards
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
    --dry / --no-dry          [default: no-dry]
    --silence / --no-silence  [default: no-silence]
    -h, --help                Show this message and exit.

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
    --dry / --no-dry          [default: no-dry]
    --silence / --no-silence  [default: no-silence]
    -h, --help                Show this message and exit.

sportbot version
****************
.. code-block::

  Usage: sportbot version [OPTIONS]

    Print version, equivalent to -V and --version

  Options:
    -h, --help  Show this message and exit.
