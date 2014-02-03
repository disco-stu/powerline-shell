def add_postgres_segment():
    from os import getenv

    pgservice = getenv('PGSERVICE')

    if pgservice:
        # PGSERVICE is defined
        color_background = Color.PG_ENV_BG_SERVICE
        color_foreground = Color.PG_ENV_FG_SERVICE

        pg_prompt = " [%s] " % (pgservice,)

    else:
        # PGSERVICE is not defined, use other env variables
        pghost = getenv('PGHOST')
        pgport = getenv('PGPORT')
        pguser = getenv('PGUSER')

        # don't add a segment if none of the three env
        # variables are set
        if not (pghost or pgport or pguser):
            return

        color_background = Color.PG_ENV_BG
        color_foreground = Color.PG_ENV_FG

        # if PGPORT or PGUSER are not set we use the default settings
        if pgport is None: pgport = '5432'
        if pguser is None: pguser = getenv('USER')

        pg_prompt = " %s@%s:%s " % (pguser, pghost, pgport)

    powerline.append(pg_prompt, color_foreground, color_background)


add_postgres_segment()
