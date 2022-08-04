import shutil

class Backup:
    def __init__(self, file_path, backup_path, succ_path, err_path):
        self.file_path = file_path
        self.backup_path = backup_path
        self.succ_path = succ_path
        self.err_path = err_path

    def backup(bac):

        source = bac.file_path
        destination = bac.backup_path

        shutil.copy(source, destination) 