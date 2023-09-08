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

        This method takes all text files in the source directory and categorizes them based on language.
        For each text file, the function extracts the language information from the filename, assuming it is
        located at the start of the filename and separated by a hyphen ("-"). It then creates a separate
        subdirectory for each language (if one doesn't already exist) and moves the corresponding file into
        its respective language subdirectory. This effectively organizes the files based on their language.
        The process works as follows:
            1. Create an empty dictionary to store language directories.
            2. List all files in the source directory.
            3. Iterate through each file in the source directory:
                a. Extract the language prefix from the filename by splitting at the first hyphen ("-").
                b. Check if a subdirectory for the language already exists in the source directory.
                c. If it exists, add the file to the list of files for that language.
                d. If it doesn't exist, create a new subdirectory for the language and add the file to it.
            4. Move each file to its respective language subdirectory.
            5. After processing all files, the source directory will be organized into subdirectories by language.

        param: self (FileOrganizerService): The FileOrganizerService instance with the source directory.
        Returns: None
        """
        directors_name: dict = {}
        files: list = self.list_files()
        for file in files:
            prefix = file.split("-")[0]
            if prefix in directors_name:
                directors_name[prefix].append(file)
            else:
                directors_name[prefix] = [file]

        for directory in directors_name.keys():
            os.mkdir(f"{self.source_dir}/{directory}")
            for file in directors_name[directory]:
                shutil.move(f"{self.source_dir}/{file}", f"{self.source_dir}/{directory}/{file}")

        print("solution 1 Done!!.")


if __name__ == "__main__":
    source_dir = "files"
    organizer = FileOrganizerService(source_dir)
    organizer.organize_files()
