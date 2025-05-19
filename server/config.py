import os
def get_env(name: str) -> str:
    try:
        return os.environ[name]
    except KeyError:
        raise EnvironmentError(f"Required environment variable '{name}' not found.")


CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): get_env("TEAMS_RANGE").split("/")[0].format(i)
             for i in range(int(get_env("TEAMS_RANGE").split("/")[1]), int(get_env("TEAMS_RANGE").split("/")[2]) + 1)},
    'FLAG_FORMAT': r'{}'.format(get_env("FLAG_REGEX")),

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    # 'SYSTEM_PROTOCOL': 'ructf_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,

    'SYSTEM_PROTOCOL': 'ructf_http',
    'SYSTEM_URL': get_env("SUBMIT_URL"),
    'SYSTEM_TOKEN': get_env("TEAM_TOKEN"),

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 5,
    'FLAG_LIFETIME': 5 * 60,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': get_env("SERVER_PASSWORD"),

    # Use authorization for API requests
    'ENABLE_API_AUTH': False,
    'API_TOKEN': '00000000000000000000'
}
