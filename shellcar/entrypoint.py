from .main import main


def entrypoint():
    main(auto_envvar_prefix='SHELLCAR', obj={})


if __name__ == '__main__':
    entrypoint()
