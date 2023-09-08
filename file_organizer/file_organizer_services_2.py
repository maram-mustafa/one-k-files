import os
import shutil


class FileOrganizerService:
    def __init__(self, source_dir: str):
        """
        Initialize the FileOrganizerService with a source folder.
        :param source_dir: The directory where files are to be organized.
        """
        self.source_dir = source_dir

    def list_files(self) -> list:
        """
        List files in the source folder.
        :return: A list of filenames in the source folder.
        """
        return os.listdir(self.source_dir)

    def organize_files(self) -> None:
        """
         Organizes text files in the source folder into subdirectories by language.
         For each text file in the source folder, this function follows these steps to organize the files:
            1. Extracts the language information from the filename by splitting the filename at the first "-" character.
            2. Creates a corresponding language subdirectory (if it doesn't already exist) within the source directory.
            3. Moves the file into the appropriate language subdirectory.
        This effectively organizes the files by their respective languages based on the filename.
        Note:
        - This function is designed to work specifically with text files (.txt).
        - It expects the language information to be at the start of the filename, separated by a "-" character.

        param: self (FileOrganizerService): The FileOrganizerService instance with the source directory.
        Returns: None
        """
        files: list = self.list_files()

        for filename in files:
            language: str = filename.split("-")[0]
            language_folder: str = os.path.join(self.source_dir, language)
            if not os.path.exists(language_folder):
                os.mkdir(language_folder)

            source_path: str = os.path.join(self.source_dir, filename)
            destination_path: str = os.path.join(language_folder, filename)
            shutil.move(source_path, destination_path)

        print("solution 2 Done!!.")


if __name__ == "__main__":
    source_dir = "files2"
    organizer = FileOrganizerService(source_dir)
    organizer.organize_files()
