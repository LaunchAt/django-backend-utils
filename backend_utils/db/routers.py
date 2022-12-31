from .settings import DATABASES


class ReadAndWriteRouter:
    def db_for_read(self, *args, **kwargs):
        if 'readonly' in DATABASES:
            return 'readonly'

        return 'default'

    def db_for_write(self, *args, **kwargs):
        return 'default'

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_migrate(self, *args, **kwargs):
        return True
