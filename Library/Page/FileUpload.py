class FileChooser:

    upload_element_locator = "input[name=\"file\"]"
    upload_button = "input:has-text(\"Upload\")"
    uploaded_file_locator = "#uploaded-files"
    file_to_upload = None

    @staticmethod
    def silent_upload_file(page, filepath):
        page.set_input_files(FileChooser.upload_element_locator, filepath)
        page.click(FileChooser.upload_button)

    @staticmethod
    def click_on_file_upload(page):
        page.click(FileChooser.upload_element_locator)
        page.click(FileChooser.upload_button)

    @staticmethod
    def set_filepath_upload(filepath):
        FileChooser.file_to_upload = filepath

    @staticmethod
    def get_uploaded_file_name(page):
        element = page.query_selector(FileChooser.uploaded_file_locator)
        return element.text_content()
