
  FileNotFoundError

  [Errno 2] No such file or directory: b'/usr/games/poetry2setup'

  at ~/.pyenv/versions/3.8.6/lib/python3.8/os.py:601 in _execvpe
       597│         path_list = map(fsencode, path_list)
       598│     for dir in path_list:
       599│         fullname = path.join(dir, file)
       600│         try:
    →  601│             exec_func(fullname, *argrest)
       602│         except (FileNotFoundError, NotADirectoryError) as e:
       603│             last_exc = e
       604│         except OSError as e:
       605│             last_exc = e
